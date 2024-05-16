from joueur import Joueur
from enumChoix import Choix
class Partie:
    """
    Manche entre deux joueurs
    arg:
        num (int): numéro de la partie
        j1 (Joueur): Joueur n°1
        j2 (Joueur): Joueur n°2
        gagnant (Joueur, None): joueur gagnant de la manche
        perdant (Joueur, None): joueur perdant de la manche
    """
    def __init__(self,numPartie, nomJoueur1, nomJoueur2):
        """
        Crée une nouvelle manche
        Instancies des 'nouveaux' joueur pour ne pas prendre en compte leurs modifications lors des
        prochaines parties
        :param numPartie: string: numéro de la partie (nombre de partie réalisé)
        :param jo1: string: nom du Joueur n°1
        :param jo2: string: nom du Joueur n°2
        """
        self.num = numPartie
        self.j1 = Joueur(nomJoueur1)
        self.j2 = Joueur(nomJoueur2)
        self.gagnant = Joueur
        self.perdant = Joueur

    def duel(self,choix1,choix2):
        """
        Lance le duel entre les deux joueurs
        Si les choix des joueurs sont différents, appel la méthode getGagant pour récupérer le choix gagnant.
        Attribue ensuite la victoire à un joueur et la défaite à l'autre.
        Sinon gagnant et perdant prennent la valeur None
        :param choix1: string: choix de l'utilisateur
        :param choix2: string: choix du Bot
        :return: string: le gagnant de la manche ou Egalité en cas d'égalité
        """
        self.j1.setChoix(choix1)
        self.j2.setChoix(choix2)
        if (choix1==choix2):
            self.gagnant = None
            self.perdant = None
            return "Egalité"

        self.gagnant = self.j2
        self.perdant = self.j1
        if choix1 == self.getGagnant():
            self.gagnant = self.j1
            self.perdant = self.j2
        return self.gagnant.toPrint() + " remporte la manche"

    def isSelect(self,choix):
        """
        Permet de savoir si un choix a été choisi par un utilisateur
        :param choix: string
        :return: boolean: True si la valeur a été choisie par un utilisateur, False sinon
        """
        return self.j1.getChoix() == choix or self.j2.getChoix() == choix

    def getGagnant(self):
        """
        Définition des règles de la manche. Indique quelle valeur l'emporte sur l'autre.
        :return: string: choix gagnant
        """
        if self.isSelect(Choix.PIERRE.value):
            if self.isSelect(Choix.FEUILLE.value):
                return Choix.FEUILLE.value
            return Choix.PIERRE.value
        return Choix.CISEAUX.value

    def getChoixUser(self):
        """
        Récupère le choix de l'utilisateur de l'application
        :return: string
        """
        return self.j1.getChoix()
    def toPrint(self):
        """
        Phrase explicative de la manche
        :return: string
        """
        resum = "Partie n°",self.num,"entre",self.j1.toPrint(), "et",self.j2.toPrint()
        if self.gagnant:
            resum += "-Gagnant:", self.gagnant.toPrint(),"-Choix:",self.gagnant.getChoix(),"contre",self.perdant.getChoix()
        else:
            resum += "Egalité",self.j1.getChoix()
        return resum