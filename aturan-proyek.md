# Aturan Proyek untuk Asisten AI

## Stack
Python 3.12+ (disarankan 3.12 atau 3.13), Flask, SQLite (SQLAlchemy)
Pustaka tambahan: Flask-SQLAlchemy
Gunakan pip untuk manajemen paket, dan selalu perbarui `requirements.txt`.

## Struktur folder
app.py, templates/, static/, tests/, docs/

## Konvensi
Bahasa: Komentar kode dan pesan antarmuka (UI) harus menggunakan Bahasa Indonesia yang baik dan benar.
Commit: Satu fitur atau satu perbaikan per commit. Pesan commit deskriptif (misal: "Tambah fitur login kasir").
Fungsi/Variabel: Gunakan nama yang deskriptif dan konsisten dalam Bahasa Inggris atau Indonesia (sepakati dalam tim).

## Larangan
Jangan menambah paket/pustaka tanpa izin kelompok.
Jangan pernah menyimpan rahasia (kata sandi, token, kunci akses) langsung di kode.
Ubah hanya berkas yang diminta; jangan menghapus atau melemahkan uji tanpa izin.

## Menjalankan dan menguji
python app.py
python -m unittest test_app.py