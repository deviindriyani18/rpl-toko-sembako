# PRD Aplikasi Toko Sembako "Berkah Sampit"

## 1. Ringkasan dan tujuan
Aplikasi web lokal untuk Toko Sembako "Berkah Sampit" guna mencatat stok barang, menghitung transaksi penjualan dengan diskon otomatis, dan menampilkan laporan agar selisih stok berkurang dan pengelolaan keuangan lebih transparan.

## 2. Pengguna dan peran
- **Kasir:** Berinteraksi langsung untuk mencatat transaksi penjualan.
- **Pemilik:** Melihat laporan, mengelola stok, dan mengubah harga.

## 3. Fitur per Prioritas (Target Sprint 1-2)
### F-01 Perhitungan Transaksi & Diskon (Must, Sprint 1)
Kriteria penerimaan:
Given jumlah beli minyak goreng 1L adalah 4, When kasir menekan tombol hitung, Then subtotal Rp 60.000, diskon Rp 6.000 (10%), dan total Rp 54.000 ditampilkan.

### F-02 Integrasi Basis Data Produk (Must, Sprint 2)
Kriteria penerimaan:
Given aplikasi berjalan, When pengguna membuka halaman utama, Then daftar produk (seperti minyak goreng, gula) diambil langsung dari basis data SQLite dan ditampilkan dalam dropdown.

## 4. Data awal (Entitas)
- **Produk:** id (Integer, primary key), nama_barang (String), harga (Integer)

## 5. Di luar lingkup
- Aplikasi ponsel (Mobile App)
- Cetak nota fisik
- Pembayaran digital
- Manajemen multi-pengguna dengan hak akses (login)

## 6. Pertanyaan terbuka
- Bagaimana mekanisme validasi data pembelian di browser (frontend) sebelum dikirim?
- Apakah data awal produk perlu dimasukkan secara otomatis saat basis data dibuat?