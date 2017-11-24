from random import randint

class Carte:
    def __init__(self, haut, droite, bas, gauche):
        self.haut = haut
        self.droite = droite
        self.bas = bas
        self.gauche = gauche

    def __str__(self):
        return "← {gauche} ↑ {haut} ↓ {bas} → {droite}".format(
            haut = self.haut,
            droite = self.droite,
            bas = self.bas,
            gauche = self.gauche
        )

    def bataille(self, other):
        """
        retourne le gagnant d'une bataille
        A invoquer quand une carte est posée
        """
        if self.haut > other.bas or self.droite > other.gauche or self.gauche > other.droite or self.bas > other.haut:
            return self
        else:
            return other

class Grille:
    def __init__(self):
        cartes = []
        for i in range(9):
            cartes.append("."*16)
            self.cartes = cartes

    def __iter__(self):
        for carte in self.cartes:
            yield carte

    def __str__(self):
        return "\n\n".join([
            "{c[0]}\t{c[1]}\t{c[2]}",
            "{c[3]}\t{c[4]}\t{c[5]}",
            "{c[6]}\t{c[7]}\t{c[8]}\n\n\n"
        ]).format(
            c = self.cartes
        )

if __name__ == "__main__":
    grille = Grille()
    print(grille)
    grille.cartes[3] = Carte(1, 2, 10, 4)
    print(grille)
