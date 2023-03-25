import math


def lire_instance(fichier):
    f=open("./Instances_genome/"+fichier, "r")
    taille_x = f.readline()
    taille_y = f.readline()
    x = f.readline()
    y = f.readline()
    x = x.split()
    y = y.split()
    f.close()
    return ("".join(x), "".join(y), taille_x, taille_y) #renvoi les mots x et y du fichier

c_del = 2 #cout de suppression
c_ins = 2 #cout d'insertion


""" cout_sub(a, b) = 0 si a = b,
cout_sub(a, b) = 3 si {a, b} est une paire concordante, c’est-à-dire {a, b} = {A,T} ou {a, b} = {G,C}, et
cout_sub(a, b)= 4 sinon.
"""
def cout_sub(a, b):
    if a == b:
        return 0
    if (a == 'A' and b == 'T') or (a == 'T' and b == 'A') or (a == 'G' and b == 'C') or (a == 'C' and b == 'G') :
        return 3
    return 4


def DIST_NAIF(x, y) :
    return DIST_NAIF_REC(x, y, 0, 0, 0, math.inf)


""" x et y deux mots,
i un indice dans [0..|x|], j un indice dans [0..|y|],
cout le coût de l’alignement de (x[1..i], y[1..j])
dist le coût du meilleur alignement de (x, y)
"""
def DIST_NAIF_REC (x, y, i, j, cout , dist) :
    if i == len(x) and j == len(y):
        if cout < dist :
            dist = cout
    else:
        if i < len(x) and j < len(y) :
            dist = DIST_NAIF_REC(x, y, i+1, j+1, cout+cout_sub(x[i], y[j]), dist)
        if i < len(x):
            dist = DIST_NAIF_REC(x, y, i+1, j, cout+c_del, dist)
        if j < len(y):
            dist = DIST_NAIF_REC(x, y, i, j+1, cout+c_ins, dist)
    return dist



def DIST_1(x,y):
    tab = []

    n = len(x) + 1
    m = len(y) + 1
    
    #initialisation tab[][] à 0
    for i in range(n):
        tab.append([0]*m)

    #initialisation des colonnes et des lignes d'indices [i][0] ou [0][i] dans le tab
    for i in range(1 , n):
        tab [i][0] = tab[i-1][0] + c_del #ligne D(i,0)
    for j in range(1 , m):
        tab [0][j] = tab[0][j-1] + c_ins #colonne D(0,j)
       
    for i in range(1, n):
        for j in range(1, m):
            h = tab[i-1][j] + c_del
            g = tab[i][j-1] + c_ins
            d = tab[i-1][j-1] + cout_sub(x[i-1],y[j-1])
            tab[i][j] = min(h, g, d)
    return (tab[n-1][m-1], tab)



def SOL_1(x,y,tab):
    S = "" #mot 1
    T = "" #mot 2
    i = len(x)
    j = len(y)
   
    while(i > 0 or j > 0):
        val_case = tab[i][j] #valeur de la case courante
        h = tab[i-1][j] # valeur de la case au dessus
        g = tab[i][j-1] # valeur de la case a gauche
        diag = tab[i-1][j-1] # valeur de la case en diagonale

        if val_case - diag == cout_sub(x[i-1],y[j-1]) :
            S = x[i-1] + S # concatener le caractere x[i-1] avec le chaine S
            T = y[j-1] + T # concatener le cracatere y[j-1] avec la chaine T
            i -= 1
            j -= 1
        elif(val_case - h == c_del):
            S = x[i-1] + S
            T = "-"+T # on ajoute un "-" en tête de T
            i -= 1
        elif(val_case - g == c_ins):
            S = "-"+S
            T = y[j-1] + T # concatener le caractere y[j-1] avec la chaine T
            j -= 1
    while i > 0 :
        S = "-"+S
        i -= 1
    while j > 0 :
        T = "-"+T
        j -= 1
    return (S,T)

def PROG_DYN(x,y):
    distance, tab = DIST_1(x,y)
    return distance, SOL_1(x,y, tab)

def DIST_2(x,y):
    n = len(x) + 1
    m = len(y) + 1
    #initialisation tab
    tab_1 = [0]*m
    tab_2 = [0]*m

    for j in range(1 , m):
        tab_1[j] = tab_1[j-1] + c_ins
       
    for i in range(1, n):
        tab_2[0] = tab_1[0] + c_del
        for j in range(1, m):
            h = tab_1[j] + c_del
            g = tab_2[j-1] + c_ins
            d = tab_1[j-1] + cout_sub(x[i-1],y[j-1])
            tab_2[j] = min(h, g, d)
        tab_1, tab_2 = tab_2, tab_1
   
    return (tab_1[m-1])

def mots_gap(k):
    return "-"*k

def align_lettre_mot(x,y):
    nb_gaps = 0
    c_min = cout_sub(x, y[0])
    m = len(y)
   
    for i in range(1, m):
        if c_min > cout_sub(x, y[i]) :
            c_min = cout_sub(x, y[i])
            nb_gaps = i

    return mots_gap(nb_gaps) + x + mots_gap(m-nb_gaps-1)


def coupure(x, y):
    """
    :param x: Un mot
    :param y: Un mot
    :return: le rang de la lettre a laquelle on doit couper y.
    """
    n = len(x)
    m = len(y)

    T = [[], []]  # Stock les distances
    col = [[], []]  # Stock la colonne d'origine sur la ligne i

    for j in range(0, m + 1):
        (T[0]).append(j * c_ins)  # Initialisation
        (T[1]).append(-1)  # Remplissage

        (col[0]).append(j)  # Initialisation
        (col[1]).append(-1)  # Remplissage

    for i in range(1, n // 2 + 1):
        T[1][0] = i * c_del
        for j in range(1, m + 1):
            T[1][j] = min([T[1][j - 1] + c_ins,
                           T[0][j] + c_del,
                           T[0][j - 1] + cout_sub(x[i - 1], y[j - 1])])
        T[0] = [c for c in T[1]]  # On veut eviter les effet de bords

    # On separe la boucle en deux pour eviter les tests et le stockage a chaque iteration.

    for i in range(n // 2 + 1, n + 1):
        T[1][0] = i * c_del
        for j in range(1, m + 1):
            # Calcul D(i,j)
            val1 = T[1][j - 1] + c_ins
            val2 = T[0][j] + c_del
            val3 = T[0][j - 1] + cout_sub(x[i - 1], y[j - 1])
            T[1][j] = min(val1, val2, val3)

            # Passage de la colonne d'origine
            if T[1][j] == val1:
                col[1][j] = col[1][j - 1]
            if T[1][j] == val2:
                col[1][j] = col[0][j]
            if T[1][j] == val3:
                col[1][j] = col[0][j - 1]

        T[0] = [c for c in T[1]]  # 

        col[0] = [c for c in col[1]]

    return col[0][m]



def SOL_2(x, y) :
    n = len(x) # longueur du mot x
    m = len(y) # longueur du mot y

    # cas de base
    if n == 0 :
        return mots_gap(m), y
    if m == 0 :
        return x, mots_gap(n)
    if n == 1 :
        return align_lettre_mot(x,y), y
    if m == 1 :
        return x, align_lettre_mot(y, x)

    mid = math.floor(n/2) # on coupe toujours le premier mot au milieu
    cut_y = coupure(x, y) # fonction coupure donne l'endroit optimal ou couper y

    s, t = SOL_2(x[:mid],y[:cut_y]) # sous-arbre gauche
    u, v = SOL_2(x[mid:],y[cut_y:]) # sous-arbre droit

    return (s+u, t+v) # mise en commun des deux sous-arbres
