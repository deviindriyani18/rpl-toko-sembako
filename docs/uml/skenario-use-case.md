# Dokumentasi Skenario Use Case Aplikasi Toko Sembako

Dokumen ini mendefinisikan alur utama, alur alternatif, dan pengecualian untuk use case prioritas (Must Have) berdasarkan PRD dan Use Case Diagram.

---

## (UC-01) Pencatatan Transaksi Penjualan

| Bagian | Isi |
|---|---|
| **Aktor Utama** | Kasir, Pemilik |
| **Kebutuhan Terkait (SRS)** | KF-03, KF-04, KF-05 (MoSCoW: Must) |
| **Kriteria Penerimaan (PRD)** | F-01 (Perhitungan Transaksi & Diskon) |
| **Prasyarat** | Aplikasi web terbuka di halaman utama/kasir. Basis data produk tersedia. |
| **Alur Utama** | 1. Aktor membuka halaman kasir.<br>2. Sistem menampilkan daftar produk dan kuantitas stoknya.<br>3. Aktor memilih produk, mengisi jumlah beli, dan menambahkannya ke keranjang.<br>4. Sistem menghitung subtotal transaksi.<br>5. Sistem memeriksa apakah subtotal mencapai Rp 50.000.<br>6. Jika ya, Sistem menghitung dan menampilkan diskon 10% (sesuai F-01).<br>7. Sistem menghitung dan menampilkan total bayar setelah diskon.<br>8. Aktor menekan tombol 'Hitung Belanjaan' (Given-When-Then F-01).<br>9. Sistem menampilkan ringkasan transaksi akhir. |
| **Alur Alternatif** | 2a. Jika data produk kosong: Sistem menampilkan pesan "Daftar produk tidak tersedia" (Langkah 3-9 tidak bisa dilanjutkan). |
| **Pengecualian (Error)** | 3a. Jika jumlah beli melebihi jumlah stok: Sistem menampilkan pesan kesalahan "Stok produk X tidak mencukupi" dan mencegah penambahan ke keranjang (KF-02). |
| **Pascakondisi** | Transaksi berhasil dihitung dan ditampilkan di layar. (Catatan: Pada tahap ini transaksi tidak otomatis mengurangi stok). |

---

## (UC-02) Integrasi Data Produk & Stok

| Bagian | Isi |
|---|---|
| **Aktor Utama** | Sistem (Use Case internal/background) |
| **Kebutuhan Terkait (SRS)** | KF-02 (MoSCoW: Must) |
| **Kriteria Penerimaan (PRD)** | F-02 (Integrasi Basis Data Produk & Stok) |
| **Prasyarat** | Basis data SQLite `sembako.db` sudah dibuat dengan entitas Produk terisi. |
| **Alur Utama** | 1. Pengguna (Kasir/Pemilik) membuka halaman utama.<br>2. Sistem (F-02) secara otomatis melakukan koneksi ke basis data SQLite.<br>3. Sistem mengambil data (ID, nama, harga, jumlah_stok) dari tabel Produk.<br>4. Sistem mengisi (populate) daftar produk dalam dropdown transaksi.<br>5. Sistem menampilkan halaman utama yang siap digunakan. |
| **Alur Alternatif** | - |
| **Pengecualian (Error)** | 2a. Jika basis data tidak ditemukan: Sistem menampilkan pesan kesalahan "Gagal memuat data produk (Database error)".<br>3a. Jika tabel Produk kosong: Sistem menampilkan dropdown kosong dengan pesan "Data produk masih kosong". |
| **Pascakondisi** | Daftar produk dan stok dinamis dari basis data tersedia di antarmuka web. |