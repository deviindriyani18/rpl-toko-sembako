from datetime import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

def salam_waktu(jam):
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
        subtotal = jumlah * harga_satuan
        
        # Logika Diskon (Fitur Jobsheet 2)
        diskon = 0
        if subtotal > 50000:
            diskon = int(subtotal * 0.10) # Diskon 10%
        
        total_bayar = subtotal - diskon
        
        hasil = {
            "nama": nama,
            "barang": barang,
            "jumlah": jumlah,
            "subtotal": subtotal,
            "diskon": diskon,
            "total": total_bayar
        }

    return render_template(
        "index.html",
        hasil=hasil,
        waktu=sekarang.strftime("%d-%m-%Y %H:%M:%S"),
        salam=salam_waktu(sekarang.hour)
    )

if __name__ == "__main__":
    app.run(debug=True)