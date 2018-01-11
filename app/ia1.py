from random import randint
from random import choice
from os import system
from time import sleep

class Main:
    def __init__(self, joueur):
        self.cartes = [
            Carte(joueur, randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)),
            Carte(joueur, randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)),
            Carte(joueur, randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)),
            Carte(joueur, randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)),
            Carte(joueur, randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
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

    def humanPlay(self,grille):
        print(joueur.main)
        redo = True

        while redo:
            try:
                redo=False
                pos_carte = int(input("Vous choisissez quelle carte ? "))
            except:
                print("Cette carte n'est pas disponible")
                redo = True

            try:
                redo=False
                position = int(input("Où voulez vous poser votre carte ? "))
                if grille[position] != None:
                    raise Exception("Occupé")
            except:
                print("Cette position n'est pas disponible")
                redo = True

            if not redo:
                carte = joueur.main[pos_carte]
                print(carte)
                grille.poser(carte, position)
                joueur.main.remove(carte)

class IA:
    def __init__(self, nom):
        self.nom = nom
        self.main = Main(self)
        self.score = 5

    def __str__(self):
        return str(self.nom)

    def iaLvl1(self,grille):
        redo=True
        while redo:
            try:
                redo=False
                position = randint(0,8)
                if grille[position] != None:
                    raise Exception("Occupé")
            except:
                redo = True

            if not redo:
                carte = j2.main[0]
                print(carte)
                grille.poser(carte, position)
                joueur.main.remove(carte)


class Carte:
    id = 1
    def __init__(self, joueur, gauche, haut, bas, droite):
        self.id = Carte.id
        Carte.id += 1

        self.joueur = joueur
        self.haut = haut
        self.droite = droite
        self.bas = bas
        self.gauche = gauche

    def __str__(self):
        return "({joueur})← {gauche} ↑ {haut} ↓ {bas} → {droite}".format(
            haut = self.haut,
            droite = self.droite,
            bas = self.bas,
            gauche = self.gauche,
            joueur = self.joueur
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
            if position == "haut":
                return self.haut > other.bas
            elif position == "bas":
                return self.bas > other.haut
            elif position == "gauche":
                return self.gauche > other.droite
            elif position == "droite":
                return self.droite > other.gauche

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
        en haut -> -3
        en bas -> +3
        a gauche -> -1
        a droite -> +1
        """


        voisins = {}
        voisins["haut"] = self[index-3] if index-3 >= 0 else None
        voisins["bas"] = self[index+3] if index+3 < 9 else None
        voisins["gauche"] = self[index-1] if index-1 >= 0 else None
        voisins["droite"] = self[index+1] if index+1 < 9 else None

        # La c'est un dictionnaire donc la référence marche
        if carte.bataille(voisins["haut"], "haut") and voisins["haut"]:
            voisins["haut"].joueur = carte.joueur
            if joueur1:
                j1.score+=1
                j2.score-=1
            else:
                j1.score-=1
                j2.score-=1
        if carte.bataille(voisins["bas"], "bas") and voisins["bas"]:
            if joueur1:
                j1.score+=1
                j2.score-=1
            else:
                j1.score-=1
                j2.score-=1

            voisins["bas"].joueur = carte.joueur
        if carte.bataille(voisins["gauche"], "gauche") and voisins["gauche"]:
            if joueur1:
                j1.score+=1
                j2.score-=1
            else:
                j1.score-=1
                j2.score-=1

            voisins["gauche"].joueur = carte.joueur
        if carte.bataille(voisins["droite"], "droite") and voisins["droite"]:
            if joueur1:
                j1.score+=1
                j2.score-=1
            else:
                j1.score-=1
                j2.score-=1

            voisins["droite"].joueur = carte.joueur

        self[index] = carte



if __name__ == "__main__":
    grille = Grille()
    j1 = Joueur(1)
    j2 = IA(2)
    joueur1 = choice([True,False])
    nb_tours = 1

    while nb_tours <= 9:
        system("clear")
        print(grille)

        joueur = j1 if joueur1 else j2
        print("C'est au tour du joueur %s" % joueur)
        if joueur1:
            j1.humanPlay(grille)

        else:
            j2.iaLvl1(grille)

        joueur1 = not joueur1
        nb_tours +=1
    # fin du jeu

    nb_points_j1 = len(list(filter(lambda carte: carte.joueur.nom == 1, grille.cartes)))
    nb_points_j2 = 9 - nb_points_j1

    gagnant = 1 if nb_points_j1 > nb_points_j2 else 2
    system("clear")
    print(grille)

    if gagnant==1:
        print("Vous avez gagné ! Félicitations !")
    else:
        print("Vous avez perdu ! :( Vous ferez mieux la prochaine fois")
