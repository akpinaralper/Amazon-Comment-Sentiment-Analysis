from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import pandas as pd
import matplotlib.pyplot as plt
import time
import re

# 1. Tarayıcıyı başlat
options = Options()
options.add_argument("--window-size=1920,1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 2. Amazon ürün URL'si al
url = input("Amazon ürün URL'sini girin: ")
driver.get(url)

# 3. Sayfa yüklendi mi?
try:
    wait = WebDriverWait(driver, 15)
    wait.until(EC.presence_of_element_located((By.ID, 'productTitle')))
    print("✅ Sayfa yüklendi.")
except Exception as e:
    print("❌ Sayfa yüklenemedi:", e)
    driver.quit()
    exit()

# 4. Ürün başlığı
try:
    title = driver.find_element(By.ID, 'productTitle').text.strip()
    print("🛍️ Ürün Başlığı:", title)
except Exception:
    title = "Başlık alınamadı"

# 5. Manuel giriş bekleme
print("\n🔑 Lütfen Amazon hesabınıza giriş yapın.")
print("⏳ 30 saniye içinde giriş yapıp, sayfada kalmaya devam edin...")
time.sleep(30)

# 6. Yorumları çek
reviews = []
try:
    print("📝 Yorumlar çekiliyor...")

    asin_match = re.search(r"/dp/([A-Z0-9]{10})", url)
    if not asin_match:
        print("❌ ASIN kodu bulunamadı.")
        driver.quit()
        exit()

    asin = asin_match.group(1)
    review_url = f"https://www.amazon.com.tr/product-reviews/{asin}"
    driver.get(review_url)
    time.sleep(3)

    while True:
        WebDriverWait(driver, 15).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "span[data-hook='review-body']"))
        )
        time.sleep(2)

        review_elements = driver.find_elements(By.CSS_SELECTOR, "span[data-hook='review-body']")
        for r in review_elements:
            text = r.text.strip()
            if text:
                reviews.append(text)

        print(f"📦 {len(reviews)} yorum alındı...")

        try:
            next_button = driver.find_element(By.CSS_SELECTOR, "li.a-last a")
            driver.execute_script("arguments[0].click();", next_button)
            time.sleep(3)
        except:
            print("✅ Tüm sayfalar gezildi.")
            break

except Exception as e:
    print("❌ Yorumlar alınamadı:", e)

driver.quit()

if not reviews:
    print("🚫 Hiç yorum bulunamadı.")
    exit()

# 7. Duygu analizi başlat
print("\n🤖 Duygu analizi başlatılıyor...")
model_name = "savasy/bert-base-turkish-sentiment-cased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

sonuclar = []
for yorum in reviews[:50]:
    inputs = tokenizer(yorum, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        predicted = torch.argmax(logits, dim=1).item()
        duygu = ["Olumsuz", "Tarafsız", "Olumlu"][predicted]
        sonuclar.append((yorum, duygu))

# 8. DataFrame oluştur
df = pd.DataFrame(sonuclar, columns=["Yorum", "Duygu"])

# 9. Tarafsız yorum düzeltme
pozitif_kelime_seti = [
    "iyi", "güzel", "sorunsuz", "hızlı", "tavsiye", "beğendim", "memnun", "kaliteli",
    "şık", "fiyatına göre", "başarılı", "sağlam", "tatmin", "orijinal", "harika", "süper",
    "mükemmel", "kusursuz", "teşekkür", "bayıldım", "favorim", "etkileyici", "uçak hissiyatı"
]

def yumuşak_duygu_duzelt(yorum, duygu):
    yorum_kucuk = yorum.lower()
    if duygu == "Tarafsız":
        if any(kelime in yorum_kucuk for kelime in pozitif_kelime_seti):
            return "Olumlu"
        if len(yorum_kucuk.split()) <= 3 and any(kelime in yorum_kucuk for kelime in ["süper", "harika", "şahane", "beğendim", "mükemmel", "güzel"]):
            return "Olumlu"
    return duygu

df["Duygu"] = df.apply(lambda row: yumuşak_duygu_duzelt(row["Yorum"], row["Duygu"]), axis=1)

# 10. Uzun yorumları kısalt
df['Yorum'] = df['Yorum'].apply(lambda x: x[:175] + "..." if len(x) > 175 else x)

# 11. Terminal çıktısı
pd.set_option('display.max_colwidth', 175)
pd.set_option('display.width', 120)
pd.set_option('display.max_rows', 50)

print("\n📊 Analiz Sonuçları (İlk 50 Yorum):\n")
print(df.to_string(index=False))

# 12. Grafikler için hazırlık
duygular = ["Olumsuz", "Tarafsız", "Olumlu"]
duygu_sayim = df['Duygu'].value_counts().reindex(duygular, fill_value=0)
colors = ['red', 'gray', 'green']

# 12.0 Klasik bar grafiği
plt.figure(figsize=(7, 4))
bars = plt.bar(duygu_sayim.index, duygu_sayim.values, color=colors)
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.2, int(yval), ha='center', va='bottom', fontsize=12)

plt.title("Yorumların Duygu Dağılımı", fontsize=14)
plt.xlabel("Duygu", fontsize=12)
plt.ylabel("Yorum Sayısı", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 12.1 Yüzdelik bar grafiği - modern
plt.style.use("ggplot")
duygu_yuzde = (duygu_sayim / duygu_sayim.sum()) * 100

fig, ax = plt.subplots(figsize=(8, 5), facecolor="#f9f9f9")
bars = ax.bar(duygu_yuzde.index, duygu_yuzde.values, color=colors, edgecolor='black', linewidth=0.6)

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.1f}%", ha='center', va='bottom', fontsize=12, fontweight='bold')

ax.set_title("Yüzdelik Duygu Dağılımı", fontsize=16, fontweight='bold', color="#333")
ax.set_xlabel("Duygu", fontsize=13)
ax.set_ylabel("Yüzde (%)", fontsize=13)
ax.set_ylim(0, 100)
ax.grid(axis='y', linestyle='--', alpha=0.4)
ax.set_facecolor("#ffffff")
fig.patch.set_facecolor("#f9f9f9")

plt.tight_layout()
plt.show()

# 12.2 Pasta grafiği - modern
fig, ax = plt.subplots(figsize=(6, 6), facecolor="#f9f9f9")

wedges, texts, autotexts = ax.pie(
    duygu_sayim,
    labels=duygu_sayim.index,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    textprops={'fontsize': 12},
    wedgeprops={'edgecolor': 'black', 'linewidth': 0.5}
)

ax.set_title("Duygu Dağılımı (Pasta Grafiği)", fontsize=15, fontweight='bold', color="#333")
fig.patch.set_facecolor("#f9f9f9")
plt.tight_layout()
plt.show()

# 13. CSV’ye kaydet
df.to_csv("yorum_duygu_analizi.csv", index=False, encoding="utf-8-sig")
print("\n📁 Sonuçlar 'yorum_duygu_analizi.csv' dosyasına kaydedildi.")

