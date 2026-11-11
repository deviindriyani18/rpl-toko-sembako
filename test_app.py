import unittest
from app import app

class TokoSembakoTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_halaman_utama(self):
        """Memastikan halaman utama merespons dengan status 200 (OK)"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_kalkulasi_tanpa_diskon(self):
        """Uji pembelian di bawah 50rb (tanpa diskon)"""
        response = self.app.post('/', data=dict(
            nama="Budi",
            barang="Gula Pasir 1Kg",
            jumlah=2 # 2 x 14.000 = 28.000
        ))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"28000", response.data)

    def test_kalkulasi_dengan_diskon(self):
        """Uji pembelian di atas 50rb (dapat diskon 10%)"""
        response = self.app.post('/', data=dict(
            nama="Siti",
            barang="Minyak Goreng 1L",
            jumlah=4 # 4 x 15.000 = 60.000 - diskon 6.000 = 54.000
        ))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"54000", response.data)

if __name__ == '__main__':
    unittest.main()