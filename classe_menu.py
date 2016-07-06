from classe_niveau import *

class Menu:
    "classe des menus"

    def __init__(self):
        "cree un menu"
        self.on = 1
        self.next_niveau = 1
        self.initialiser_pygame()
        self.initialiser_fenetre()
        self.charger_images()
        self.premier_lancement = True
        self.vie = 3

    def charger_images(self):
        "charge les images"
        self.img = pygame.image.load(chemin_menu).convert_alpha()
        self.img_win = pygame.image.load(chemin_win).convert_alpha()
        self.img_vitesse = pygame.image.load(chemin_vitesse).convert_alpha()
        self.img_vitesse1 = pygame.image.load(chemin_vitesse1).convert_alpha()
        self.img_force = pygame.image.load(chemin_force).convert_alpha()
        self.img_force1 = pygame.image.load(chemin_force1).convert_alpha()
        self.img_vies = pygame.image.load(chemin_vies).convert_alpha()
        self.img_vies1 = pygame.image.load(chemin_vies1).convert_alpha()

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
        pygame.display.get_surface().blit(self.img_vitesse, bouton1_pos)
        pygame.display.get_surface().blit(self.img_force, bouton2_pos)
        pygame.display.get_surface().blit(self.img_vies, bouton3_pos)

    def creer_niveau(self):
        "instancie un niveau"
        self.niveau = Niveau(self, chemins_niveaux[self.next_niveau - 1])

    def boucle_evenement(self):
        "traite les actions du joueur"
        for event in pygame.event.get():
            self.afficher()
            #pygame.time.Clock().tick(70)
            posSouris = pygame.mouse.get_pos()

            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                self.on = 0
                #on quitte le jeu

            elif event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] <= bouton1_bas and event.pos[1] >= bouton1_haut and  event.pos[0] <= bouton1_droite and event.pos[0] >= bouton1_gauche :
                self.mode = 'vitesse'

                #on definie les constantes correspondantes au mode
                self.gravity = mode_vitesse_gravity
                self.m = mode_vitesse_m
                self.dt = mode_vitesse_dt

                self.move_speed = mode_vitesse_move_speed
                self.jump_speed = mode_vitesse_jump_speed

                self.f_solide = mode_vitesse_f_solide
                self.f_fluide = mode_vitesse_f_fluide

                self.premier_lancement = False
                if self.next_niveau == len(chemins_niveaux) + 1:
                    pygame.display.get_surface().blit(self.img_win, (0, 0))
                    pygame.display.flip()
                    pygame.time.Clock().tick(1)
                    self.on = 0
                else:
                    self.creer_niveau()
                    self.niveau.afficher()
                    self.niveau.boucle_principale()

            elif event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] <= bouton2_bas and event.pos[1] >= bouton2_haut and  event.pos[0] <= bouton2_droite and event.pos[0] >= bouton2_gauche :
                self.mode = 'force'


                #On définit les constantes du mode force :
                self.gravity = mode_force_gravity
                self.m = mode_force_m
                self.dt = mode_force_dt
                self.move_force = mode_force_move_force
                self.jump_force = mode_force_jump_force

                self.f_solide = mode_force_f_solide
                self.f_fluide = mode_force_f_fluide

                self.premier_lancement = False
                if self.next_niveau == len(chemins_niveaux) + 1:
                    pygame.display.get_surface().blit(self.img_win, (0, 0))
                    pygame.display.flip()
                    pygame.time.Clock().tick(1)
                    self.on = 0
                else:
                    self.creer_niveau()
                    self.niveau.afficher()
                    self.niveau.boucle_principale()


            elif event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] <= bouton3_bas and event.pos[1] >= bouton3_haut and  event.pos[0] <= bouton3_droite and event.pos[0] >= bouton3_gauche :
                self.mode = 'vies'
                self.gravity = mode_vitesse_gravity
                self.m = mode_vitesse_m
                self.dt = mode_vitesse_dt

                self.move_speed = mode_vitesse_move_speed
                self.jump_speed = mode_vitesse_jump_speed

                self.f_solide = mode_vitesse_f_solide
                self.f_fluide = mode_vitesse_f_fluide

                self.premier_lancement = False
                if self.next_niveau == len(chemins_niveaux) + 1:
                    pygame.display.get_surface().blit(self.img_win, (0, 0))
                    pygame.display.flip()
                    pygame.time.Clock().tick(1)
                    self.on = 0
                else:
                    self.creer_niveau()
                    self.niveau.afficher()
                    self.niveau.boucle_principale()


            elif posSouris[1] <= bouton2_bas and posSouris[1] >= bouton2_haut and  posSouris[0] <= bouton1_droite and posSouris[0] >= bouton1_gauche :
                pygame.display.get_surface().blit(self.img,(0,0))
                pygame.display.get_surface().blit(self.img_vitesse1, bouton1_pos)
                pygame.display.get_surface().blit(self.img_force, bouton2_pos)
                pygame.display.get_surface().blit(self.img_vies, bouton3_pos)

            elif posSouris[1] <= bouton1_bas and posSouris[1] >= bouton1_haut and  posSouris[0] <= bouton2_droite and posSouris[0] >= bouton2_gauche :
                pygame.display.get_surface().blit(self.img,(0,0))
                pygame.display.get_surface().blit(self.img_vitesse, bouton1_pos)
                pygame.display.get_surface().blit(self.img_force1, bouton2_pos)
                pygame.display.get_surface().blit(self.img_vies, bouton3_pos)

            elif posSouris[1] <= bouton3_bas and posSouris[1] >= bouton3_haut and  posSouris[0] <= bouton3_droite and posSouris[0] >= bouton3_gauche :
                pygame.display.get_surface().blit(self.img,(0,0))
                pygame.display.get_surface().blit(self.img_vitesse, bouton1_pos)
                pygame.display.get_surface().blit(self.img_force, bouton2_pos)
                pygame.display.get_surface().blit(self.img_vies1, bouton3_pos)

            pygame.display.flip()

    def boucle_principale(self):
        "boucle globale du menu"
        while self.on:
            if self.next_niveau == 1 and self.premier_lancement:
                self.boucle_evenement()
            else:
                pygame.display.set_caption(titre_fenetre + " - Niveau {0}".format(self.next_niveau))
                if self.next_niveau == len(chemins_niveaux) + 1:
                    pygame.display.get_surface().blit(self.img_win, (0, 0))
                    pygame.display.flip()
                    pygame.time.Clock().tick(1)
                    self.on = 0
                else:
                    self.creer_niveau()
                    self.niveau.afficher()
                    self.niveau.boucle_principale()


if __name__ == "__main__":
    from main import *
