#!/usr/bin/python3
# -*- coding: Utf-8 -*

import pygame
from pygame.locals import *
from constantes import *
from classes import *

menu = Menu()
while menu.on:
    menu.afficher()
    #on attend une action du joueur
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            menu.on = 0
            #on quitte le jeu

        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                # on cree le niveau et le perso
                niveau1 = Niveau(chemin_niveau1)
                #perso = Personnage(niveau1)
                niveau1.afficher()
                compteur = 100
                while niveau1.on:
                    compteur += 1
                    #compteur = 51
                    pygame.time.Clock().tick(70)
                    for event in pygame.event.get():
                        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                            niveau1.on, menu.on = 0, 0


                        elif niveau1.gravity in ("down", "up"):
                            if event.type == KEYDOWN:
                                touches_pressees = pygame.key.get_pressed()
                                if touches_pressees[K_LEFT]:
                                    niveau1.personnage.vx_controle = -move_speed
                                    niveau1.personnage.direction = "left"
                                elif touches_pressees[K_RIGHT]:
                                    niveau1.personnage.vx_controle = move_speed
                                    niveau1.personnage.direction = "right"
                                else:
                                    niveau1.personnage.vx_controle = 0
                                if touches_pressees[K_UP] and niveau1.gravity == "down":
                                    if compteur > 50:
                                        niveau1.personnage.vy_controle = -jump_speed
                                        compteur = 0
                                elif touches_pressees[K_DOWN] and niveau1.gravity == "up":
                                    if compteur > 50:
                                        niveau1.personnage.vy_controle = jump_speed
                                        compteur = 0
                            if event.type == KEYUP:
                                if event.key == K_LEFT or event.key == K_RIGHT:
                                    niveau1.personnage.vx_controle = 0
                                if event.key == K_UP or event.key == K_DOWN:
                                    niveau1.personnage.vy_controle = 0

                        elif niveau1.gravity in ("left", "right"):
                            if event.type == KEYDOWN:
                                touches_pressees = pygame.key.get_pressed()
                                if touches_pressees[K_UP]:
                                    niveau1.personnage.vy_controle = -move_speed
                                    niveau1.personnage.direction = "up"
                                elif touches_pressees[K_DOWN]:
                                    niveau1.personnage.vy_controle = move_speed
                                    niveau1.personnage.direction = "down"
                                else:
                                    niveau1.personnage.vy_controle = 0
                                if touches_pressees[K_LEFT] and niveau1.gravity == "right":
                                    if compteur > 50:
                                        niveau1.personnage.vx_controle = -jump_speed
                                        compteur = 0
                                elif touches_pressees[K_RIGHT] and niveau1.gravity == "left":
                                    if compteur > 50:
                                        niveau1.personnage.vx_controle = jump_speed
                                        compteur = 0
                            if event.type == KEYUP:
                                if event.key == K_LEFT or event.key == K_RIGHT:
                                    niveau1.personnage.vx_controle = 0
                                if event.key == K_UP or event.key == K_DOWN:
                                    niveau1.personnage.vy_controle = 0

                    niveau1.personnage.PFD()
                    #niveau1.test_de_contact()
                    niveau1.personnage.rebondis()
                    niveau1.afficher()
                    niveau1.switch_gravity()
                    niveau1.win()
                    #print(niveau1.est_dans_un_bloc())
