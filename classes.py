import pygame
from pygame.locals import *
from constantes import *

class Menu:
    "classe des menus"

    def __init__(self):
        "cree un menu"
        self.on = 1
        self.initialiser_pygame()
        self.initialiser_fenetre()
        self.img = pygame.image.load(chemin_menu).convert_alpha()

    def initialiser_pygame(self):
        "initialise pygame"
        pygame.init()
        pygame.key.set_repeat(repeat_wait, repeat_every)

    def initialiser_fenetre(self):
        "initialise la fenetre"
        pygame.display.set_mode((window_width, window_height))
        pygame.display.set_icon(pygame.image.load(chemin_icone).convert_alpha())
        pygame.display.set_caption(titre_fenetre)

    def afficher(self):
        "affiche le menu"
        pygame.display.get_surface().blit(self.img,(0,0))
        pygame.display.flip()

################################################################################

class Personnage:
    "classe des personnages"

    def __init__(self, niveau):
        "cree un personnage"
        self.niveau = niveau
        self.x, self.y = self.niveau.position_initiale
        self.X = [self.x, self.x]
        self.Y = [self.y, self.y]
        self.Vx = [0, 0]
        self.Vy = [0, 0]
        self.vx_controle = 0
        self.vy_controle = 0
        self.ax = 0
        self.ay = 0
        self.frottements_x = 0
        self.frottements_y = 0
        self.gx = 0
        self.gy = gravity
        self.direction = "down"
        self.img_left = pygame.image.load(chemin_perso_left).convert_alpha()
        self.img_right = pygame.image.load(chemin_perso_right).convert_alpha()
        self.img_up = pygame.image.load(chemin_perso_up).convert_alpha()
        self.img_down = pygame.image.load(chemin_perso_down).convert_alpha()
        self.width, self.height = self.img_left.get_rect().size
        self.liste_coins = self.generer_liste_coins()

    def masquer(self):
        "masque le personnage"
        pygame.display.get_surface().blit(niveau.surface,(self.X[1], self.Y[1]),pygame.Rect(self.X[1], self.Y[1], self.width, self.height))

    def afficher(self):
        "affiche le personnage"
        if self.direction == "left":
            pygame.display.get_surface().blit(self.img_left, (self.x, self.y))
        if self.direction == "right":
            pygame.display.get_surface().blit(self.img_right, (self.x, self.y))
        if self.direction == "up":
            pygame.display.get_surface().blit(self.img_up, (self.x, self.y))
        if self.direction == "down":
            pygame.display.get_surface().blit(self.img_down, (self.x, self.y))

    def PFD(self):
        "calcule la prochaine position a partir de la position actuelle"
        self.ax = self.gx + self.frottements_x / m
        self.Vx[1] = self.ax * dt + self.Vx[0] + self.vx_controle
        self.X[1] = 0.5 * self.ax * dt ** 2 + self.Vx[0] * dt + self.X[0]
        self.Vx[0], self.Vx[1] = self.Vx[1], self.Vx[0]
        self.X[0], self.X[1] = self.X[1], self.X[0]
        self.x = self.X[0]
        self.frottements_x = -f * self.Vx[0]
        if self.niveau.gravity in ("left", "right"):
            self.vx_controle = 0

        self.ay = self.gy + self.frottements_y / m
        self.Vy[1] = self.ay * dt + self.Vy[0] + self.vy_controle
        self.Y[1] = 0.5 * self.ay * dt ** 2 + self.Vy[0] * dt + self.Y[0]
        self.Vy[0], self.Vy[1] = self.Vy[1], self.Vy[0]
        self.Y[0], self.Y[1] = self.Y[1], self.Y[0]
        self.y = self.Y[0]
        self.frottements_y = -f * self.Vy[0]
        if self.niveau.gravity in ("up", "down"):
            self.vy_controle = 0

        self.liste_coins = self.generer_liste_coins()

    def rebondis(self):
        "just for fun ;)"
        if self.x < 0 + 40:
            self.x = 0 + 40
            self.Vx[0] =- self.Vx[0]
        if self.x > window_width - self.width - 40:
            self.x = window_width - self.width - 40
            self.Vx[0] =- self.Vx[0]
        if self.y < 0 + 40:
            self.y = 0 + 40
            self.Vy[0] =- self.Vy[0]
        if self.y > window_height - self.height - 40:
            self.y = window_height - self.height - 40
            self.Vy[0] =- self.Vy[0]
        """
        if abs(self.Vx[0]) < 1:
            self.Vx[0] = 0
        if abs(self.Vy[0]) < 1:
            self.Vy[0] = 0
        """

    def bloc_equivalent(self, coordonnees):
        "renvoie la position en blocs d une position en pixels"
        return((coordonnees[0] // self.niveau.taille_bloc[0], coordonnees[1] // self.niveau.taille_bloc[1]))

    def generer_liste_coins(self):
        "renvoie une liste contenant les equivalents blocs des coordonnees des quatres coins du personnage"
        L = []
        L.append(self.bloc_equivalent((self.x, self.y)))
        L.append(self.bloc_equivalent((self.x + self.width, self.y)))
        L.append(self.bloc_equivalent((self.x, self.y + self.height)))
        L.append(self.bloc_equivalent((self.x + self.width, self.y + self.height)))
        return(L)

################################################################################

class Niveau:
    "classe des niveaux"

    def __init__(self, chemin_fichier):
        "cree un niveau"
        self.on = 1
        self.matrice = self.generer_matrice(chemin_fichier)
        self.img_background = pygame.image.load(chemin_background).convert_alpha()
        self.img_fleche_left = pygame.image.load(chemin_fleche_left).convert_alpha()
        self.img_fleche_right = pygame.image.load(chemin_fleche_right).convert_alpha()
        self.img_fleche_up = pygame.image.load(chemin_fleche_up).convert_alpha()
        self.img_fleche_down = pygame.image.load(chemin_fleche_down).convert_alpha()
        self.img_entree = pygame.image.load(chemin_entree).convert_alpha()
        self.img_sortie = pygame.image.load(chemin_sortie).convert_alpha()
        self.img_bloc = pygame.image.load(chemin_bloc).convert_alpha()
        self.taille_bloc = self.img_bloc.get_rect().size
        self.surface = self.generer_surface()
        self.compteur_affichage = 0
        self.position_initiale = self.definir_position("e")
        self.personnage = Personnage(self)
        self.generer_dict_positions_blocs()
        self.gravity = "down"

    def generer_matrice(self, chemin_fichier):
        "genere la matrice du niveau"
        fichier = open(chemin_fichier, "r")
        matrice = []
        for ligne in fichier:
            liste=[lettre for lettre in ligne]
            matrice.append(liste[:len(liste)-1])
        fichier.close()
        return(matrice)

    def definir_position(self, bloc_type):
        "renvoie les coordonnees de l entree du nivau"
        for i in range(len(self.matrice)):
            for j in range(len(self.matrice[0])):
                if self.matrice[i][j] == bloc_type:
                    return((j * self.taille_bloc[0], i * self.taille_bloc[1]))

    def generer_positions_blocs(self, bloc_type):
        "genere la liste des positions des blocs du niveau (en blocs)"
        L=[]
        for i in range(len(self.matrice)):
            for j in range(len(self.matrice[0])):
                if self.matrice[i][j] == bloc_type:
                    L.append((j, i))
        return(L)

    def generer_dict_positions_blocs(self):
        self.dict_positions_blocs = dict()
        for bloc_type in liste_blocs:
            self.dict_positions_blocs[bloc_type] = self.generer_positions_blocs(bloc_type)

    def est_dans_un_bloc(self, bloc_type):
        "renvoie True si le personnage est dans un bloc"
        for position in self.personnage.liste_coins:
            if position in self.dict_positions_blocs[bloc_type]:
                return(True)
        return(False)

    def generer_surface(self):
        "genere une surface avec tous les blocs du niveau"
        self.surface = pygame.Surface((window_width, window_height))
        self.surface.blit(self.img_background, (0, 0))
        for i in range(len(self.matrice)):
            for j in range(len(self.matrice[0])):
                if self.matrice[i][j] == 'b' :
                    self.surface.blit(self.img_bloc, (j * self.taille_bloc[0], i * self.taille_bloc[1]))
                if self.matrice[i][j] == 'l' :
                    self.surface.blit(self.img_fleche_left, (j * self.taille_bloc[0], i * self.taille_bloc[1]))
                if self.matrice[i][j] == 'r' :
                    self.surface.blit(self.img_fleche_right, (j * self.taille_bloc[0], i * self.taille_bloc[1]))
                if self.matrice[i][j] == 'u' :
                    self.surface.blit(self.img_fleche_up, (j * self.taille_bloc[0], i * self.taille_bloc[1]))
                if self.matrice[i][j] == 'd' :
                    self.surface.blit(self.img_fleche_down, (j * self.taille_bloc[0], i * self.taille_bloc[1]))
                if self.matrice[i][j] == 'e' :
                    self.surface.blit(self.img_entree, (j * self.taille_bloc[0], i * self.taille_bloc[1]))
                if self.matrice[i][j] == 's' :
                    self.surface.blit(self.img_sortie, (j * self.taille_bloc[0], i * self.taille_bloc[1]))
        return(self.surface)


    def afficher(self):
        "affiche le niveau et le personnage dans le bon ordre"
        if self.compteur_affichage == 0:
            pygame.display.get_surface().blit(self.surface, (0, 0))
        else:
            self.personnage.masquer()
        self.personnage.afficher()
        pygame.display.flip()

    def win(self):
        if self.est_dans_un_bloc("s"):
            print("you win")
            self.on = 0

    def switch_gravity(self):
        if self.est_dans_un_bloc("u"):
            self.gravity = "up"
            self.personnage.gy = -gravity
            self.personnage.gx = 0
        if self.est_dans_un_bloc("d"):
            self.gravity = "down"
            self.personnage.gy = gravity
            self.personnage.gx = 0
        if self.est_dans_un_bloc("l"):
            self.gravity = "left"
            self.personnage.gx = -gravity
            self.personnage.gy = 0
        if self.est_dans_un_bloc("r"):
            self.gravity = "right"
            self.personnage.gx = gravity
            self.personnage.gy = 0

    def test_de_contact(self):
        if self.est_dans_un_bloc("b"):
            print("in bloc")
            self.personnage.x = self.personnage.X[1]
            self.personnage.y = self.personnage.Y[1]
            self.personnage.liste_coins = self.personnage.generer_liste_coins()
