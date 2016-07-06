from classe_niveau import *

class Menu:
    "classe des menus"

    def __init__(self):
        "cree un menu"

        self.vie = 3
        self.on = 1
        self.initialiser_pygame()
        self.initialiser_fenetre()
        self.img = pygame.image.load(chemin_menu).convert_alpha()
        self.next_niveau = 1
        self.premier_lancement = True
        self.bouton_vies = pygame.image.load(bouton_mode_vies).convert_alpha()
        self.bouton_vitesse = pygame.image.load(bouton_mode_vitesse).convert_alpha()
        self.bouton_forces = pygame.image.load(bouton_mode_forces).convert_alpha()
        self.bouton_vitesse1 = pygame.image.load(bouton_mode_vitesse1).convert_alpha()
        self.bouton_vies1 = pygame.image.load(bouton_mode_vies1).convert_alpha()
        self.bouton_forces1 = pygame.image.load(bouton_mode_forces1).convert_alpha()

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

    def creer_niveau(self):
        "instancie un niveau"
        self.niveau = Niveau(self, chemins_niveaux[self.next_niveau - 1])

    def boucle_evenement(self):
        "traite les actions du joueur"
        for event in pygame.event.get():
            pygame.display.get_surface().blit(self.bouton_vies, bouton1_pos)
            pygame.display.get_surface().blit(self.bouton_vitesse, bouton2_pos)
            pygame.display.get_surface().blit(self.bouton_forces, bouton3_pos)
            posSouris = pygame.mouse.get_pos()


            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                self.on = 0
                #on quitte le jeu


            elif event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] <= bouton1_bas and event.pos[1] >= bouton1_haut and  event.pos[0] <= bouton1_droite and event.pos[0] >= bouton1_gauche :
                self.mode = 'hard'
                self.gravity = 1
                self.m = 1
                self.dt = 1

                self.move_speed = 1
                self.jump_speed = 35

                self.f_solide = 0.14
                self.f_fluide = 0.14

                self.premier_lancement = False
                self.creer_niveau()
                self.niveau.afficher()
                self.niveau.boucle_principale()

            elif event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] <= bouton2_bas and event.pos[1] >= bouton2_haut and  event.pos[0] <= bouton2_droite and event.pos[0] >= bouton2_gauche :

                self.mode = 'easy'
                print(self.mode)

                self.gravity = 1
                self.m = 1
                self.dt = 1

                self.move_speed = 1
                self.jump_speed = 35

                self.f_solide = 0.14
                self.f_fluide = 0.14

                self.premier_lancement = False
                self.creer_niveau()
                self.niveau.afficher()
                self.niveau.boucle_principale()

            elif event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] <= bouton3_bas and event.pos[1] >= bouton3_haut and  event.pos[0] <= bouton3_droite and event.pos[0] >= bouton3_gauche :
                self.mode = 'forces'
                mode_force = True

                #On définit les constantes du mode force :
                self.gravity = 35
                self.m = 1
                self.dt = 0.1
                self.move_force = 60
                self.jump_force = 900
                self.move_speed = 0
                self.jump_speed = 0

                self.f_solide = 1
                self.f_fluide = 0.1
                print(self.mode)

                self.premier_lancement = False
                self.creer_niveau()
                self.niveau.afficher()
                self.niveau.boucle_principale()

                #On définit les variables du mode force :



            elif posSouris[1] <= bouton2_bas and posSouris[1] >= bouton2_haut and  posSouris[0] <= bouton2_droite and posSouris[0] >= bouton2_gauche :
                pygame.display.get_surface().blit(self.bouton_vitesse1, bouton2_pos)

            elif  posSouris[1] <= bouton1_bas and posSouris[1] >= bouton1_haut and  posSouris[0] <= bouton1_droite and posSouris[0] >= bouton1_gauche :
                pygame.display.get_surface().blit(self.bouton_vies1, bouton1_pos)

            elif  posSouris[1] <= bouton3_bas and posSouris[1] >= bouton3_haut and  posSouris[0] <= bouton3_droite and posSouris[0] >= bouton3_gauche :
                pygame.display.get_surface().blit(self.bouton_forces1, bouton3_pos)

            pygame.display.flip()


    def boucle_principale(self):
        "boucle globale du menu"
        self.afficher()
        while self.on:
            if self.next_niveau == 1 and self.premier_lancement:
                self.boucle_evenement()
            else:
                self.creer_niveau()
                self.niveau.afficher()
                self.niveau.boucle_principale()


if __name__ == "__main__":
    from main import *
