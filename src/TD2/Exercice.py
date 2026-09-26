#Calculez la complexité C(n) de l’algorithme find(T,x)
# permettant de retourner l’indice de l’élément x dans un tableau T de taille n.
# Les éléments ne sont pas triés et sont sans répétition.
# L’algorithme termine par l’affichage de l’indice de l’élément s’il existe, sinon il affiche -1.
# Trouvez aussi l’ordre de grandeur de cet algorithme.

def find_v1(values, element):
    for i, e in zip(range(len(values)), values):
        if e == element:
            return i
    return -1
#Pour chaque cas ci-dessous, trouvez une fonction g(x), la plus simple possible, telle que f(x) ∈ O(g(x)).
#f(x) = 4x2 +3x+7+ 6*3x +5log(x)
# -> g(x) = 3x
#f(n) = (14n+3)log(n) +3n2
# -> g(x) = n2
#f(x) = x2 +5x
# -> g(x) = 5x
#f(x) = SquareRoot(7)x6 +7x5 +πx3 −194x2 −2112
# ->  g(x) = x6

#Étant donné un ensemble d’éléments (tableau, liste ou toute autre structure collective de votre choix),
# écrivez un algorithme permettant de trouver l’ensemble des éléments uniques qui lui correspond (en éliminant les doublons possibles).
# Pour ce faire utilisez deux ensembles, l’ensemble en entrée et un ensemble secondaire pour les uniques.
#Question: Codez en Python les deux algorithmes ci-dessous et trouvez le nombre d’opération et l’ordre de grandeur de chaque algorithme.
#Méthode 1: On constitue une liste de sortie qui contiendra les éléments uniques déjà rencontrés et qui est initialement vide.
# On parcourt la liste donnée en entrée,
# et pour chaque élément, on regarde s'il déjà est présent dans la liste de sortie
# (on peut utiliser pour cela un autre algorithme qui teste la présence d’un élément dans une liste).
# Si l’élément n’est pas présent dans la liste de sortie, on le rajoute à cette liste,
# sinon on passe à l’élément suivant. À la fin du parcours,
# la liste de sortie contient tous les éléments uniques de la liste d’entrée.

def exist(values, element):
    for e in values:
        if e == element:
            return True
    return False

def remove_duplicates_v1(values):
    result = []
    for value in values:
        if not exist(result, value):
            result.append(value)
    return result

#On appelle tableau de classement trié tout tableau d’entiers positifs {T[i]}i = 1n tel que:
#T[1] = 1 (Note premier élément du tableau est d’indice 1)
#Pour tout i < n, T[i] ≤ T[i + 1], autrement dit T est un tableau trié
#Pour tout i ≤ n, T[i] ≤ i
#Un tableau sera dit tableau de classement lorsque Sort(T) est un tableau de classement trié,
# la fonction Sort étant une méthode de tri quelconque.
# Par exemple, le tableau (1, 2, 2, 2, 5, 6, 6, 8) est un tableau de classement trié,
# et (6, 8, 2, 1, 2, 6, 2, 5) est un tableau de classement.
#Ecrire un algorithme check_array_v1(T) qui teste si un tableau est un tableau de classement trié.
# Calculer sa complexité. La méthode consiste à parcourir le tableau
# et à vérifier les conditions ci-dessus.

def check_array_v1(values):
    if values[0] !=1:
        return False
    for i in range(2,len(values)):
        print(i,values[i],values[i-1])
        if values[i] < values[i-1] or (values[i]> i+1):
            return False
    return True
#Cet algorithme a une complexité linéaire O(n)

#En déduire la complexité de l’algorithme check_array_v2(T) qui consiste tout d’abord
# à trier le tableau T puis lui appliquer la procédure check_array_v1(T)

def check_array_v2(values):
    sort_selection(values)
    print(check_array_v1(values))

def sort_selection(values):
    for i in range(len(values)):
        min_index = i
        for j in range(i+1,len(values)):
            if values[min_index] > values[j]:
                min_index = j
        values[i], values[min_index] = values[min_index], values[i]

#Cet algorithme a une complexité quadratique O(n2), car n2 domine né