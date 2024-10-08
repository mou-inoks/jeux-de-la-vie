from enum import Enum

class Etat(Enum):
    VIVANT = 1
    MORT = 0

class Cellule:
    def __init__(self, x, y, etat):
        self.x = x
        self.y = y
        self.etat = etat
        self.etat_futur = etat  # Ajout d'un attribut pour l'état futur

    @property
    def etat(self):
        return self._etat
    
    @etat.setter
    def etat(self, valeur):
        self._etat = valeur

    # Méthode pour définir l'état futur
    def definir_etat_futur(self, etat_futur):
        self.etat_futur = etat_futur
    
    def appliquer_etat_futur(self):
        self.etat = self.etat_futur
    
    def basculer_etat(self):
        self.etat = 1 if self.etat == 0 else 0


class Tableau:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.grille = [[0 for _ in range(largeur)] for _ in range(hauteur)] 

    def initialiser(self, cellules_vivantes):
        for x, y in cellules_vivantes:
            self.grille[y][x] = 1 

    def afficher(self):
        for ligne in self.grille:
            print(" ".join(str(cellule) for cellule in ligne))

    def compter_voisins_vivants(self, x, y):
        voisins_vivants = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i == 0 and j == 0) or not (0 <= x + i < self.largeur) or not (0 <= y + j < self.hauteur):
                    continue
                voisins_vivants += self.grille[y + j][x + i]
        return voisins_vivants

    def mettre_a_jour_grille(self):
        nouvelle_grille = [[0 for _ in range(self.largeur)] for _ in range(self.hauteur)]
        for y in range(self.hauteur):
            for x in range(self.largeur):
                voisins_vivants = self.compter_voisins_vivants(x, y)
                if self.grille[y][x] == 1:  # Cellule vivante
                    if voisins_vivants in [2, 3]:
                        nouvelle_grille[y][x] = 1  # Reste vivante
                else:  # Cellule morte
                    if voisins_vivants == 3:
                        nouvelle_grille[y][x] = 1  # Devient vivante
        self.grille = nouvelle_grille

    def reinitialiser_grille(self):
        self.grille = [[0 for _ in range(self.largeur)] for _ in range(self.hauteur)]
