class Joueur:
    def __init__(self): # La main c'est un paramètre ou pas ?
        self.score = 5
        self.main = Main()

    def deposer_carte():
    def retourner_carte():
    def incrementer_score():
        self.score += 1

    def decrementer_score():
        self.score -= 1

class JoueurHumain(Joueur):
    def __init__(self, pseudo):
        """
        pseudo: str
        """
        Joueur.__init__(self)
        self.pseudo = pseudo

    def personnaliser_profil()
    def personnaliser_deck()
    def choisir_deck_principal()

class IA(Joueur):
    def __init__():
        Joueur.__init__(self)

class Main:
    def __init__(self, deck):
        # Je prends les 5 premières cartes du deck, parce qu'il est melangé
        self.cartes = deck.cartes[0:5]



class Deck:
    def __init__(self, cartes):
        """
        cartes : tableau de cartes
        """
        self.cartes = cartes
        self.taille = len(cartes)

class Plateau:
    def __init__(self):
        self.cases = []
        for i in range(9):
            self.cases[i] = Case()

class Case:
    def __init__(self):
        self.carte = False

    def poser_carte(self, carte):
        if not self.carte:
            print("Erreur, il y a déjà une carte dessus") # A remplacer par une vraie erreur
        else:
            self.carte = carte
