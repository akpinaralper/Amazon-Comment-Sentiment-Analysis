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

## 🧰 Kullanılan Teknolojiler

- Python  
- Selenium  
- Hugging Face Transformers (BERT)  
- PyTorch  
- Pandas  
- Matplotlib

---

## ⚙️ Kurulum

Gerekli kütüphaneleri yüklemek için:

```bash
pip install selenium webdriver-manager torch transformers pandas matplotlib


