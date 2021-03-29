import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa(self):
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_lataa_saldo(self):
        self.maksukortti.lataa_rahaa(1000)
        self.assertEqual(str(self.maksukortti), "saldo: 20.0")

    def test_vahenna_rahaa(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(str(self.maksukortti), "saldo: 5.0")

    def test_vahenna_liikaa_saldo(self):
        self.maksukortti.ota_rahaa(999999)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_vahenna_liikaa_false(self):
        result = self.maksukortti.ota_rahaa(999999)
        self.assertEqual(result, False)

    def test_vahenna_rahaa_true(self):
        result = self.maksukortti.ota_rahaa(100)
        self.assertEqual(result, True)