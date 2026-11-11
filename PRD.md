# PRD Aplikasi Toko Sembako "Berkah Sampit"

## 1. Ringkasan dan tujuan
Aplikasi web lokal untuk Toko Sembako "Berkah Sampit" guna mencatat stok barang dasar, menghitung transaksi penjualan dengan diskon otomatis 10% untuk belanja di atas Rp 50.000, dan menampilkan laporan agar selisih stok berkurang dan pengelolaan keuangan lebih transparan.

## 2. Pengguna dan peran
- **Kasir:** Berinteraksi langsung untuk mencatat transaksi penjualan.
- **Pemilik:** Melihat laporan, mengelola stok dasar, dan mengubah harga.

## 3. Fitur per Prioritas (Target Sprint 1-2)
### F-01 Perhitungan Transaksi & Diskon (Must, Sprint 1)
Aturan Bisnis: Diskon global 10% berlaku untuk total belanja (subtotal) yang mencapai atau melebihi Rp 50.000.
Kriteria penerimaan:
Given jumlah beli produk X adalah 4 (harga satuan 15.000), When kasir menekan tombol hitung, Then subtotal Rp 60.000, diskon Rp 6.000 (10%), dan total Rp 54.000 ditampilkan.

### F-02 Integrasi Basis Data Produk & Stok (Must, Sprint 2)
Kriteria penerimaan:
Given aplikasi berjalan, When pengguna membuka halaman utama, Then daftar produk beserta kuantitas stoknya diambil langsung dari basis data SQLite dan ditampilkan dalam dropdown. Transaksi yang dihitung tidak otomatis mengurangi stok pada tahap ini (target sprint 3).

## 4. Data awal (Entitas Dasar)
- **Produk:** id (Integer, primary key), nama_barang (String), harga (Integer), jumlah_stok (Integer)

## 5. Di luar lingkup
- Aplikasi ponsel (Mobile App)
- Cetak nota fisik
- Pembayaran digital
- Manajemen multi-pengguna dengan hak akses (login dengan kata sandi). *Pemisahan akses dilakukan hanya dengan URL berbeda tanpa perlindungan kata sandi (misal: /kasir dan /admin).*

## 6. Pertanyaan terbuka
- Bagaimana mekanisme validasi data pembelian di browser (frontend) sebelum dikirim?
- Apakah data awal produk perlu dimasukkan secara otomatis saat basis data dibuat?