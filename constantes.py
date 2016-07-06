#on definie des constantes
window_width = 1200
window_height = 680

repeat_wait = 150 # temps d attente avant de considerer la touche en appui long
repeat_every = 1 # delai entre chaque action ensuite
import pygame

mode_force = False
##if mode_force:
##    gravity = 15
##    m = 1
##    dt = 0.1
##
##    global move_force
##    move_force = 60
##    jump_force = 600
##
##    f_solide = 1
##    f_fluide = 0.1
##else:
##    gravity = 1
##    m = 1
##    dt = 1
##
##    move_speed = 1
##    jump_speed = 35
##
##    f_solide = 0.14
##    f_fluide = 0.14


titre_fenetre = "Gravity Knight"

chemin_niveau1 = "niveaux/1"
chemin_niveau2 = "niveaux/2"
chemin_niveau3 = "niveaux/3"
chemin_niveau4 = "niveaux/4"
chemin_niveau5 = "niveaux/5"
chemin_niveau6 = "niveaux/6"
chemin_niveau7 = "niveaux/7"

chemins_niveaux = [chemin_niveau1, chemin_niveau2, chemin_niveau3, chemin_niveau4, chemin_niveau5, chemin_niveau6, chemin_niveau7]

chemin_icone = "images/icone.png"
chemin_menu = "images/menu.png"
chemin_background = "images/background.png"

chemin_perso0 = "images/perso0.png"
chemin_perso1 = "images/perso1.png"
chemin_perso2 = "images/perso2.png"

chemin_fleche = "images/fleche.png"
chemin_entree = "images/entree.png"
chemin_sortie = "images/sortie.png"
chemin_sortie_ouverte = "images/sortie_ouverte.png"
chemin_bloc = "images/bloc.png"
chemin_bloc1 = "images/bloc1.png"
chemin_pics = "images/pics.png"
chemin_key = "images/key.png"

bouton_mode_vies = "images/mode_vies.png"
bouton_mode_vitesse1 = "images/mode_vitesse1.png"
bouton_mode_vitesse =  "images/mode_vitesse.png"
bouton_mode_forces = "images/mode_force.png"
bouton_mode_vies1 = "images/mode_vies1.png"
bouton_mode_forces1 = "images/mode_forces1.png"

liste_blocs = ["b", "e", "s", "u", "d", "l", "r", "k", "p"]

coeur = "images/coeur1.png"
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

bouton3_gauche =  2 *taille_bouton[0] + 1
bouton3_droite = bouton3_gauche + taille_bouton[0]
bouton3_pos = (bouton3_gauche, bouton3_haut)





if __name__ == "__main__":
    from main import *
