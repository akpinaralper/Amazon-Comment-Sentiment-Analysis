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


Örnek Çıktı 1:

![Duygu Dağılımı]blob/main/duygudagilimi1.png


Örnek Çıktı 2:
![duygu dagilimi2](https://github.com/user-attachments/assets/acebfb67-abb5-4591-9ea4-9e4f873e1026)

Örnek Çıktı 3:
![duygu dagilimi3](https://github.com/user-attachments/assets/aef00bec-fa37-40ad-b366-55e5850a7a38)


