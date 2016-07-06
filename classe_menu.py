from classe_niveau import *

class Menu:
    "classe des menus"

    def __init__(self):
        "cree un menu"
        self.on = 1
        self.initialiser_pygame()
        self.initialiser_fenetre()
        self.img = pygame.image.load(chemin_menu).convert_alpha()
        self.next_niveau = -1

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
        self.niveau = Niveau(self, chemins_niveaux[self.next_niveau])

    def boucle_evenement(self):
        "traite les actions du joueur"
        self.next_niveau = 0
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                self.on = 0
                #on quitte le jeu
            elif event.type == KEYDOWN and event.key == K_SPACE:
                self.creer_niveau()
                self.niveau.afficher()
                self.niveau.boucle_principale()

    def boucle_principale(self):
        "boucle globale du menu"
        self.afficher()
        while self.on:
            if self.next_niveau != -1:
                self.creer_niveau()
                self.niveau.afficher()
                self.niveau.boucle_principale()
            else:
                self.boucle_evenement()


if __name__ == "__main__":
    from main import *
