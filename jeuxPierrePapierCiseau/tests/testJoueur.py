import unittest
import sys
sys.path.append("..")
from src.joueur import Joueur
from src.enumChoix import Choix

class TestPartie(unittest.TestCase):
    def setUp(self):
        self.joueur = Joueur("Nom")

    def test_init(self):
        self.assertEqual(self.joueur.nom, "Nom")
        self.assertIsNone(self.joueur.choix)

    def test_setChoix(self):
        self.joueur.setChoix(Choix.CISEAUX)
        self.assertEqual(self.joueur.choix, Choix.CISEAUX)

    def test_toPrint(self):
        self.assertEqual(self.joueur.toPrint(), "Nom")


if __name__ == '__main__':
    unittest.main()