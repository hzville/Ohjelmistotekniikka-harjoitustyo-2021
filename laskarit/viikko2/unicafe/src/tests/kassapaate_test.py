import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(10000)

    def test_luotu_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_saldo_alussa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullisesti_maksu_kateisella_liian_vahan(self):

        palautus= self.kassapaate.syo_edullisesti_kateisella(239)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(palautus, 239)


    def test_edullisesti_maksu_kateisella_riittava(self):

        palautus = self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(palautus, 0)

        palautus = self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100480)
        self.assertEqual(self.kassapaate.edulliset, 2)
        self.assertEqual(palautus, 10)

    def test_maukkaasti_maksu_kateisella_liian_vahan(self):

        palautus = self.kassapaate.syo_maukkaasti_kateisella(399)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(palautus, 399)

    def test_maukkaasti_maksu_kateisella_riittava(self):
        palautus = self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(palautus, 0)

        palautus = self.kassapaate.syo_maukkaasti_kateisella(450)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100800)
        self.assertEqual(self.kassapaate.maukkaat, 2)
        self.assertEqual(palautus, 50)

    def test_edullisesti_maksu_kortilla_epaonnistuu(self):

        self.maksukortti = Maksukortti(2)
        palautus = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(palautus, False)
        self.assertEqual(self.maksukortti.saldo, 2)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edulliset_maksu_kortilla_onnistuu(self):

        palautus = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(palautus, True)
        self.assertEqual(self.maksukortti.saldo, 9760)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukkaat_maksu_kortilla_epaonnistuu(self):

        self.maksukortti = Maksukortti(2)
        palautus = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(palautus, False)
        self.assertEqual(self.maksukortti.saldo, 2)
        self.assertEqual(self.kassapaate.maukkaat,0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukkaat_maksu_kortilla_onnistuu(self):

        palautus = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(palautus, True)
        self.assertEqual(self.maksukortti.saldo, 9600)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)


    def test_lataa_rahaa_kortille(self):

        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -5000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.maksukortti.saldo, 10000)

        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 5000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 105000)
        self.assertEqual(self.maksukortti.saldo, 15000)

