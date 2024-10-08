import pygame
import entities

Cellule = entities.Cellule
Tableau = entities.Tableau
EtatEnum = entities.Etat
largeut_grille = 20
hauteur_grille = 20
taille_cellule = 20

def initialiser_grille(largeut_grille, hauteur_grille, cellules_vivantes):
    tableau = Tableau(largeut_grille, hauteur_grille)
    tableau.initialiser(cellules_vivantes)
    return tableau


if(__name__ == "__main__"):
    cellules_vivantes = [(1, 1), (2, 2), (2, 3), (3, 1), (3, 2)]
    grille = initialiser_grille(largeut_grille, hauteur_grille, cellules_vivantes)

    pygame.init()

    screen = pygame.display.set_mode((largeut_grille * taille_cellule, hauteur_grille * taille_cellule))

    # Boucle principale
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        grille.mettre_a_jour_grille()
        grille.afficher_grille(screen, taille_cellule)
        pygame.time.wait(1000)

    pygame.quit()