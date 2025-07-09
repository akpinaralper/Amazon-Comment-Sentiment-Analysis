# Amazon-Comment-Sentiment-Analysis

## 🛍️ Amazon Yorum Duygu Analizi

Bu proje, Amazon Türkiye'deki ürün sayfalarından kullanıcı yorumlarını otomatik olarak çekip, Türkçe BERT modeli ile duygu analizi yapan bir Python uygulamasıdır.

---

## 🚀 Özellikler

- ✅ Amazon ürün yorumlarını Selenium ile toplar  
- ✅ Türkçe BERT modeli ile **Olumlu / Olumsuz / Tarafsız** duygu sınıflandırması yapar  
- ✅ Tarafsız yorumları pozitif içerik barındırıyorsa "Olumlu" olarak günceller  
- ✅ Analiz sonuçlarını tablo ve grafik olarak sunar  
- ✅ CSV çıktısı oluşturur

---

## 🖼️ Örnek Çıktılar

![duygu dagilimi1](https://github.com/user-attachments/assets/27af9da7-4165-4202-b6c2-2ad6be19bdc3)

![duygu dagilimi2](https://github.com/user-attachments/assets/acebfb67-abb5-4591-9ea4-9e4f873e1026)

![duygu dagilimi3](https://github.com/user-attachments/assets/aef00bec-fa37-40ad-b366-55e5850a7a38)

---

## 🧰 Kullanılan Teknolojiler

- Python  
- Selenium  
- Hugging Face Transformers (BERT)  
- PyTorch  
- Pandas  
- Matplotlib  
- Seaborn

---

## ⚙️ Kurulum

1. Depoyu klonlayın:

   ```bash
   git clone https://github.com/akpinaralper/Amazon-Comment-Sentiment-Analysis.git
   cd Amazon-Comment-Sentiment-Analysis

2. Gerekli kütüphaneleri yükleyin:

   ```bash
   pip install -r requirements.txt
   veya elle yüklemek istersen:
   pip install selenium webdriver-manager torch transformers pandas matplotlib seaborn





---
🚦 Kullanım

Bu proje iki ana adımdan oluşur:

Amazon ürün yorumlarının toplanması

Bu yorumlara duygu analizi uygulanması

Aşağıdaki adımları takip ederek analiz sürecini başlatabilirsiniz:

1. Ürün bağlantısını hazırlayın
Amazon Türkiye üzerinde yorumları bulunan bir ürün sayfasını açın.
Tarayıcınızın adres çubuğundaki ürün bağlantısını kopyalayın. Örneğin:

arduino
[https://www.amazon.com.tr/dp/B0C1234567](https://www.amazon.com.tr/Multi-Let-Toprakl%C4%B1-Kablolu-Korumal%C4%B1-Metre-Beyaz/dp/B07CJHQ5MR/ref=zg_bs_c_home-improvement_d_sccl_1/257-7353852-7269744?pd_rd_w=88GfC&content-id=amzn1.sym.f39ea4be-1606-4425-a28a-b0b62417f306&pf_rd_p=f39ea4be-1606-4425-a28a-b0b62417f306&pf_rd_r=5RET3MH6MDCJS5WGCHCB&pd_rd_wg=o2sE6&pd_rd_r=7ee6f16a-a896-4f3f-835d-a7e0cfb7299f&pd_rd_i=B07CJHQ5MR&th=1)

Program sizden Amazon hesabınıza giriş yapmanızı isteyecektir.
Bu sırada, 30 saniyelik bir süre tanınır. Giriş yaptıktan sonra otomatik olarak yorumlar toplanacaktır.

Analiz tamamlandıktan sonra:

Tüm yorum ve duygu sonuçları yorum_duygu_analizi.csv dosyasına kaydedilir

Yorumların dağılımını gösteren grafikler (bar, pasta ve yüzdelik harita) otomatik olarak açılır
