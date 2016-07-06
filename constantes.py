################################################################################
###                                                                          ###
###                      fichier de definition des constantes                ###
###                                                                          ###
################################################################################


### Constantes liees a pygame

# Temps d attente avant de considerer la touche en appui long
repeat_wait = 150
# Delai entre chaque action ensuite
repeat_every = 1



### Constantes liees a la fenetre de jeu

window_width = 1200
window_height = 680

titre_fenetre = "Gravity Knight"

chemin_icone = "images/icone.png"



### Constantes liees au menu

# Image du fond
chemin_menu = "images/menu.png"
chemin_win = "images/win.png"

# Images des boutons
chemin_vitesse =  "images/vitesse.png"
chemin_vitesse1 = "images/vitesse1.png"
chemin_force = "images/force.png"
chemin_force1 = "images/force1.png"
chemin_vies = "images/vies.png"
chemin_vies1 = "images/vies1.png"



### Constantes liees au mode vitesse

mode_vitesse_gravity = 1
mode_vitesse_m = 1
mode_vitesse_dt = 1

mode_vitesse_move_speed = 1
mode_vitesse_jump_speed = 35

mode_vitesse_f_solide = 0.14
mode_vitesse_f_fluide = 0.14



### Constantes liees au mode force

mode_force_gravity = 35
mode_force_m = 1
mode_force_dt = 0.1


mode_force_move_force = 60
mode_force_jump_force = 900

mode_force_f_solide = 2
mode_force_f_fluide = 0.1



### Chemins des fichiers des niveaux

chemin_niveau1 = "niveaux/1"
chemin_niveau2 = "niveaux/2"
chemin_niveau3 = "niveaux/3"
chemin_niveau4 = "niveaux/4"
chemin_niveau5 = "niveaux/5"
chemin_niveau6 = "niveaux/6"
chemin_niveau7 = "niveaux/7"
chemin_niveau8 = "niveaux/8"
chemin_niveau9 = "niveaux/9"

chemins_niveaux = [chemin_niveau1, chemin_niveau2, chemin_niveau3, chemin_niveau4, chemin_niveau5, chemin_niveau6, chemin_niveau7, chemin_niveau8, chemin_niveau9]



### Chemins des images des niveaux

# Image de fond du niveau
chemin_background = "images/background.png"
chemin_game_over = "images/game_over.png"

# Images du personnage
chemin_perso0 = "images/perso0.png"
chemin_perso1 = "images/perso1.png"
chemin_perso2 = "images/perso2.png"

# Images des differents blocs
chemin_fleche = "images/fleche.png"
chemin_entree = "images/entree.png"
chemin_sortie = "images/sortie.png"
chemin_sortie_ouverte = "images/sortie_ouverte.png"
chemin_bloc = "images/bloc.png"
chemin_bloc1 = "images/bloc1.png"
chemin_pics = "images/pics.png"
chemin_key = "images/key.png"

liste_blocs = ["b", "e", "s", "u", "d", "l", "r", "k", "p"]







### a trier



chemin_coeur = "images/coeur.png"
pos_coeur1 = (1000, 0)
pos_coeur2 = (1050, 0)
pos_coeur3 = (1100, 0)

#taille_bouton = bouton_mode_vies.get_rect().size
taille_bouton = (400, 250)

  #Positions du bouton du mode vie
bouton1_haut = 250
bouton1_bas = bouton1_haut + taille_bouton[1]

bouton1_gauche = 0
bouton1_droite = bouton1_gauche + taille_bouton[0]
bouton1_pos = (bouton1_gauche, bouton1_haut)

    #du mode vitesse
bouton2_haut = 250
bouton2_bas = bouton2_haut + taille_bouton[1]

bouton2_gauche = taille_bouton[0] + 1
bouton2_droite = bouton2_gauche + taille_bouton[0]
bouton2_pos = (bouton2_gauche, bouton2_haut)

    #du mode force
bouton3_haut = 250
bouton3_bas = bouton3_haut + taille_bouton[1]

bouton3_gauche =  2 *taille_bouton[0] + 2
bouton3_droite = bouton3_gauche + taille_bouton[0]
bouton3_pos = (bouton3_gauche, bouton3_haut)
"""
class Bouton:
    "classe des boutons du menu"

    def __init__(self, indice, chemin_img0, chemin_img1):
        self.img0 = pygame.image.load(chemin_img0).convert_alpha()
        self.img1 = pygame.image.load(chemin_img1).convert_alpha()
        self.width, self.height = self.img0.get_rect().size
        self.x =
        self.y = (window_height - self.height) / 2

"""

if __name__ == "__main__":
    from main import *
