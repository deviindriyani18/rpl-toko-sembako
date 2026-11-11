from datetime import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

def salam_waktu(jam):
    """Mengembalikan salam sesuai jam (0-23)."""
    if 4 <= jam < 11:
        return "Selamat pagi"
    elif 11 <= jam < 15:
        return "Selamat siang"
    elif 15 <= jam < 18:
        return "Selamat sore"
    else:
        return "Selamat malam"

@app.route("/", methods=["GET", "POST"])
def beranda():
    hasil = None
    sekarang = datetime.now()
    
    if request.method == "POST":
        nama = request.form.get("nama", "").strip()
        barang = request.form.get("barang", "")
        try:
            jumlah = int(request.form.get("jumlah", 0))
        except ValueError:
            jumlah = 0
            
        harga_satuan = 15000 if barang == "Minyak Goreng 1L" else 14000
        total_harga = jumlah * harga_satuan
        
        hasil = {
            "nama": nama,
            "barang": barang,
            "jumlah": jumlah,
            "total": total_harga
        }

    return render_template(
        "index.html",
        hasil=hasil,
        waktu=sekarang.strftime("%d-%m-%Y %H:%M:%S"),
        salam=salam_waktu(sekarang.hour)
    )

if __name__ == "__main__":
    app.run(debug=True)