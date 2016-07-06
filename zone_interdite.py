def interdit_bloc(x, y) :
    'prends des coordonnées en parmètres et renvoie la liste des points des bords du bloc'
    L = []
    for i in range(40) :
        L = L + [(x + i, y)]
    
        L = L + [(x, y + i)]

        L = L + [(x + 39, y + i)]
        L = L + [(x + i, y + 39)]
    return(L)

def zone_interdite(M) :
    'prends une matrice de niveau en paramètre et renvoie la liste des points interdits'
    zone = []
    for i in range(len(M)) :
        for j in range(len(M[0])) :
            if M[i][j] == 'b' :
                zone = zone + interdit_bloc(i * 40, j * 40)

    return(zone) #renvoie UNE liste de tupleS


def interdit_bloc_direction(x, y) :
    'même chose, mais avec la direction interdite'
    L = []
    for i in range(40) :
        L = L + [(x + i, y, 'gauche')]
    
        L = L + [(x, y + i, 'bas')]

        L = L + [(x + 39, y + i, 'haut')]
        L = L + [(x + i, y + 39, 'droite')]
    return(L)

def zone_interdite_direction(M) :
    'meme chose, mais avec une matrice de niveau'
    zone_dir = []
    for i in range(len(M)) :
        for j in range(len(M[0])) :
            if M[i][j] == 'b' :
                zone_dir = zone_dir + interdit_bloc_direction(i * 40, j * 40)

    return(zone_dir) #renvoie UNE liste de tupleS
