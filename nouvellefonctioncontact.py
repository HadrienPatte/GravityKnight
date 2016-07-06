def contact(M, perso_x, perso_y,x,y,vx,vy,f, taille_bloc = 40, marge = 10):
    '''indique s'il y a contact avec un bloc'''
    saut_autorise =0
    for k in range(len(M)):
        #dessus et dessous:
        if perso_x > M[k][0] and perso_x <= M[k][0] + taille_bloc:

            #dessus:
            if perso_y + 40 > M[k][1] - marge and perso_y <= M[k][1] + marge:
                y[0], y[1] = M[k][1] + 40, M[k][1] + 40 #on force le perso  rester juste au dessus du bloc(mettre perso_y au lieu de y j'me rappelle plus lequel c'est
                if vy[1] <= 0: #mettre 'or vy[0] <= 0' ausi si besoin
                    vy[0], vy[1] = 0, 0 #on met les vitesses a zro pour le PFD
                    saut_autorise = 'haut' #on indique o le perso a le droit de sauter
                    f = f_solide
                    return(x[0], x[1], y[0], y[1], vx[0], vx[1], vy[0], vy[1], saut_autorise, f)

            #dessous:
            if perso_y > M[k][1] - taille_bloc - marge and perso_y <= M[k][1] - taille_bloc + marge:
                y[0], y[1] = M[k][1] - taille_bloc, M[k][1] - taille_bloc #on force le perso  rester juste en dessous du bloc(mettre perso_y au lieu de y j'me rappelle plus lequel c'est
                if vy[1] > 0 :
                    vy[0], vy[1] = 0, 0 #on met les vitesses a zro pour le PFD
                    saut_autorise = 'bas'
                    f = f_solide
                    return(x[0], x[1], y[0], y[1], vx[0], vx[1], vy[0], vy[1], saut_autorise, f)

        #gauche et droite:
        if perso_y <= M[k][1] and perso_y > M[k][1] - taille_bloc:

            #gauche:
            if perso_x + 40 > M[k][0] - marge and perso_x <= M[k][0] + marge:
                x[0], x[1] = M[k][0] + 40, M[k][0] + 40 #on force le perso  rester juste  gauche du bloc(mettre perso_y au lieu de y j'me rappelle plus lequel c'est
                if vx[1] > 0:
                    vx[0], vx[1] = 0, 0 #on met les vitesses a zro pour le PFD
                    saut_autorise = 'gauche'
                    f = f_solide
                    return(x[0], x[1], y[0], y[1], vx[0], vx[1], vy[0], vy[1], saut_autorise, f)

            #droite:
            if perso_x > M[k][0] + taille_bloc - marge and perso_x <= M[k][0] + taille_bloc + marge:
                x[0], x[1] = M[k][0] + taille_bloc, M[k][0] + taille_bloc  #on force le perso  rester juste  droite du bloc(mettre perso_y au lieu de y j'me rappelle plus lequel c'est
                if vx[1] <= 0:
                    vx[0], vx[1] = 0, 0
                    saut_autorise = 'droite'
                    f = f_solide
                    return(x[0], x[1], y[0], y[1], vx[0], vx[1], vy[0], vy[1], saut_autorise, f)

    return(x[0], x[1], y[0], y[1], vx[0], vx[1], vy[0], vy[1], saut_autorise, f)
