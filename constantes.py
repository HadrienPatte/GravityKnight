#on definie des constantes
window_width = 1200
window_height = 680

repeat_wait = 150 # temps d attente avant de considerer la touche en appui long
repeat_every = 1 # delai entre chaque action ensuite

mode_force = False

if mode_force:
    gravity = 15
    m = 1
    dt = 0.1

    global move_force
    move_force = 60
    jump_force = 500

    f_solide = 1
    f_fluide = 0.1
else:
    gravity = 1
    m = 1
    dt = 1

    move_speed = 1
    jump_speed = 35

    f_solide = 0.14
    f_fluide = 0.14


titre_fenetre = "Gravity Knight"

chemin_niveau1 = "niveaux/1"
chemin_niveau2 = "niveaux/2"
chemin_niveau3 = "niveaux/3"

chemins_niveaux = [chemin_niveau1, chemin_niveau2, chemin_niveau3]

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
chemin_chest = "images/chest.png"

liste_blocs = ["b", "e", "s", "u", "d", "l", "r", "c", "p"]


if __name__ == "__main__":
    from main import *
