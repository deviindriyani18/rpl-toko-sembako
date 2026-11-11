# SRS Ringkas Aplikasi Toko Sembako "Berkah Sampit"

## 1. Pendahuluan
**Tujuan dan ruang lingkup:**
Dokumen ini menetapkan kebutuhan fungsional dan non-fungsional untuk aplikasi web kasir lokal Toko Sembako "Berkah Sampit". Aplikasi ini fokus pada perhitungan transaksi penjualan dan manajemen stok dasar.

## 2. Gambaran umum
**Pengguna dan peran:**
- **Kasir:** Mampu mencatat transaksi.
- **Pemilik:** Mampu melihat laporan dan mengelola data produk.

**Lingkungan operasi:**
Satu laptop lokal, sistem operasi Windows, browser modern, dan tanpa koneksi internet yang stabil (lokal).

**Batasan:**
- Waktu pengembangan hingga Minggu 16.
- Anggaran klien terbatas.
- Kemampuan pengguna terhadap teknologi masih terbatas.

**Asumsi (dengan rencana konfirmasi):**
- Asumsi: Aplikasi berjalan tanpa koneksi internet. (Rencana konfirmasi: Cek kebutuhan sinkronisasi kelak).
- Asumsi: Data produk tidak sering berubah. (Rencana konfirmasi: Tanya pemilik tentang frekuensi perubahan harga).

## 3. Kebutuhan fungsional
| ID | Pernyataan kebutuhan | Sumber | Prioritas | Asumsi? |
|---|---|---|---|---|
| KF-01 | Sistem harus menampilkan sapaan waktu dinamis berdasarkan jam server. | US-01 | Must | Tidak |
| KF-02 | Sistem harus menampilkan data produk (nama, harga) dari basis data SQLite. | US-02 | Must | Tidak |
| KF-03 | Sistem harus menghitung subtotal berdasarkan jumlah beli. | US-03 | Must | Tidak |
| KF-04 | Sistem harus menghitung diskon 10% jika subtotal di atas Rp 50.000. | US-03 | Must | Tidak |
| KF-05 | Sistem harus menghitung total bayar setelah diskon. | US-03 | Must | Tidak |
| KF-06 | Sistem harus menyimpan transaksi penjualan ke dalam basis data. | US-04 | Should | Tidak |
| KF-07 | Sistem harus menyediakan formulir untuk menambah produk baru. | US-05 | Should | Tidak |
| KF-08 | Sistem harus menyediakan formulir untuk mengubah harga produk. | US-06 | Should | Tidak |
| KF-09 | Sistem harus menampilkan laporan penjualan harian. | US-07 | Should | Tidak |
| KF-10 | Sistem harus menyediakan unit testing otomatis untuk logika diskon. | Jobsheet 3 | Must | Tidak |

## 4. Kebutuhan non-fungsional
| ID | Kategori | Pernyataan terukur | Sumber |
|---|---|---|---|
| KNF-01 | Kinerja | Halaman utama harus terbuka dalam waktu ≤ 3 detik pada laptop klien. | Catatan Wawancara 1 |
| KNF-02 | Keandalan | Aplikasi harus dapat beroperasi penuh tanpa koneksi internet. | Catatan Wawancara 1 |
| KNF-03 | Kegunaan | Pengguna baru harus dapat mencatat satu transaksi tanpa bantuan setelah 1 jam pelatihan. | Catatan Wawancara 2 |
| KNF-04 | Keamanan | Data basis data harus dilindungi dengan hash pada kata sandi (jika ada fitur login). | Asumsi |

## 5. Di luar lingkup (Won't have)
- Cetak nota fisik (alasan: keterbatasan anggaran printer).
- Sinkronisasi data ke cloud (alasan: jaringan tidak stabil).
- Pembayaran digital (alasan: fokus pada pencatatan).

## 6. Matriks keterlacakan
| User story | KF / KNF turunan | Uji (diisi Minggu 13) |
|---|---|---|
| US-01 | KF-01 | |
| US-02 | KF-02 | |
| US-03 | KF-03, KF-04, KF-05, KNF-01 | |
| US-04 | KF-06 | |
| US-05 | KF-07 | |
| US-06 | KF-08 | |
| US-07 | KF-09 | |
| Jobsheet 3 | KF-10 | |

## Riwayat konfirmasi klien
- [cite: Tanggal]: Pemilik menyetujui prioritas fitur dan batasan operasional (Langkah 14-15).