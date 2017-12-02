from random import randint
from os import system

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
            "{c[0]} \t{c[1]} \t{c[2]}",
            "{c[3]} \t{c[4]} \t{c[5]}",
            "{c[6]} \t{c[7]} \t{c[8]}\n\n\n"
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
        if carte.bataille(voisins["bas"], "bas") and voisins["bas"]:
            voisins["bas"].joueur = carte.joueur
        if carte.bataille(voisins["gauche"], "gauche") and voisins["gauche"]:
            voisins["gauche"].joueur = carte.joueur
        if carte.bataille(voisins["droite"], "droite") and voisins["droite"]:
            voisins["droite"].joueur = carte.joueur

        self[index] = carte



if __name__ == "__main__":
    grille = Grille()
    joueur1 = True
    nb_tours = 1

    while nb_tours <= 9:
        system("clear")
        print(grille)

        joueur = 1 if joueur1 else 2
        print("C'est au tour du joueur %d" % joueur)
        position = int(input("Où voulez vous poser votre carte ? "))
        points_carte = list(map(int, input("Entrez gauche haut bas droite : ").split(" "))) # Cette ligne est dégueu mais osef

        # l'opérateur * "aplatit" une liste pour la faire tenir dans des arguments c'est grave pratique
        carte = Carte(joueur, *points_carte)
        print(carte)
        grille.poser(carte, position)

        joueur1 = not joueur1

    nb_points_j1 = filter(lambda carte: carte.id == 1, grille.cartes)
    nb_points_j2 = 9 - nb_points_j1

    gagnant = 1 if nb_points_j1 > nb_points_j2 else 2

    print(gagnant)
