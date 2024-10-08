# entities.py
from enum import Enum
import pygame

class Etat(Enum):
    VIVANT = 1
    MORT = 0

class Cellule:
    def __init__(self, x, y, etat):
        self.x = x
        self.y = y
        self.etat = etat
        self.etat_futur = etat 

    @property
    def etat(self):
        return self._etat
    
    @etat.setter
    def etat(self, valeur):
        self._etat = valeur

    def definir_etat_futur(self, etat_futur):
        self.etat_futur = etat_futur
    
    def appliquer_etat_futur(self):
        self.etat = self.etat_futur
    
class Tableau:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.grille = [[Cellule(x, y, Etat.MORT) for x in range(largeur)] for y in range(hauteur)]

    def initialiser(self, cellules_vivantes):
        for x, y in cellules_vivantes:
            self.grille[y][x].etat = Etat.VIVANT 

    def afficher_grille(self, screen, taille_cellule):
        screen.fill((255, 255, 255))
        for y in range(self.hauteur):
            for x in range(self.largeur):
                cellule = self.grille[y][x]
                couleur = (255, 255, 255) if cellule.etat == Etat.MORT else (0, 0, 0)
                pygame.draw.rect(screen, couleur, (x * taille_cellule, y * taille_cellule, taille_cellule, taille_cellule))
        pygame.display.flip()

    def compter_voisins_vivants(self, x, y):
        voisins_vivants = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i == 0 and j == 0) or not (0 <= x + i < self.largeur) or not (0 <= y + j < self.hauteur):
                    continue
                if self.grille[y + j][x + i].etat == Etat.VIVANT:
                    voisins_vivants += 1
        return voisins_vivants

    def mettre_a_jour_grille(self):
        for y in range(self.hauteur):
            for x in range(self.largeur):
                voisins_vivants = self.compter_voisins_vivants(x, y)
                if self.grille[y][x].etat == Etat.VIVANT:  # Cellule vivante
                    if voisins_vivants not in [2, 3]:
                        self.grille[y][x].definir_etat_futur(Etat.MORT)  # Meurt
                else:  # Cellule morte
                    if voisins_vivants == 3:
                        self.grille[y][x].definir_etat_futur(Etat.VIVANT)  # Devient vivante

        # Appliquer les états futurs
        for y in range(self.hauteur):
            for x in range(self.largeur):
                self.grille[y][x].appliquer_etat_futur()

    def reinitialiser_grille(self):
        self.grille = [[Cellule(x, y, Etat.MORT) for x in range(self.largeur)] for y in range(self.hauteur)]
