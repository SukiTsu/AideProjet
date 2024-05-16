import unittest
import sys
sys.path.append("..")
from src.joueur import Joueur
from src.enumChoix import Choix
from src.partie import Partie

class TestPartie(unittest.TestCase):
    def setUp(self):
        self.joueur1 = Joueur("Nom")
        self.joueur2 = Joueur("Bot")
        self.partie = Partie(1, self.joueur1, self.joueur2)

    def test_init(self):
        self.assertEqual(self.partie.num, 1)
        self.assertEqual(self.partie.j1, self.joueur1)
        self.assertEqual(self.partie.j2, self.joueur2)
        self.assertIsNone(self.partie.gagnant)
        self.assertIsNone(self.partie.perdant)

    def test_duel_equal_choices(self):
        self.partie.duel(Choix.PIERRE, Choix.PIERRE)
        self.assertIsNone(self.partie.gagnant)
        self.assertIsNone(self.partie.perdant)

    def test_duel_player1_wins(self):
        self.partie.duel(Choix.PIERRE, Choix.CISEAUX)
        self.assertEqual(self.partie.gagnant, self.joueur1)
        self.assertEqual(self.partie.perdant, self.joueur2)

    def test_duel_player2_wins(self):
        self.partie.duel(Choix.FEUILLE, Choix.CISEAUX)
        self.assertEqual(self.partie.gagnant, self.joueur2)
        self.assertEqual(self.partie.perdant, self.joueur1)

    def test_isSelect(self):
        self.partie.j1.setChoix(Choix.PIERRE)
        self.assertTrue(self.partie.isSelect(Choix.PIERRE))
        self.assertFalse(self.partie.isSelect(Choix.FEUILLE))

    def test_getGagnant(self):
        self.partie.j1.setChoix(Choix.PIERRE)
        self.partie.j2.setChoix(Choix.CISEAUX)
        self.assertEqual(self.partie.getGagnant(), Choix.PIERRE)
        self.partie.j2.setChoix(Choix.FEUILLE)
        self.assertEqual(self.partie.getGagnant(), Choix.FEUILLE)
        self.partie.j1.setChoix(Choix.CISEAUX)
        self.assertEqual(self.partie.getGagnant(),Choix.CISEAUX)

    def test_getChoixUser(self):
        self.partie.j1.setChoix(Choix.PIERRE)
        self.assertEqual(self.partie.getChoixUser(), Choix.PIERRE)

    def test_toPrint(self):
        expected_output = ("Partie n°", 1, "entre", "Nom", "et", "Bot", "Egalité", Choix.PIERRE)
        self.assertEqual(self.partie.toPrint(), expected_output)

if __name__ == '__main__':
    unittest.main()
