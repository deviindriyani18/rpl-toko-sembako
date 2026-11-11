# Product Backlog Aplikasi Toko Sembako "Berkah Sampit"

Manajemen tugas Sprint (dua mingguan) berdasarkan prioritas MoSCoW.

## Pembagian Sprint (Usulan)

| Sprint | ID Kebutuhan | Nama Tugas / Butir Backlog | Prioritas | Alasan/Catatan |
|---|---|---|---|---|
| 1 | KF-01 | Implementasi sapaan waktu dinamis di halaman utama. | Must | Fitur dasar yang sudah ada, tinggal dipastikan berjalan. |
| 1 | KF-03, KF-04, KF-05 | Implementasi logika kalkulasi transaksi (subtotal, diskon 10% di atas 50rb, total bayar). | Must | Inti aplikasi (kasir); menyelesaikan Jobsheet 2. |
| 1 | KF-10 | Finalisasi skrip unit testing untuk logika diskon. | Must | Menjamin kualitas kode inti (Jobsheet 3). |
| 2 | KF-02 | Integrasi SQLite: Tampilkan daftar produk, harga, dan **jumlah stok** langsung dari basis data. | Must | Mengubah data statis menjadi dinamis. |
| 2 | KF-07, KF-08 | Buat formulir untuk menambah dan mengubah harga produk. | Should | Mempermudah manajemen produk (opsional jika waktu kurang). |
| 3 | KF-06 | Implementasi penyimpanan transaksi penjualan ke basis data. | Should | Catatan riwayat (opsional jika waktu kurang). |
| 3 | KF-09 | Buat halaman laporan penjualan harian dasar. | Should | opsional jika waktu kurang. |

## Tugas Kecil untuk Sprint 1

1.  Pastikan fungsi `salam_waktu()` di `app.py` berjalan sesuai jam server lokal.
2.  Perbarui templates/index.html untuk menampilkan diskon dan total bayar yang lebih rapi (menyelesaikan Jobsheet 2).
3.  Jalankan `python -m unittest test_app.py` untuk memastikan tes diskon OK.