from random import randint
from classe_personnage import *

class Niveau:
    "classe des niveaux"

    def __init__(self, menu, chemin_fichier):
        "cree un niveau"
        self.on = 1
        self.menu = menu
        self.matrice = self.generer_matrice(chemin_fichier)
        self.img_background = pygame.image.load(chemin_background).convert_alpha()
        self.img_fleche_left = pygame.image.load(chemin_fleche_left).convert_alpha()
        self.img_fleche_right = pygame.image.load(chemin_fleche_right).convert_alpha()
        self.img_fleche_up = pygame.image.load(chemin_fleche_up).convert_alpha()
        self.img_fleche_down = pygame.image.load(chemin_fleche_down).convert_alpha()
        self.img_entree = pygame.image.load(chemin_entree).convert_alpha()
        self.img_sortie = pygame.image.load(chemin_sortie).convert_alpha()
        self.img_bloc = pygame.image.load(chemin_bloc).convert_alpha()
        self.img_bloc1 = pygame.image.load(chemin_bloc1).convert_alpha()
        self.img_bloc2 = pygame.image.load(chemin_bloc2).convert_alpha()
        self.img_bloc3 = pygame.image.load(chemin_bloc3).convert_alpha()
        self.img_chest = pygame.image.load(chemin_chest).convert_alpha()
        self.img_pics = pygame.image.load(chemin_pics).convert_alpha()
        self.taille_bloc = self.img_bloc.get_rect().size
        self.surface = self.generer_surface()
        self.compteur_affichage = 0
        self.position_initiale = self.definir_position("e")
        self.personnage = Personnage(self)
        self.generer_dict_positions_blocs()
        self.gravity = "down"
        self.gx = 0
        self.gy = gravity

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
        "cree le dictionnaire des positions des blocs de chaque type"
        self.dict_positions_blocs = dict()
        for bloc_type in liste_blocs:
            self.dict_positions_blocs[bloc_type] = self.generer_positions_blocs(bloc_type)

    def generer_surface(self):
        "genere une surface avec tous les blocs du niveau"
        self.surface = pygame.Surface((window_width, window_height))
        self.surface.blit(self.img_background, (0, 0))
        for i in range(len(self.matrice)):
            for j in range(len(self.matrice[0])):
                if self.matrice[i][j] == 'b' :
                    n = randint(1,100)
                    if n <= 3:
                        self.surface.blit(self.img_bloc1, (j * self.taille_bloc[0], i * self.taille_bloc[1]))
                    elif False:
                        self.surface.blit(self.img_bloc2, (j * self.taille_bloc[0], i * self.taille_bloc[1]))
                    elif False:
                        self.surface.blit(self.img_bloc3, (j * self.taille_bloc[0], i * self.taille_bloc[1]))
                    else:
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
                if self.matrice[i][j] == 'c' :
                    self.surface.blit(self.img_chest, (j * self.taille_bloc[0], i * self.taille_bloc[1]))
                if self.matrice[i][j] == 'p' :
                    self.surface.blit(self.img_pics, (j * self.taille_bloc[0], i * self.taille_bloc[1]))
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
        "gere la condition de victoire"
        if self.personnage.est_dans_un_bloc("s"):
            print("you win")
            self.menu.next_niveau += 1
            self.on = 0

    def switch_gravity(self):
        "gere le passage dans des blocs inverseurs de gravite"
        if self.personnage.est_dans_un_bloc("u"):
            self.gravity = "up"
            self.gy = -gravity
            self.gx = 0
        if self.personnage.est_dans_un_bloc("d"):
            self.gravity = "down"
            self.gy = gravity
            self.gx = 0
        if self.personnage.est_dans_un_bloc("l"):
            self.gravity = "left"
            self.gx = -gravity
            self.gy = 0
        if self.personnage.est_dans_un_bloc("r"):
            self.gravity = "right"
            self.gx = gravity
            self.gy = 0

    def boucle_evenement(self):
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                self.on, self.menu.on = 0, 0
            else:
                self.personnage.controler(event)

    def boucle_principale(self):
        while self.on:
            pygame.time.Clock().tick(70)
            self.boucle_evenement()
            self.personnage.PFD()
            self.personnage.vous_ne_passerez_pas()
            #self.personnage.rebondis()
            self.afficher()
            self.personnage.die()
            self.switch_gravity()
            self.win()
