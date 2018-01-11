from django.shortcuts import render
from random import randint
from random import randrange as r
from os import system
from time import sleep
import sqlite3
from django.db import connection
from django import forms
from django.http import HttpResponse

class Main:
    def __init__(self, joueur):
        self.cartes = [
            Carte(joueur, r(5)),
            Carte(joueur, r(5)),
            Carte(joueur, r(5)),
            Carte(joueur, r(5)),
            Carte(joueur, r(5)),
        ]

    def __str__(self):
        return "\n".join(["{}: {}".format(i, carte) for i, carte in enumerate(self.cartes)])

    def __getitem__(self, index):
        return self.cartes[index]

    def remove(self, carte):
        self.cartes.remove(carte)

class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.main = Main(self)
        self.score = 5

    def __str__(self):
        return str(self.nom)

class Carte:
    def __init__(self, joueur,id):
        self.id = id
        connexion = sqlite3.connect('db.sqlite3')
        cursor = connexion.cursor()
        cursor.execute("SELECT * FROM carte_carte WHERE id = id; ")
        liste = cursor.fetchall()
        self.joueur = joueur
        self.Haut = liste[id][5]
        self.Droite = liste[id][1]
        self.Bas = liste[id][2]
        self.Gauche = liste[id][3]
        print(list)



    def __str__(self):
        return "← {Gauche} ↑ {Haut} ↓ {Bas} → {Droite}".format(
            Haut = self.Haut,
            Droite = self.Droite,
            Bas = self.Bas,
            Gauche = self.Gauche,
        )

    def bataille(self, other, position):
        """
        retourne le gagnant d'une bataille
        A invoquer quand une carte est posée
        position, c'est la position de other
        """
        if other == None: # other est soit pas posée, soit en dehors du terrain
            return self.id
        else:
            if position == "Haut":
                return self.Haut > other.Bas
            elif position == "Bas":
                return self.Bas > other.Haut
            elif position == "Gauche":
                return self.Gauche > other.Droite
            elif position == "Droite":
                return self.Droite > other.Gauche

class Grille:
    def __init__(self):
        cartes = []
        for i in range(9):
            cartes.append(None)
            self.cartes = cartes

    def __iter__(self):
        for carte in self.cartes:
            yield carte

    def __str__(self):
        return "\n\n".join([
            "[0] {c[0]} \t[1] {c[1]} \t[2] {c[2]}",
            "[3] {c[3]} \t[4] {c[4]} \t[5] {c[5]}",
            "[6] {c[6]} \t[7] {c[7]} \t[8] {c[8]}\n\n\n"
        ]).format(
            c = self.cartes
        )


    def __getitem__(self, index):
        return self.cartes[index]

    def __setitem__(self, index, valeur):
        self.cartes[index] = valeur

    def poser(self, carte, index):
        """
        0 1 2
        3 4 5
        6 7 8
        """
        """
        en Haut -> -3
        en Bas -> +3
        a Gauche -> -1
        a Droite -> +1
        """

        voisins = {}
        voisins["Haut"] = self[index-3] if index-3 >= 0 else None
        voisins["Bas"] = self[index+3] if index+3 < 9 else None
        voisins["Gauche"] = self[index-1] if index-1 >= 0 else None
        voisins["Droite"] = self[index+1] if index+1 < 9 else None

        # # La c'est un dictionnaire donc la référence marche
        # if carte.bataille(voisins["Haut"], "Haut") and voisins["Haut"]:
        #     voisins["Haut"].joueur = carte.joueur
        # if carte.bataille(voisins["Bas"], "Bas") and voisins["Bas"]:
        #     voisins["Bas"].joueur = carte.joueur
        # if carte.bataille(voisins["Gauche"], "Gauche") and voisins["Gauche"]:
        #     voisins["Gauche"].joueur = carte.joueur
        # if carte.bataille(voisins["Droite"], "Droite") and voisins["Droite"]:
        #     voisins["Droite"].joueur = carte.joueur

        self[index] = carte




def play(request):

    # if not 'ingame' in request.session:
        # request.session = {
        #     "plateau": ziehfzef,
        #     "joueur": hfezufhzuhf
        # }
    connexion = sqlite3.connect('db.sqlite3')
    cursor = connexion.cursor()
    plateau = Grille()
    joueur =  Joueur(1)
    context={
        "score":joueur.score,
        "cartes":joueur.main.cartes,
        "plateau":plateau,
    }
    request.session['ingame'] = True #A supprimer dans fin de partie


    if request.POST.get('pos'):
        position = int(request.POST.get('pos'))
        numCarte = int(request.POST.get('numCarte'))
        carte = request.session.get('joueur', joueur).main[numCarte]
        plateau.poser(carte,position)

    context={
        "score":request.session.get('joueur', joueur).score,
        "cartes":request.session.get('joueur', joueur ).main.cartes,
        "plateau":request.session.get('plateau', plateau),
    }

    # if 'count' in request.session:
    #     request.session['count'] += 1
    #     return HttpResponse('new count=%s' % request.session['count'])
    # else:
    #     request.session['count'] = 1
    #     return HttpResponse('No count in session. Setting to 1')
    #
    return render(request,"testing.html",context)
