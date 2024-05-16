import time
from tkinter import *
from game import Game
from enumChoix import Choix
from frameDuel import FrameDuel
NB_PARTIE = 2
class Interface():
    """
    Permet d'avoir une interface graphique
    Affiche les résultats des manches
    """
    def __init__(self):
        """
        Création de l'interface avec un titre, un input texte et un bouton pour lancer le jeux
        :return:
        """
        app = Tk()
        app.title("Pierre papier ciseau")
        app.minsize(800, 600)
        app.geometry("700x250")

        boite = Frame(app)

        label_titre = Label(app, text="Jeux de pierre papier ciseaux")

        entry_name_user = Entry(boite)
        bouton_commencer = Button(boite, text="Commencer", command=self.lancement_game, font=("Helevia"))

        label_titre.pack(expand=YES)
        entry_name_user.pack()
        bouton_commencer.pack()
        boite.pack()
        self.label_gagnant = None
        self.game = None
        self.inUser = entry_name_user
        self.app = app
        self.app.mainloop()

    def lancement_game(self):
        """
        Action du bouton commencé
        Créer le jeux en instancian l'objet game
        Lance la première partie
        Affiche trois boutons de choix pour l'utilisateur
        :return:
        """
        name_user = "Anonyme"
        if (self.inUser.get()!= ""):
            name_user = self.inUser.get()

        for widget in self.app.winfo_children():
            widget.destroy()
        self.game = Game(name_user)

        frameButton = Frame(self.app)
        frameButton.pack(side="bottom")

        buttonCiseaux = Button(frameButton, text=Choix.PIERRE.value, command=lambda: self.buttonClique(Choix.PIERRE.value))
        buttonPierre = Button(frameButton, text=Choix.CISEAUX.value, command=lambda: self.buttonClique(Choix.CISEAUX.value))
        buttonFeuille = Button(frameButton, text=Choix.FEUILLE.value, command=lambda: self.buttonClique(Choix.FEUILLE.value))

        buttonCiseaux.pack(side="right",padx=10)
        buttonPierre.pack(side="right",padx=10)
        buttonFeuille.pack(side="right",padx=10)
        self.decompte_label= Label(self.app, text="")
        self.label_gagnant = Label(self.app, text="")
        self.decompte_label.pack(expand=YES)
        self.label_gagnant.pack()
        self.frame_bouton = frameButton
        self.fram_duel = FrameDuel(self.app)

    def buttonClique(self, choix):
        """
        Action des boutons choix
        Lance le duel entre les joueurs
        Affiche le résultats de la manche
        :param choix: string: valeur du bouton cliqué
        :return:
        """
        self.game.setChoixUser(choix)
        self.frame_bouton.pack_forget()
        self.decompte_label.pack()
        self.decompteLabel(3)

    def decompteLabel(self, tmps_restant):
        """
        Affiche un label entre les manches expliquant les choix des joueurs et les résultats des duel
        :param tmps_restant:
        :return:
        """
        if tmps_restant > 0:
            """Décompte de x seconde après le choix de l'utilisateur"""
            self.decompte_label.config(text=str(tmps_restant))
            self.app.after(1000,self.decompteLabel, tmps_restant-1)
        elif tmps_restant == 0:
            """Lancement du duel après le décompte"""
            bot_choix = self.game.setChoixBot()
            self.decompte_label.pack_forget()
            resultat_duel = self.game.newGame()
            self.fram_duel.setChoix(self.game.j1.getChoix(), self.game.j2.getChoix(),resultat_duel)
            self.fram_duel.pack()
            self.app.after(1000,self.decompteLabel,tmps_restant-1)
        elif tmps_restant == -1:
            """Affichage du résultat du duel"""
            self.fram_duel.setResultatDuel()
            self.app.after(2000,self.decompteLabel,tmps_restant-1)
        else:
            """Après le duel, vérifi si le nombre de partie joué a bien été respecté"""
            if (len(self.game.historic) >= NB_PARTIE):
                self.fram_duel.pack_forget()
                label_titre = Label(self.app,text="Résultat des parties:")
                label_titre.pack
                for history in self.game.historic:
                    label_history = Label(self.app,text=history.toPrint())
                    label_history.pack()
            else:
                self.nouvellePartie()

    def nouvellePartie(self):
        """
        Affiche les boutons de choix pour permettre le lancement d'un prochain duel
        :return:
        """
        self.fram_duel.pack_forget()
        self.frame_bouton.pack(side="bottom")