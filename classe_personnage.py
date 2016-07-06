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
        self.vx_controle = 0
        self.vy_controle = 0
        self.ax = 0
        self.ay = 0
        self.frottements_x = 0
        self.frottements_y = 0
        self.direction = "down"
        self.img_left = pygame.image.load(chemin_perso_left).convert_alpha()
        self.img_right = pygame.image.load(chemin_perso_right).convert_alpha()
        self.img_up = pygame.image.load(chemin_perso_up).convert_alpha()
        self.img_down = pygame.image.load(chemin_perso_down).convert_alpha()
        self.width, self.height = self.img_left.get_rect().size
        self.liste_coins = self.generer_liste_coins()
        self.saut_possible = True

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

    def est_dans_un_bloc(self, bloc_type):
        "renvoie True si le personnage est dans un bloc"
        self.liste_coins = self.generer_liste_coins()
        for position in self.liste_coins:
            if position in self.niveau.dict_positions_blocs[bloc_type]:
                return(True)
        return(False)

    def vous_ne_passerez_pas(self):
        "LA putain de fonction de contact qui marche enfin! (ou presque)"
        self.liste_coins = self.generer_liste_coins()
        L=[]
        for i in range(len(self.liste_coins)):
            if self.liste_coins[i] in self.niveau.dict_positions_blocs["b"]:
                L.append(i)
        if 2 in L and 3 in L:
            self.y = self.liste_coins[2][1]*40 - 1 - self.height
            if self.Vy[0] > 0:
                self.Vy[0] = 0
            self.Y = [self.liste_coins[2][1]*40 - 1 - self.height, self.liste_coins[2][1]*40 - 1 - self.height]
            if self.niveau.gravity == "down":
                self.saut_possible = True

        elif 0 in L and 1 in L:
            self.y = (self.liste_coins[0][1] + 1) * 40 + 1
            if self.Vy[0] < 0:
                self.Vy[0] = 0
            self.Y = [(self.liste_coins[0][1] + 1) * 40 + 1, (self.liste_coins[0][1] + 1) * 40 + 1]
            if self.niveau.gravity == "up":
                self.saut_possible = True

        elif 0 in L and 2 in L:
            self.x = (self.liste_coins[0][0] + 1) * 40 + 1
            if self.Vx[0] < 0:
                self.Vx[0] = 0
            self.X = [(self.liste_coins[0][0] + 1) * 40 + 1, (self.liste_coins[0][0] + 1) * 40 + 1]
            if self.niveau.gravity == "left":
                self.saut_possible = True

        elif 1 in L and 3 in L:
            self.x = self.liste_coins[1][0] * 40 - 1 - self.width
            if self.Vx[0] > 0:
                self.Vx[0] = 0
            self.X = [self.liste_coins[1][0] * 40 - 1 - self.width, self.liste_coins[1][0] * 40 - 1 - self.width]
            if self.niveau.gravity == "right":
                self.saut_possible = True


        elif self.niveau.gravity == "down" or self.niveau.gravity == "up":
            if 2 in L or 3 in L:
                self.y = self.liste_coins[2][1]*40 - 1 - self.height
                if self.Vy[0] > 0:
                    self.Vy[0] = 0
                self.Y = [self.liste_coins[2][1]*40 - 1 - self.height, self.liste_coins[2][1]*40 - 1 - self.height]
                self.saut_possible = True
            elif 0 in L or 1 in L:
                self.y = (self.liste_coins[0][1] + 1) * 40 + 1
                if self.Vy[0] < 0:
                    self.Vy[0] = 0
                self.Vy[0] = 0
                self.Y = [(self.liste_coins[0][1] + 1) * 40 + 1, (self.liste_coins[0][1] + 1) * 40 + 1]
                self.saut_possible = True
        elif self.niveau.gravity == "left" or self.niveau.gravity == "right":
            if 0 in L or 2 in L:
                self.x = (self.liste_coins[0][0] + 1) * 40 + 1
                if self.Vx[0] < 0:
                    self.Vx[0] = 0
                self.Vx[0] = 0
                self.X = [(self.liste_coins[0][0] + 1) * 40 + 1, (self.liste_coins[0][0] + 1) * 40 + 1]
                self.saut_possible = True
            elif 1 in L or 3 in L:
                self.x = self.liste_coins[1][0] * 40 - 1 - self.width
                if self.Vx[0] > 0:
                    self.Vx[0] = 0
                self.Vx[0] = 0
                self.X = [self.liste_coins[1][0] * 40 - 1 - self.width, self.liste_coins[1][0] * 40 - 1 - self.width]
                self.saut_possible = True

        if self.saut_possible:
            self.frottements_x = f_solide
            self.frottements_y = f_solide

    def PFD(self):
        "calcule la prochaine position a partir de la position actuelle"
        self.ax = self.niveau.gx + self.frottements_x
        self.Vx[1] = self.ax * dt + self.Vx[0] + self.vx_controle
        self.X[1] = 0.5 * self.ax * dt ** 2 + self.Vx[0] * dt + self.X[0]
        self.Vx[0], self.Vx[1] = self.Vx[1], self.Vx[0]
        self.X[0], self.X[1] = self.X[1], self.X[0]
        self.x = self.X[0]
        self.frottements_x = -f * self.Vx[0]
        if self.niveau.gravity in ("left", "right"):
            self.vx_controle = 0

        self.ay = self.niveau.gy + self.frottements_y
        self.Vy[1] = self.ay * dt + self.Vy[0] + self.vy_controle
        self.Y[1] = 0.5 * self.ay * dt ** 2 + self.Vy[0] * dt + self.Y[0]
        self.Vy[0], self.Vy[1] = self.Vy[1], self.Vy[0]
        self.Y[0], self.Y[1] = self.Y[1], self.Y[0]
        self.y = self.Y[0]
        self.frottements_y = -f * self.Vy[0]
        if self.niveau.gravity in ("up", "down"):
            self.vy_controle = 0

        self.liste_coins = self.generer_liste_coins()

    def die(self):
        if self.est_dans_un_bloc("p"):
            self.niveau.on = 0

    def controler(self, event):
        if self.niveau.gravity in ("down", "up"):
            if event.type == KEYDOWN:
                touches_pressees = pygame.key.get_pressed()
                if touches_pressees[K_LEFT]:
                    self.vx_controle = -move_speed
                    self.direction = "left"
                elif touches_pressees[K_RIGHT]:
                    self.vx_controle = move_speed
                    self.direction = "right"
                else:
                    self.vx_controle = 0
                if touches_pressees[K_UP] and self.niveau.gravity == "down" and self.saut_possible:
                    self.vy_controle = -jump_speed
                    self.saut_possible = False
                elif touches_pressees[K_DOWN] and self.niveau.gravity == "up" and self.saut_possible:
                    self.vy_controle = jump_speed
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
                    self.vy_controle = -move_speed
                    self.direction = "up"
                elif touches_pressees[K_DOWN]:
                    self.vy_controle = move_speed
                    self.direction = "down"
                else:
                    self.vy_controle = 0
                if touches_pressees[K_LEFT] and self.niveau.gravity == "right" and self.saut_possible:
                    self.vx_controle = -jump_speed
                    self.saut_possible = False
                elif touches_pressees[K_RIGHT] and self.niveau.gravity == "left" and self.saut_possible:
                    self.vx_controle = jump_speed
                    self.saut_possible = False
            if event.type == KEYUP:
                if event.key == K_LEFT or event.key == K_RIGHT:
                    self.vx_controle = 0
                if event.key == K_UP or event.key == K_DOWN:
                    self.vy_controle = 0

    def rebondis(self):
        "just for fun ;)"
        if self.x < 0 + 40:
            self.x = 0 + 40
            if self.Vx[0] < 0:
                self.Vx[0] = 0
            #self.Vx[0] =- 0.88 * self.Vx[0]
        if self.x > window_width - self.width - 40:
            self.x = window_width - self.width - 40
            if self.Vx[0] > 0:
                self.Vx[0] = 0
            #self.Vx[0] =- 0.88 * self.Vx[0]
        if self.y < 0 + 40:
            self.y = 0 + 40
            if self.Vy[0] < 0:
                self.Vy[0] = 0
            #self.Vy[0] =- 0.88 * self.Vy[0]
        if self.y > window_height - self.height - 40:
            self.y = window_height - self.height - 40
            if self.Vy[0] > 0:
                self.Vy[0] = 0
            #self.Vy[0] =- 0.88 * self.Vy[0]
        """
        if abs(self.Vx[0]) < 1:
            self.Vx[0] = 0
        if abs(self.Vy[0]) < 1:
            self.Vy[0] = 0
        """
