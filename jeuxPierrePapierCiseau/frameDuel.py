from tkinter import *

class FrameDuel(Frame):
    def __init__(self,master=None,**kwargs):
        super().__init__(master,**kwargs)
        self.pack()
        self.label_joueur2 = Label(self,text="")
        self.label_joueur1 = Label(self,text="")
        self.label_resultat = Label(self,text="")

    def setChoix(self,choix1,choix2,resultat_duel):
        self.label_joueur1.config(text="Votre choix: "+choix1)
        self.label_joueur2.config(text="Choix du Bot: "+choix2)
        self.label_resultat.config(text=resultat_duel)
        self.label_joueur2.pack()
        self.label_resultat.pack()
        self.label_resultat.pack_forget()
        self.label_joueur1.pack()

    def setResultatDuel(self):
        self.label_resultat.pack()