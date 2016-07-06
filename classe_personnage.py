import pygame
from pygame.locals import *
from constantes import *


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
        self.fx_controle = 0
        self.fy_controle = 0
        self.vx_controle = 0
        self.vy_controle = 0
        self.ax = 0
        self.ay = 0
        self.frottements_x = 0
        self.frottements_y = 0
        self.f = self.niveau.menu.f_solide
        self.direction = "right"
        self.generer_images()
        self.width, self.height = self.img_left_gdown[0].get_rect().size
        self.liste_coins = self.generer_liste_coins()
        self.saut_possible = True
        self.compteur_affichages = 0

    def generer_images(self):
        "genere toutes les images du personnage en fonction de sa direction et de la direction de la gravite"
        self.img_left_gdown = [pygame.image.load(chemin_perso0).convert_alpha(), \
                               pygame.image.load(chemin_perso1).convert_alpha(), \
                               pygame.image.load(chemin_perso2).convert_alpha()]
        self.img_right_gdown = [pygame.transform.flip(self.img_left_gdown[0], 1, 0), \
                               pygame.transform.flip(self.img_left_gdown[1], 1, 0), \
                               pygame.transform.flip(self.img_left_gdown[2], 1, 0)]
        self.img_left_gright = [pygame.transform.rotate(self.img_left_gdown[0], 90), \
                               pygame.transform.rotate(self.img_left_gdown[1], 90), \
                               pygame.transform.rotate(self.img_left_gdown[2], 90)]
        self.img_right_gright = [pygame.transform.rotate(self.img_right_gdown[0], 90), \
                               pygame.transform.rotate(self.img_right_gdown[1], 90), \
                               pygame.transform.rotate(self.img_right_gdown[2], 90)]
        self.img_left_gup = [pygame.transform.rotate(self.img_left_gdown[0], 180), \
                               pygame.transform.rotate(self.img_left_gdown[1], 180), \
                               pygame.transform.rotate(self.img_left_gdown[2], 180)]
        self.img_right_gup = [pygame.transform.rotate(self.img_right_gdown[0], 180), \
                               pygame.transform.rotate(self.img_right_gdown[1], 180), \
                               pygame.transform.rotate(self.img_right_gdown[2], 180)]
        self.img_left_gleft = [pygame.transform.rotate(self.img_left_gdown[0], 270), \
                               pygame.transform.rotate(self.img_left_gdown[1], 270), \
                               pygame.transform.rotate(self.img_left_gdown[2], 270)]
        self.img_right_gleft = [pygame.transform.rotate(self.img_right_gdown[0], 270), \
                               pygame.transform.rotate(self.img_right_gdown[1], 270), \
                               pygame.transform.rotate(self.img_right_gdown[2], 270)]

    def masquer(self):
        "masque le personnage"
        pygame.display.get_surface().blit(self.niveau.surface,(self.X[1], self.Y[1]),pygame.Rect(self.X[1], self.Y[1], self.width, self.height))

    def afficher(self):
        "affiche le personnage"
        # le temps d affichage de chaque etat du personnage est proportionnel a la vitesse
        if self.niveau.gravity in ("up", "down"):
            self.compteur_affichages += 0.03 * self.Vx[0]
        else:
            self.compteur_affichages += 0.03 * self.Vy[0]

        i = int(self.compteur_affichages % 3)
        if self.niveau.gravity == "down":
            if self.direction == "left":
                pygame.display.get_surface().blit(self.img_left_gdown[i], (self.x, self.y))
            else:
                pygame.display.get_surface().blit(self.img_right_gdown[i], (self.x, self.y))
        elif self.niveau.gravity == "up":
            if self.direction == "left":
                pygame.display.get_surface().blit(self.img_right_gup[i], (self.x, self.y))
            else:
                pygame.display.get_surface().blit(self.img_left_gup[i], (self.x, self.y))
        elif self.niveau.gravity == "left":
            if self.direction == "up":
                pygame.display.get_surface().blit(self.img_left_gleft[i], (self.x, self.y))
            else:
                pygame.display.get_surface().blit(self.img_right_gleft[i], (self.x, self.y))
        else:
            if self.direction == "up":
                pygame.display.get_surface().blit(self.img_right_gright[i], (self.x, self.y))
            else:
                pygame.display.get_surface().blit(self.img_left_gright[i], (self.x, self.y))

    def bloc_equivalent(self, coordonnees):
        "renvoie la position en blocs d une position en pixels"
        return((coordonnees[0] // self.niveau.taille_bloc[0], coordonnees[1] // self.niveau.taille_bloc[1]))

    def generer_liste_coins(self):
        "renvoie une liste contenant les equivalents blocs des coordonnees des quatres coins du personnage"
        # position des coins :
        # 0     1
        #  perso
        # 2     3
        L = []
        L.append(self.bloc_equivalent((self.x, self.y)))
        L.append(self.bloc_equivalent((self.x + self.width, self.y)))
        L.append(self.bloc_equivalent((self.x, self.y + self.height)))
        L.append(self.bloc_equivalent((self.x + self.width, self.y + self.height)))
        return(L)

    def est_dans_un_bloc(self, bloc_type):
        "renvoie True si le personnage est dans un bloc"
        self.liste_coins = self.generer_liste_coins()
        for position in self.liste_coins:
            if position in self.niveau.dict_positions_blocs[bloc_type]:
                return(True)
        return(False)

    def contact_bloc(self):
        "LA fonction de contact! repositionne le personnage la ou il faut si il est dans un bloc"
        self.liste_coins = self.generer_liste_coins()
        L=[]
        for i in range(len(self.liste_coins)):
            if self.liste_coins[i] in self.niveau.dict_positions_blocs["b"]:
                L.append(i)
        if 2 in L and 3 in L:
            self.y = self.liste_coins[2][1]*40 - 0.5 - self.height
            if self.Vy[0] > 0:
                self.Vy[0] = 0
            self.Y = [self.y, self.y]
            if self.niveau.gravity == "down":
                self.saut_possible = True

        elif 0 in L and 1 in L:
            self.y = (self.liste_coins[0][1] + 1) * 40 + 0.5
            if self.Vy[0] < 0:
                self.Vy[0] = 0
            self.Y = [self.y, self.y]
            if self.niveau.gravity == "up":
                self.saut_possible = True

        elif 0 in L and 2 in L:
            self.x = (self.liste_coins[0][0] + 1) * 40 + 0.5
            if self.Vx[0] < 0:
                self.Vx[0] = 0
            self.X = [self.x, self.x]
            if self.niveau.gravity == "left":
                self.saut_possible = True

        elif 1 in L and 3 in L:
            self.x = self.liste_coins[1][0] * 40 - 0.5 - self.width
            if self.Vx[0] > 0:
                self.Vx[0] = 0
            self.X = [self.x, self.x]
            if self.niveau.gravity == "right":
                self.saut_possible = True


        elif self.niveau.gravity == "down" or self.niveau.gravity == "up":
            if 2 in L or 3 in L:
                self.y = self.liste_coins[2][1]*40 - 0.5 - self.height
                if self.Vy[0] > 0:
                    self.Vy[0] = 0
                self.Y = [self.y, self.y]
                self.saut_possible = True
            elif 0 in L or 1 in L:
                self.y = (self.liste_coins[0][1] + 1) * 40 + 0.5
                if self.Vy[0] < 0:
                    self.Vy[0] = 0
                self.Vy[0] = 0
                self.Y = [self.y, self.y]
                self.saut_possible = True
        elif self.niveau.gravity == "left" or self.niveau.gravity == "right":
            if 0 in L or 2 in L:
                self.x = (self.liste_coins[0][0] + 1) * 40 + 0.5
                if self.Vx[0] < 0:
                    self.Vx[0] = 0
                self.Vx[0] = 0
                self.X = [self.x, self.x]
                self.saut_possible = True
            elif 1 in L or 3 in L:
                self.x = self.liste_coins[1][0] * 40 - 0.5 - self.width
                if self.Vx[0] > 0:
                    self.Vx[0] = 0
                self.Vx[0] = 0
                self.X = [self.x, self.x]
                self.saut_possible = True
        else:
            saut_possible = True

    def PFD(self):
        "calcule la prochaine position a partir de la position actuelle"
        self.ax = self.niveau.gx + (self.frottements_x + self.fx_controle) / self.niveau.menu.m
        self.Vx[1] = self.ax * self.niveau.menu.dt + self.Vx[0] + self.vx_controle
        self.X[1] = 0.5 * self.ax * self.niveau.menu.dt ** 2 + self.Vx[0] * self.niveau.menu.dt + self.X[0]
        self.Vx[0], self.Vx[1] = self.Vx[1], self.Vx[0]
        self.X[0], self.X[1] = self.X[1], self.X[0]
        self.x = self.X[0]
        self.frottements_x = -self.f * self.Vx[0]
        if self.niveau.gravity in ("left", "right"):
            self.fx_controle, self.vx_controle = 0, 0

        self.ay = self.niveau.gy + (self.frottements_y + self.fy_controle) / self.niveau.menu.m
        self.Vy[1] = self.ay * self.niveau.menu.dt + self.Vy[0] + self.vy_controle
        self.Y[1] = 0.5 * self.ay * self.niveau.menu.dt ** 2 + self.Vy[0] * self.niveau.menu.dt + self.Y[0]
        self.Vy[0], self.Vy[1] = self.Vy[1], self.Vy[0]
        self.Y[0], self.Y[1] = self.Y[1], self.Y[0]
        self.y = self.Y[0]
        self.frottements_y = -self.f * self.Vy[0]
        if self.niveau.gravity in ("up", "down"):
            self.fy_controle, self.vy_controle = 0, 0

        self.liste_coins = self.generer_liste_coins()

    def die(self):
        "si le personnage est dans un bloc pics, il meurt"
        if self.est_dans_un_bloc("p"):
            self.niveau.on = 0
        if self.niveau.menu.mode == 'hard' :
            if self.est_dans_un_bloc("p"):
                self.niveau.menu.vie += -1
            if self.niveau.menu.vie == 0:
                self.niveau.on = 0
                self.niveau.menu.on = 0

    def controler_vitesse(self, event):
        "gere le controle manuel du personnage a l aide des touches de direction"
        if self.niveau.gravity in ("down", "up"):
            if event.type == KEYDOWN:
                touches_pressees = pygame.key.get_pressed()
                if touches_pressees[K_LEFT]:
                    self.vx_controle = -self.niveau.menu.move_speed
                    self.direction = "left"
                elif touches_pressees[K_RIGHT]:
                    self.vx_controle = self.niveau.menu.move_speed
                    self.direction = "right"
                else:
                    self.vx_controle = 0
                if (touches_pressees[K_UP] or touches_pressees[K_SPACE]) and self.niveau.gravity == "down" and self.saut_possible:
                    self.vy_controle = -self.niveau.menu.jump_speed
                    self.saut_possible = False
                elif (touches_pressees[K_DOWN] or touches_pressees[K_SPACE]) and self.niveau.gravity == "up" and self.saut_possible:
                    self.vy_controle = self.niveau.menu.jump_speed
                    self.saut_possible = False
            if event.type == KEYUP:
                if event.key == K_LEFT or event.key == K_RIGHT:
                    self.vx_controle = 0
                if event.key == K_UP or event.key == K_DOWN:
                    self.vy_controle = 0

        elif self.niveau.gravity in ("left", "right"):
            if event.type == KEYDOWN:
                touches_pressees = pygame.key.get_pressed()
                if touches_pressees[K_UP]:
                    self.vy_controle = -self.niveau.menu.move_speed
                    self.direction = "up"
                elif touches_pressees[K_DOWN]:
                    self.vy_controle = self.niveau.menu.move_speed
                    self.direction = "down"
                else:
                    self.vy_controle = 0
                if (touches_pressees[K_LEFT] or touches_pressees[K_SPACE]) and self.niveau.gravity == "right" and self.saut_possible:
                    self.vx_controle = -self.niveau.menu.jump_speed
                    self.saut_possible = False
                elif (touches_pressees[K_RIGHT] or touches_pressees[K_SPACE]) and self.niveau.gravity == "left" and self.saut_possible:
                    self.vx_controle = self.niveau.menu.jump_speed
                    self.saut_possible = False
            if event.type == KEYUP:
                if event.key == K_LEFT or event.key == K_RIGHT:
                    self.vx_controle = 0
                if event.key == K_UP or event.key == K_DOWN:
                    self.vy_controle = 0

    def controler_force(self, event):
        "gere le controle manuel du personnage a l aide des touches de direction"
        if self.niveau.gravity in ("down", "up"):
            if event.type == KEYDOWN:
                touches_pressees = pygame.key.get_pressed()
                if touches_pressees[K_LEFT]:
                    self.fx_controle = -self.niveau.move_force
                    self.direction = "left"
                elif touches_pressees[K_RIGHT]:
                    self.fx_controle = self.niveau.move_force
                    self.direction = "right"
                else:
                    self.fx_controle = 0
                if (touches_pressees[K_UP] or touches_pressees[K_SPACE]) and self.niveau.gravity == "down" and self.saut_possible:
                    self.fy_controle = -self.niveau.jump_force
                    self.saut_possible = False
                elif (touches_pressees[K_DOWN] or touches_pressees[K_SPACE]) and self.niveau.gravity == "up" and self.saut_possible:
                    self.fy_controle = self.niveau.jump_force
                    self.saut_possible = False
            if event.type == KEYUP:
                if event.key == K_LEFT or event.key == K_RIGHT:
                    self.fx_controle = 0
                if event.key == K_UP or event.key == K_DOWN:
                    self.fy_controle = 0

        elif self.niveau.gravity in ("left", "right"):
            if event.type == KEYDOWN:
                touches_pressees = pygame.key.get_pressed()
                if touches_pressees[K_UP]:
                    self.fy_controle = -self.niveau.move_force
                    self.direction = "up"
                elif touches_pressees[K_DOWN]:
                    self.fy_controle = self.niveau.move_force
                    self.direction = "down"
                else:
                    self.fy_controle = 0
                if (touches_pressees[K_LEFT] or touches_pressees[K_SPACE]) and self.niveau.gravity == "right" and self.saut_possible:
                    self.fx_controle = -self.niveau.jump_force
                    self.saut_possible = False
                    self.chute_libre = True
                elif (touches_pressees[K_RIGHT] or touches_pressees[K_SPACE]) and self.niveau.gravity == "left" and self.saut_possible:
                    self.fx_controle = self.niveau.jump_force
                    self.saut_possible = False
                    self.chute_libre = True
            if event.type == KEYUP:
                if event.key == K_LEFT or event.key == K_RIGHT:
                    self.fx_controle = 0
                if event.key == K_UP or event.key == K_DOWN:
                    self.fy_controle = 0

    def rebondis(self):
        "n est plus utilisee, empechait le personnage de tomber de l ecran"
        if self.x < 0:
            self.x = 0
            if self.Vx[0] < 0:
                #self.Vx[0] = 0
                self.Vx[0] =- 0.88 * self.Vx[0]
        if self.x > window_width - self.width:
            self.x = window_width - self.width
            if self.Vx[0] > 0:
                #self.Vx[0] = 0
                self.Vx[0] =- 0.88 * self.Vx[0]
        if self.y < 0:
            self.y = 0
            if self.Vy[0] < 0:
                #self.Vy[0] = 0
                self.Vy[0] =- 0.88 * self.Vy[0]
        if self.y > window_height - self.height:
            self.y = window_height - self.height
            if self.Vy[0] > 0:
                #self.Vy[0] = 0
                self.Vy[0] =- 0.88 * self.Vy[0]

    def update_frottements(self):
        "met a jour les coefficients de frottements selon l etat du personnage (en chute ou au sol)"
        if self.saut_possible:
            self.f = self.niveau.menu.f_solide

        else:
            self.f = self.niveau.menu.f_fluide

    def gravity_switch_offset(self):
        "effectue des reglages suite a un changement de gravite"
        """
        self.x -= (self.height - self.width) / 2
        self.X[0] -= (self.height - self.width) / 2
        self.X[1] -= (self.height - self.width) / 2
        self.y += (self.height - self.width) / 2
        self.Y[0] += (self.height - self.width) / 2
        self.Y[1] += (self.height - self.width) / 2
        """
        self.height, self.width = self.width, self.height

    def chute_libre_stricte(self):
        """bloque les touches si le perso chute pour faire comme de vrai, fonction a ne pas appeller si on veut un jeu moins realiste mais plus jouable"""   #####################
        if not self.saut_possible and self.fx_controle != self.niveau.jump_force and self.fx_controle != -self.niveau.jump_force and self.fy_controle != self.niveau.jump_force and self.fy_controle != -self.niveau.jump_force:
            self.fx_controle = 0
            self.fy_controle = 0

    def chute_libre_regulee(self):
        """ajuste la force de deplacement en fonction de l etat de chute libre ou non"""
        if self.saut_possible:
            self.niveau.move_force = self.niveau.menu.move_force
        else:
            self.niveau.move_force = self.niveau.menu.move_force / 10


if __name__ == "__main__":
    from main import *
