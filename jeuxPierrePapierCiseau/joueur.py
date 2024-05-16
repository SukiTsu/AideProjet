class Joueur:
    """
    Instance permettant de participer à des duel
    arg:
        nom (string)
        choix (string)
    """
    def __init__(self, nomJoueur):
        """
        Initialisation d'un nouveau joueur
        :param nomJoueur: string: nom du Joueur
        """
        self.nom = nomJoueur
        self.choix = None

    def setChoix(self,c):
        """
        attribu un choix à l'utilisateur pour pouvoir entrer en duel contre l'autre joueur
        :param c: string: valeur parmis [PIERRE,FEUILLE,CISEAUX]
        :return: None
        """
        self.choix = c

    def getChoix(self):
        """
        Récupère le choix choisi par le joueur
        :return: string
        """
        return self.choix

    def toPrint(self):
        """
        Récupère le nom de l'utilisateur
        :return: string
        """
        return self.nom