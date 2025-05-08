# 📊 Splunk HEC Dummy Log Generator

Selamat datang di repo ini! Di sini kamu akan menemukan koleksi script Python untuk menghasilkan **dummy log** berbagai jenis sistem keamanan (Firewall, EDR, Malware, dll) yang bisa langsung dikirim ke **Splunk melalui HEC (HTTP Event Collector)**.

🎯 **Tujuan Repo Ini**

- Memudahkan pengujian Splunk HEC tanpa log dari production
    
- Simulasi dashboard untuk SIEM
    
- Latihan parsing field dan validasi sourcetype
    
- Keperluan demo, workshop, atau edukasi SOC
    

---

## 📁 Struktur Direktori

```
.
├── logs/
│   ├── firewall_logs.json
│   ├── malware_logs.json
│   └── edr_logs.json
├── scripts/
│   ├── generator_firewall.py
│   ├── generator_malware.py
│   └── generator_edr.py
├── README.md
```

---

## 🚀 Cara Menggunakan

1. **Jalankan Python script**
    

```bash
python3 generator_firewall.py
```

2. **Hasil akan muncul di file:**
    

```
firewall_logs.json
```

3. **(Opsional) Kirim log file .json ke Splunk HEC**
    
```bash
curl -k https://<Splunk-HEC-Host>:8088/services/collector \
  -H "Authorization: Splunk <Splunk-HEC-Token>" \
  -H "Content-Type: application/json" \
  -d @firewall_logs.json
```

Example : 
```bash
curl -k https://10.20.30.40:8088/services/collector \
  -H "Authorization: Splunk c435248c-ac6c-433d-b800-zakezkaezake" \
  -H "Content-Type: application/json" \
  -d @firewall_logs.json
```

4. **(Opsional) Kirim dummy string ke Splunk HEC**

```bash
curl -k https://<Splunk-HEC-Host>:8088/services/collector/event \
  -H "Authorization: Splunk <Splunk-Hec-Token>" \
  -d '{"event": "Value to send"}'
```

Example: 
```bash
curl -k https://10.20.30.40:8088/services/collector/event \
-H "Authorization: Splunk 35976b97-8616-4e0b-a019-zakezakezakezake" \
-d '{"event": "halo bray zake was here"}'
```

📌 Pastikan:

- Splunk HEC aktif di port 8088
    
- Token sudah di-enable dan sourcetype sesuai
    
- Lebih detail bisa baca dimedium saya disini : https://medium.com/@zxve/splunk-hec-bahasa-indonesia-cf5ca20ec734
---

## 🧠 Catatan

- Semua log bersifat **fiktif** dan disusun secara acak.
    
- Bisa dikembangkan untuk jenis log lainnya.
    
- Tidak ada dependensi eksternal (pure Python built-in).
    

---

## 📬 Kontribusi & Kontak

Ingin menambahkan jenis log lain (DNS, Proxy, dll)? Pull request terbuka!  
Untuk diskusi atau kolaborasi, silakan hubungi via GitHub atau LinkedIn saya.

---

## 👨‍💻 Created by

Zaki Zarkasih – Cyber Security Engineer
