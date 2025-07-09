# Amazon-Comment-Sentiment-Analysis

# 🛍️ Amazon Yorum Duygu Analizi

Bu proje, Amazon Türkiye'deki ürün sayfalarından kullanıcı yorumlarını otomatik olarak çekip, Türkçe BERT modeli ile duygu analizi yapan bir Python uygulamasıdır.

---

## 🚀 Özellikler

- ✅ Amazon ürün yorumlarını Selenium ile toplar  
- ✅ Türkçe BERT modeli ile **Olumlu / Olumsuz / Tarafsız** duygu sınıflandırması yapar  
- ✅ Tarafsız yorumları pozitif içerik barındırıyorsa "Olumlu" olarak günceller  
- ✅ Analiz sonuçlarını tablo ve grafik olarak sunar  
- ✅ CSV çıktısı oluşturur

---

🖼️ **Örnek Çıktılar**

![duygu dagilimi1](https://github.com/user-attachments/assets/27af9da7-4165-4202-b6c2-2ad6be19bdc3)

![duygu dagilimi2](https://github.com/user-attachments/assets/acebfb67-abb5-4591-9ea4-9e4f873e1026)

![duygu dagilimi3](https://github.com/user-attachments/assets/aef00bec-fa37-40ad-b366-55e5850a7a38)


## 🧰 Kullanılan Teknolojiler

- Python  
- Selenium  
- Hugging Face Transformers (BERT)  
- PyTorch  
- Pandas  
- Matplotlib

---

## ⚙️ Kurulum


1.Depoyu klonlayın:
```bash
git clone https://github.com/akpinaralper/Amazon-Comment-Sentiment-Analysis.git
cd Amazon-Comment-Sentiment-Analysis


2.Gerekli kütüphaneleri yükleyin:
 ```bash
 pip install -r requirements.txt


veya:
  ```bash
  pip install selenium webdriver-manager torch transformers pandas matplotlib


🚦 Kullanım

Analiz yapmak istediğiniz ürünün Amazon linkini veya yorum verilerini belirtin.
Yorumları çekmek için:

python yorum_topla.py
Duygu analizi yapmak için:

python duygu_analiz.py
Sonuçlar yorum_duygu_analizi.csv dosyasına ve grafikler olarak kaydedilir.
