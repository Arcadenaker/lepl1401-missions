# Fonction pour lire un fichier et créer une liste de lignes
def readfile(filename):
    """ Crée une liste des lignes contenues dans un fichier dont le nom est ``filename``

    Args:
        filename: le nom d'un fichier de texte
    Retourne:
        une liste dans laquelle chaque ligne du fichier filename est un élément.
        Si filename n'existe pas, la fonction retourne une liste vide.
    """
    lines = []
    try:
        # Ouvre le fichier en mode lecture et lit toutes les lignes
        file = open(filename, "r", encoding="utf-8").readlines()
        # Supprime les espaces blancs autour de chaque ligne et ajoute à la liste
        lines = [line.strip() for line in file]
        return lines
    except:
        return lines
    
# Fonction pour extraire les mots d'une ligne
def get_words(line):
    """ pour une chaîne de caractères donnée, retourne une liste des mots dans la chaîne,
        en minuscules, et sans ponctuation, dans l'ordre d'apparence dans le texte.
        Par exemple, pour la chaîne de caractères

        "Turmoil has engulfed the Galactic Republic. The taxation of trade routes
        to outlying star systems is in dispute."

        Le résultat est

        ["turmoil", "has", "engulfed", "the", "galactic", "republic", "the",
        "taxation", "of", "trade", "routes", "to", "outlying", "star", "systems",
        "is", "in", "dispute" ]

        Un caractère est considéré comme une ponctuation si ce n'est pas une
        lettre, selon la fonction string.isalpha () .

    Args:
        line: une chaîne de caractères.
    Retourne:
        une liste des mots dans la chaîne, en minuscules, et sans ponctuation.
    """
    try:
        # Liste des mots en minuscule sans ponctuation
        line = line.lower().split()
        # Liste des mots en sortie
        words = []
        # Pour chaque mot dans line
        for word in line:
            # Variable temporaire qui enregistre 
            # les lettres une par une
            temp_word = ""
            # Pour chaque lettre dans mot
            for letter in word:
                # Si c'est bien une lettre de l'alphabet
                if letter.isalpha() or letter.isnumeric():
                    # Il le rajoute dans temp_word
                    temp_word += letter
            # Il rajoute le mot trié dans words
            if temp_word != "":
                words.append(temp_word)
        return words
    except Exception as e:
        print(e)
        # Retourne un tableau vide si une erreur s'est produite
        return []

# Fonction pour créer un index de mots
def create_index(filename):
    """ crée un index pour le fichier avec nom ``filename``. L'index se compose
        d'un dictionnaire dans lequel pour chaque mot du fichier ``filename``
        on retrouve une liste des indices des lignes du fichier qui contiennent
        ce mot.

        Par exemple, pour un fichier avec le contenu suivant:

          While the Congress of the Republic endlessly debates
          this alarming chain of events, the Supreme Chancellor has
          secretly dispatched two Jedi Knights.

        Une partie de l'index, representé comme dictionnaire, est:


          {"while": [0], "the": [0,1], "congress": [0], \
           "of": [0,1], "republic": [0], ... , "jedi": [2], ...}

    Args:
        filename: une chaîne de caractères
    Retourne:
        un dictionnaire avec pour chaque mot du fichier (en minuscules)
        la liste des indices des lignes qui contiennent ce mot.
    """
    lines = readfile(filename)
    words = [get_words(line) for line in lines]
    index = {}
    line_index = 0
    for line in words:
        for word in line:
            if word in index:
                if not line_index in index[word]:
                    index[word].append(line_index)
            else:
                index[word] = [line_index]
        line_index += 1
    return index

# Fonction pour obtenir les lignes contenant certains mots
def get_lines(words, index):
    """ Détermine les lignes qui contiennent tous les mots indexes dans ``words``,
        selon l'index ``index``.

        Par exemple, pour l'index suivant:

            index = {"while": [0], "the": [0,1], "congress": [0], \
                    "of": [0,1], "republic": [0], ... , "jedi": [2], ...}

        La fonction retourne
            get_lines(["the"]) -> [0,1]
            get_lines(["jedi"]) -> [2]
            get_lines(["the","of"],index) -> [0,1]
            get_lines(["while","the"],index) -> [0]
            get_lines(["congress","jedi"]) -> []
            get_lines(["while","the","congress"]) -> [0]

    Args:
        words: une liste de mots, en minuscules
        index: un dictionnaire contenant pour mots (en minuscules) des listes de nombres entiers
    Retourne:
        une liste des nombres des lignes contenant tous les mots indiqués
    """
    # Liste qui contient toutes les lignes
    unique_occurrence = []
    # Pour tous les mots
    for word in words:
        # Si il est dans l'index
        if word in index:
            if unique_occurrence == []:
                for i in index[word]:
                    unique_occurrence.append(i)
            else:
                for occ in unique_occurrence:
                    if not occ in index[word]:
                        unique_occurrence.remove(occ)
    return unique_occurrence