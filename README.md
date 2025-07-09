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
![duygu dagilimi1](https://github.com/user-attachments/assets/c4c2f86d-2dc0-4dc5-be4b-7643cc100a40)

Örnek Çıktı 2:
![duygu dagilimi2](https://github.com/user-attachments/assets/01dad2f7-4d06-4ad6-a17a-7785064d9c9f)

Örnek Çıktı 3:
![duygu dagilimi3](https://github.com/user-attachments/assets/158b76d0-87a8-4565-85ed-6dd37ce3d8b7)


