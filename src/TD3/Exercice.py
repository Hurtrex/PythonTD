#Étant donnée la fonction itérative ci-dessous. Transformer la en une fonction récursive.
def count_iterative(limit : int):
    for i in range(limit):
        print(i)

def count_recursive(limit : int, counter: int):
    print(counter)
    if counter < limit-1:
        count_recursive(limit, counter+1)

#Transformer les deux boucles imbriquées ci-dessous en une fonction récursive
def mult_tab_iterative(limitfori: int,limitforj: int):
    for i in range(limitfori):
        for j in range(limitforj):
            print(f"{i} * {j} = {i * j}")

def mult_tab_recursive(limitfori: int,limitforj: int,i,j):
    if i < limitfori:
        if j < limitforj:
            print(f"{i} * {j} = {i * j}")
            mult_tab_recursive(limitfori,limitforj,i,j+1)
        else:
            mult_tab_recursive(limitfori, limitforj, i+1, j )

#Écrire une fonction Python permettant d’inverser une chaine de caractère.
def reverse_iterative(message, str):
    result: str = ""
    for char in message:
        result += char
    return result
def reverse_recursive(message: str):
    if len(message) == 0:
        return message
    else:
        return reverse_recursive(message[1:]) + message[0]

#Écrire une fonction en Python permettant de compter la longueur d’une chaine de caractère de façon récursive.

def lenght_recursive(message: str):
    if len(message) == 0:
        return 0
    else:
        return lenght_recursive(message[1:]) + 1

#La recherche d’une valeur particulière dans un tableau ordonné se fait par divisions successives du tableau en deux parties. Le fait que le tableau soit ordonné permet de déterminer rapidement la moitié dans laquelle se trouve l’élément recherché.
# Traduire l’algorithme de recherché binaire ci-dessous en un programme Python :
# Programmation non recursive
# Programmation récursive

def binary_search_iterative(values,start,end,key):
    i: int = start - 1
    j: int = end + 1
    while not i+1 ==j:
        middle = (i+j) // 2
        if key < values[middle]:
            j = middle
        if key == values[middle]:
            return middle
        if key > values[middle]:
            i = middle
    return -1
def binary_search_recursive(values,start,end,key):
    if end >= start:
        middle = (start + end) // 2
        if values[middle] == key:
            return middle
        elif values[middle] > key:
            return binary_search_recursive(values,start,middle,key)
        else:
            return binary_search_recursive(values,middle+1,end,key)
    else:
        return -1