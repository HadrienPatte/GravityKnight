def contact(M, perso_x, perso_y):
    '''indique s'il y a contact avec un bloc'''
    for k in range len(M):
        #dessus et dessous:
        if perso_x >= M[k][0] and perso_x <= M[k][0] + taille_bloc:

            #dessus:
            if perso_y >= M[k][1] - marge and perso_y <= M[k][1] + marge:
                y[0], y[1] = M[k][1], M[k][1] #on force le perso à rester juste au dessus du bloc(mettre perso_y au lieu de y j'me rappelle plus lequel c'est
                if vy[1] <= 0: #mettre 'or vy[0] <= 0' ausi si besoin
                    vy[0], vy[1] = 0, 0 #on met les vitesses a zéro pour le PFD
                    saut_autorise = 'haut' #on indique où le perso a le droit de sauter
                    f = f_solide

            #dessous:
            if perso_y >= M[k][1] - taille_bloc - marge and perso_y <= M[k][1] - taille_bloc + marge:
                y[0], y[1] = M[k][1] - taille_bloc, M[k][1] - taille_bloc #on force le perso à rester juste en dessous du bloc(mettre perso_y au lieu de y j'me rappelle plus lequel c'est
                if vy[1] >= 0 :
                    vy[0], vy[1] = 0, 0 #on met les vitesses a zéro pour le PFD
                    saut_autorisé = 'bas'
                    f = f_solide

        #gauche et droite:
        if perso_y <= M[k][1] and perso_y >= M[k][1] - taille_bloc:

            #gauche:
            if perso_x >= M[k][0] - marge and perso_x <= M[k][0] + marge:
                x[0], x[1] = M[k][0], M[k][0] #on force le perso à rester juste à gauche du bloc(mettre perso_y au lieu de y j'me rappelle plus lequel c'est
                if vx[1] >= 0:
                    vx[0], vx[1] = 0, 0 #on met les vitesses a zéro pour le PFD
                    saut_autorise = 'gauche'
                    f = f_solide

            #droite:
            if perso_x >= M[k][0] + taille_bloc - marge and perso_x <= M[k][0] + taille_bloc + marge:
                x[0], x[1] = M[k][0] + taille_bloc, M[k][0] + taille_bloc  #on force le perso à rester juste à droite du bloc(mettre perso_y au lieu de y j'me rappelle plus lequel c'est
                if vx[1] <= 0:
                    vx[0], vx[1] = 0, 0
                    saut_autorise = 'droite'
                    f = f_solide

return(saut_autorise, f) #voir si ça marche (global ou local)