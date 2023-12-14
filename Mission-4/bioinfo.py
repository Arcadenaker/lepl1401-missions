def is_adn(s):
    """
    Vérifie si une chaîne de caractères est constituée uniquement des bases d'ADN (A, T, C, G).

    Pré:
        s (str): La chaîne de caractères à vérifier.

    Post:
        bool: True si la chaîne est de l'ADN, False sinon.
    """
    # Vérifie si la chaîne n'est pas vide
    if s == "":
        return False
    # Convertit la chaîne en minuscules pour une comparaison insensible à la casse
    s_lower = s.lower()
    # Liste des caractères autorisés dans une séquence ADN
    adn_characters = ['a', 't', 'c', 'g']
    # Vérifie chaque caractère dans la chaîne
    for char in s_lower:
        # Si le caractère n'est pas dans la liste des caractères ADN autorisés, retourne False
        if char not in adn_characters:
            return False
    # Tous les caractères sont valides, la chaîne est une séquence ADN
    return True

def positions(s, p):
    """
    Trouve les positions des occurrences d'une sous-chaîne dans une chaîne donnée.

    Pré:
        s (str): La chaîne principale.
        p (str): La sous-chaîne à rechercher.

    Post:
        list: Une liste des positions des occurrences de la sous-chaîne dans la chaîne principale.
    """
    positions = []
    #Pour tout élément de s
    for skey in range(len(s)):
        #Vérifie si il est égal au premier élément de p
        if s[skey].lower() == p[0].lower():
            #Alors pour tous les éléments suivants
            for pkey in range(1,len(p)):
                #Il regarde si ils sont bons
                if s[skey+pkey].lower() != p[pkey].lower():
                    break
                #Si ils sont bons jusqu'à la fin de p alors il le rajoute à la liste
                if pkey == len(p)-1:
                    positions.append(skey)
    return positions

def distance_h(s1, s2):
    """
    Calcule la distance de Hamming entre deux chaînes de caractères de même longueur.

    Pré:
        s1 (str): Première chaîne.
        s2 (str): Deuxième chaîne.

    Post:
        int: La distance de Hamming entre les deux chaînes, ou None si les longueurs sont différentes.
    """
    #Si les deux chaines de caractères n'ont pas la même distance alors return
    if len(s1) != len(s2):
        return
    dist = 0
    for i in range(len(s1)):
        if s1[i].lower() != s2[i].lower():
            dist +=1
    return dist

def distances_matrice(liste_chaines):
    """
    Calcule une matrice des distances de Hamming entre toutes les paires de chaînes dans une liste.

    Pré:
        liste_chaines (list): Liste de chaînes de caractères.

    Post:
        list: Matrice des distances de Hamming entre toutes les paires de chaînes.
    """
    matrice = []
    #Pour tous les éléments de la liste il crée une ligne
    for i in range(len(liste_chaines)):
        #Il vide la liste "line"
        line = []
        #Pour tout élément dans la liste, il va comparer la différence entre chaque élément
        for u in range(len(liste_chaines)):
            line.append(distance_h(liste_chaines[i], liste_chaines[u]))
        matrice.append(line)
    return matrice

# Tests unitaires
def run_tests():
    assert is_adn("acgac") == True
    assert is_adn("AcaA") == True
    assert is_adn("aAaza") == False
    assert is_adn("aAaUza") == False
    assert is_adn("") == False

    assert positions("ACGACCG", "cg") == [1, 5]
    assert positions("ACGCGCGACCG", "cg") == [1, 3, 5, 9]

    assert distance_h("A", "A") == 0
    assert distance_h("AG", "GG") == 1
    assert distance_h("AG", "AT") == 1
    assert distance_h("ATGAC", "ATGAC") == 0
    assert distance_h("ATATA", "ATGAC") == 3
    assert distance_h("ATGAC", "AGGAG") == 2
    assert distance_h("ATGAC", "TGACG") == 5

    sequences = ["AG", "AT", "GT", "ACG", "ACT"]
    result = distances_matrice(sequences)
    expected = [
        [0, 1, 2, None, None],
        [1, 0, 1, None, None],
        [2, 1, 0, None, None],
        [None, None, None, 0, 1],
        [None, None, None, 1, 0]
    ]
    assert result == expected, f"Expected: {expected}, Got: {result}"
run_tests()