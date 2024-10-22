import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Constantes
LARGEUR, HAUTEUR = 800, 600
TAILLE_CELLULE = 70
COLONNES, LIGNES = 8, 7
NOIR = (0, 0, 0)
BLANC = (255, 255, 255)
BLEU = (0, 0, 255)
ROUGE = (255, 0, 0)

# Création de l'écran
ecran = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Puissance Quatre")

# Police
police = pygame.font.Font(None, 36)

# Plateau de jeu
plateau = [[' ' for _ in range(COLONNES)] for _ in range(LIGNES)]

def dessiner_plateau():
    for ligne in range(LIGNES):
        for colonne in range(COLONNES):
            pygame.draw.rect(ecran, BLEU, (colonne * TAILLE_CELLULE, ligne * TAILLE_CELLULE, TAILLE_CELLULE, TAILLE_CELLULE), 2)
            if plateau[ligne][colonne] == 'X':
                pygame.draw.circle(ecran, ROUGE, (colonne * TAILLE_CELLULE + TAILLE_CELLULE // 2, ligne * TAILLE_CELLULE + TAILLE_CELLULE // 2), TAILLE_CELLULE // 2 - 5)
            elif plateau[ligne][colonne] == 'O':
                pygame.draw.circle(ecran, NOIR, (colonne * TAILLE_CELLULE + TAILLE_CELLULE // 2, ligne * TAILLE_CELLULE + TAILLE_CELLULE // 2), TAILLE_CELLULE // 2 - 5)

def placer_jeton(colonne, joueur):
    for ligne in range(LIGNES-1, -1, -1):
        if plateau[ligne][colonne] == ' ':
            plateau[ligne][colonne] = joueur
            return True
    return False

def verifier_victoire(joueur):
    # Vérification horizontale
    for ligne in range(LIGNES):
        for colonne in range(COLONNES - 3):
            if plateau[ligne][colonne] == plateau[ligne][colonne+1] == plateau[ligne][colonne+2] == plateau[ligne][colonne+3] == joueur:
                return True

    # Vérification verticale
    for ligne in range(LIGNES - 3):
        for colonne in range(COLONNES):
            if plateau[ligne][colonne] == plateau[ligne+1][colonne] == plateau[ligne+2][colonne] == plateau[ligne+3][colonne] == joueur:
                return True

    # Vérification diagonale (bas-gauche vers haut-droite)
    for ligne in range(3, LIGNES):
        for colonne in range(COLONNES - 3):
            if plateau[ligne][colonne] == plateau[ligne-1][colonne+1] == plateau[ligne-2][colonne+2] == plateau[ligne-3][colonne+3] == joueur:
                return True

    # Vérification diagonale (haut-gauche vers bas-droite)
    for ligne in range(LIGNES - 3):
        for colonne in range(COLONNES - 3):
            if plateau[ligne][colonne] == plateau[ligne+1][colonne+1] == plateau[ligne+2][colonne+2] == plateau[ligne+3][colonne+3] == joueur:
                return True

    return False

def ecran_demarrage():
    ecran.fill(BLANC)
    titre = police.render("Puissance Quatre", True, NOIR)
    instruction = police.render("Cliquez pour commencer", True, NOIR)
    ecran.blit(titre, (LARGEUR // 2 - titre.get_width() // 2, HAUTEUR // 3))
    ecran.blit(instruction, (LARGEUR // 2 - instruction.get_width() // 2, HAUTEUR // 2))
    pygame.display.flip()

    attente = True
    while attente:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                attente = False

def ecran_victoire(joueur):
    ecran.fill(BLANC)
    couleur_gagnant = ROUGE if joueur == 'X' else NOIR
    nom_couleur = "rouge" if joueur == 'X' else "noir"
    message = police.render(f"Le joueur {nom_couleur} a gagné !", True, couleur_gagnant)
    instruction = police.render("Cliquez pour rejouer", True, NOIR)
    ecran.blit(message, (LARGEUR // 2 - message.get_width() // 2, HAUTEUR // 3))
    ecran.blit(instruction, (LARGEUR // 2 - instruction.get_width() // 2, HAUTEUR // 2))
    pygame.display.flip()

    attente = True
    while attente:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                attente = False

def main():
    joueur_actuel = 'X'

    while True:
        ecran_demarrage()

        # Réinitialisation du plateau
        for ligne in range(LIGNES):
            for colonne in range(COLONNES):
                plateau[ligne][colonne] = ' '

        jeu_en_cours = True
        while jeu_en_cours:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    colonne = event.pos[0] // TAILLE_CELLULE
                    if placer_jeton(colonne, joueur_actuel):
                        if verifier_victoire(joueur_actuel):
                            ecran_victoire(joueur_actuel)
                            jeu_en_cours = False
                        joueur_actuel = 'O' if joueur_actuel == 'X' else 'X'

            ecran.fill(BLANC)
            dessiner_plateau()
            pygame.display.flip()

if __name__ == "__main__":
    main()
