import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.virheellinenvarasto = Varasto(tilavuus=-1, alku_saldo=-1)
        self.ylitäysivarasto = Varasto(tilavuus=1, alku_saldo=2)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)


    def test_merkkijonoksi_metodi(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")

    def test_uudella_virheellisella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.virheellinenvarasto.tilavuus, 0)

    def test_uudella_virheellisella_varastolla_oikea_saldo(self):
        self.assertAlmostEqual(self.virheellinenvarasto.saldo, 0)

    def test_uudella_ylitaydella_varastolla_oikea_saldo(self):
        self.assertAlmostEqual(self.ylitäysivarasto.saldo, self.ylitäysivarasto.tilavuus)

    def test_lisaa_negatiivinen_sujaus(self):
        saldo = self.varasto.saldo
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, saldo)

    def test_lisaa_liikaa_saldoa(self):
        self.varasto.lisaa_varastoon(self.varasto.tilavuus + 1)
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_ota_negatiivinen_sujaus(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(-1), 0)

    def test_ota_kaikki(self):
        saldo = self.ylitäysivarasto.saldo
        saatu = self.ylitäysivarasto.ota_varastosta(saldo + 1)
        self.assertAlmostEqual(saatu, saldo)

