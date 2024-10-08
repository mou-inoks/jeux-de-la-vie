import numpy as np 
import matplotlib.pyplot as plt
import pygame

import entities

Cellule = entities.Cellule
Tableau = entities.Tableau
EtatEnum = entities.Etat



largeut_grille = 20
hauteur_grille = 20
taille_cellule = 20

def initialiser_grille(largeut_grille, hauteur_grille):
    cellules_vivantes = [(1, 1), (2, 2), (2, 3), (3, 1), (3, 2)]
    tableau = Tableau(largeut_grille, hauteur_grille)
    tableau.initialiser(cellules_vivantes)
    return tableau

def afficher_grille(tableau, screen, taille_cellule):
    screen.fill((255, 255, 255))
    for y in range(tableau.hauteur):
        for x in range(tableau.largeur):
            cellule = tableau.grille[y][x]
            couleur = (255, 255, 255) if cellule.etat == EtatEnum.MORT else (0, 0, 0)
            pygame.draw.rect(screen, couleur, (x * taille_cellule, y * taille_cellule, taille_cellule, taille_cellule))
    pygame.display.flip()

def mettre_a_jour_grille(tableau):
    for ligne in tableau.grille: 
        for cellule in ligne:
            nb_voisins_vivants = tableau.compter_voisins_vivants(cellule.x, cellule.y)
            if(cellule.etat == EtatEnum.VIVANT):
                if nb_voisins_vivants < 2 or nb_voisins_vivants > 3:
                    cellule.definir_etat_futur(EtatEnum.MORT)
            else:
                if(nb_voisins_vivants == 3):
                    cellule.definir_etat_futur(EtatEnum.VIVANT)


if(__name__ == "__main__"):

    grille = initialiser_grille(largeut_grille, hauteur_grille)

    pygame.init()

    screen = pygame.display.set_mode((largeut_grille * taille_cellule, hauteur_grille * taille_cellule))

    # Boucle principale
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        mettre_a_jour_grille(grille)
        afficher_grille(grille, screen, taille_cellule)
        pygame.time.wait(1000)

    pygame.quit()