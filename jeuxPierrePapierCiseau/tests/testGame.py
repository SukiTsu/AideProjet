import unittest
import sys
sys.path.append("..")
from src.joueur import Joueur
from src.enumChoix import Choix
from src.partie import Partie
from src.game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game("User")

    def test_initialisation(self):
        self.assertEqual(self.game.j1.nom, "User")
        self.assertEqual(self.game.j2.nom, "Bot")
        self.assertEqual(self.game.historic, [])

    def test_setChoixUser(self):
        self.game.setChoixUser(Choix.PIERRE.value)
        self.assertEqual(self.game.j1.getChoix(), Choix.PIERRE.value)

    def test_setChoixBot(self):
        choix_bot = self.game.setChoixBot()
        self.assertEqual(choix_bot, Choix.FEUILLE.value)
        self.assertEqual(self.game.j2.getChoix(), Choix.FEUILLE.value)

    def test_newGame(self):
        self.game.setChoixUser(Choix.PIERRE.value)
        self.game.setChoixBot()
        resultat_duel = self.game.newGame()
        self.assertIn(resultat_duel, [self.game.j1, self.game.j2, None])
        self.assertEqual(len(self.game.historic), 1)

    def test_getHistory(self):
        self.game.setChoixUser(Choix.PIERRE.value)
        self.game.setChoixBot()
        self.game.newGame()
        self.assertEqual(len(self.game.historic), 1)
        history_output = self.game.getHistory()
        self.assertIsNone(history_output)

if __name__ == "__main__":
    unittest.main()
