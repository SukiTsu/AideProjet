import random

from joueur import Joueur
from partie import Partie
from enumChoix import Choix
import tkinter

class Game:
    def __init__(self,name_user):
        """
        Mise en place du jeu
        :param name_user: string: nom choisi par l'utilisateur pour créer un joueur
        arg:
            j1: Joueur : joueur représentant l'utilisateur
            j2: Joueur : joueur représentant le bot
            historic: list(Partie): stock les parties jouées entre les joueurs
        """
        print("Lancement du jeux")
        self.historic = []
        joueur_1 = Joueur(name_user)
        joueur_2 = Joueur("Bot")
        self.j1 = joueur_1
        self.j2 = joueur_2
        #print("Affrontement entre", joueur_1.toPrint(),"et",joueur_2.toPrint())

    def setChoixBot(self):
        """
        Associ un choix à l'utilisateur 2
        Si il y a qu'une partie qui a été jouer, alors l'utilisateur reprend le choix de l'utilisateur 1
        :return:
        """
        if (len(self.historic)==1):
            choix2 = self.historic[0].getChoixUser()
            print("test")
            print(self.historic[0].toPrint())
            print("choix bot:"+choix2)
        else:
            #choix2 = random.choice(list(Choix)).value
            choix2 = Choix.FEUILLE.value
        self.j2.setChoix(choix2)
        return choix2

    def newGame(self):
        """
        Lancement d'une nouvelle manche
        Lance le duel entre le choix de l'utilisateur et celle du Bot
        :return: string: résultat de la manche
        """
        partie = Partie(len(self.historic)+1, self.j1.nom, self.j2.nom)
        resultat_duel = partie.duel(self.j1.getChoix(),self.j2.getChoix())
        self.historic.append(partie)
        return resultat_duel

    def getHistory(self):
        """
        Affiche les résultats des parties jouées
        :return:
        """
        for history in self.historic:
            history.toPrint()

    def setChoixUser(self,choix):
        """
        Modifie le choix de l'utilisateur
        :param choix: string: nouveau choix à attribuer
        :return:
        """
        self.j1.setChoix(choix)