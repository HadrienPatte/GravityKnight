#on definie des constantes
window_width = 1200
window_height = 680

repeat_wait = 150 # temps d attente avant de considerer la touche en appui long
repeat_every = 1 # delai entre chaque action ensuite


gravity = 1
m = 1
dt = 1

move_speed = 1
jump_speed = 35
move_speed = 1


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

chemin_perso_left = "images/perso_left.png"
chemin_perso_right = "images/perso_right.png"

chemin_fleche_left = "images/fleche_left.png"
chemin_fleche_right = "images/fleche_right.png"
chemin_fleche_up = "images/fleche_up.png"
chemin_fleche_down = "images/fleche_down.png"
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
