def contact(M, perso_x, perso_y,liste):
    '''indique s'il y a contact avec un bloc'''
    taille_bloc = 40
    marge = 5
    saut_autorise = 'non'
    for coordonnees in liste:
        #dessus et dessous:
        if perso_x >= coordonnees[0] and perso_x <= coordonnees[0] + taille_bloc:

            #dessus:
            if perso_y >= coordonnees[1] - marge and perso_y <= coordonnees[1] + marge:
                y[0], y[1] = coordonnees[1], coordonnees[1] #on force le perso  rester juste au dessus du bloc(mettre perso_y au lieu de y j'me rappelle plus lequel c'est
                if vy[1] <= 0: #mettre 'or vy[0] <= 0' ausi si besoin
                    vy[0], vy[1] = 0, 0 #on met les vitesses a zro pour le PFD
                    saut_autorise = 'haut' #on indique o le perso a le droit de sauter
                    f = f_solide

            #dessous:
            if perso_y >= coordonnees[1] - taille_bloc - marge and perso_y <= coordonnees[1] - taille_bloc + marge:
                y[0], y[1] = coordonnees[1] - taille_bloc, coordonnees[1] - taille_bloc #on force le perso  rester juste en dessous du bloc(mettre perso_y au lieu de y j'me rappelle plus lequel c'est
                if vy[1] >= 0 :
                    vy[0], vy[1] = 0, 0 #on met les vitesses a zro pour le PFD
                    saut_autorise = 'bas'
                    f = f_solide

        #gauche et droite:
        if perso_y <= coordonnees[1] and perso_y >= coordonnees[1] - taille_bloc:

            #gauche:
            if perso_x >= coordonnees[0] - marge and perso_x <= coordonnees[0] + marge:
                x[0], x[1] = coordonnees[0], coordonnees[0] #on force le perso  rester juste  gauche du bloc(mettre perso_y au lieu de y j'me rappelle plus lequel c'est
                if vx[1] >= 0:
                    vx[0], vx[1] = 0, 0 #on met les vitesses a zro pour le PFD
                    saut_autorise = 'gauche'
                    f = f_solide

            #droite:
            if perso_x >= coordonnees[0] + taille_bloc - marge and perso_x <= coordonnees[0] + taille_bloc + marge:
                x[0], x[1] = coordonnees[0] + taille_bloc, coordonnees[0] + taille_bloc  #on force le perso  rester juste  droite du bloc(mettre perso_y au lieu de y j'me rappelle plus lequel c'est
                if vx[1] <= 0:
                    vx[0], vx[1] = 0, 0
                    saut_autorise = 'droite'
                    f = f_solide

    return(saut_autorise, f) #voir si a marche (global ou local)
