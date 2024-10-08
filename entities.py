from enum import Enum

class Etat(Enum):
    VIVANT = 1
    MORT = 0

class Cellule: 
    def __init__(self, x, y, etat):
        self.x = x
        self.y = y
        self.etat = etat
        
    #methodes 
    def getEtat(self):
        return self.etat
    
    def setEtat(self, etat):
        self.etat = etat

class Tableau:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.grille = [[0 for _ in range(largeur)] for _ in range(hauteur)]  # 0 pour morte, 1 pour vivante

    def initialiser(self, cellules_initiales):
        for x, y in cellules_initiales:
            self.grille[y][x] = 1  # 1 représente une cellule vivante

    def afficher(self):
        for ligne in self.grille:
            print(" ".join(str(cellule) for cellule in ligne))

    def compter_voisins(self, x, y):
        voisins = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i == 0 and j == 0) or not (0 <= x + i < self.largeur) or not (0 <= y + j < self.hauteur):
                    continue
                voisins += self.grille[y + j][x + i]
        return voisins

    def mise_a_jour(self):
        nouvelle_grille = [[0 for _ in range(self.largeur)] for _ in range(self.hauteur)]
        for y in range(self.hauteur):
            for x in range(self.largeur):
                voisins = self.compter_voisins(x, y)
                if self.grille[y][x] == 1:  # Cellule vivante
                    if voisins in [2, 3]:
                        nouvelle_grille[y][x] = 1  # Reste vivante
                else:  # Cellule morte
                    if voisins == 3:
                        nouvelle_grille[y][x] = 1  # Devient vivante
        self.grille = nouvelle_grille

    def reinitialiser(self):
        self.grille = [[0 for _ in range(self.largeur)] for _ in range(self.hauteur)]