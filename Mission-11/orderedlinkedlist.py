from resultat import Resultat

class Node:
        def __init__(self, cargo=None, next=None):
            self.__cargo = cargo
            self.__next  = next

        def value(self):
            return self.__cargo

        def next(self):
            return self.__next

        def set_next(self,node):
            self.__next = node
    
        def __str__(self):
            return str(self.value())
    
        def __eq__(self,other):
            if other is not None :
                return self.value() == other.value()
            else :
                return False

        def print_list(self):
            head = self
            tail = self.__next
            if tail is not None :
                print(head, end=" ")
                tail.print_list()
            else :
                print(head, end=" ")

        def print_backward(self):
            head = self
            tail = self.__next
            if tail is not None :
                tail.print_backward()
            print(head, end = " ")

        def print_avec_separateur(self, separateur):
            print("[", end=" ")
            if self.first() is not None:
                self.head.print_list_avec_separateur(separateur)
            print("]")

        def print_list_avec_separateur(self,separateur):
            head = self
            tail = self.__next
            if tail is not None :
                print(head, end=separateur)
                tail.print_list_avec_separateur(separateur)
            else:
                print(head, end=" ")

class OrderedLinkedList :
    def __init__(self, lst=[]): # Prend en charge le fait de recevoir éventuellement une liste avec de résultats
        """
        Initialise LinkedList
        @pre: Prend éventuellement une liste si déjà une liste présente
        @post: /
        """
        self.__length = 0
        self.__head = None
        for resultat in lst:
            self.add(resultat)
            
    def size(self):
        """
        Retourne la longueur de la liste
        @pre: /
        @post: Retourne la longueur (type: int)
        """
        return self.__length
    
    def inc_size(self):
        """
        Ajoute 1 à la variable 'longueur' de la liste
        @pre: /
        @post: /
        """
        self.__length += 1

    def dec_size(self):
        """
        Enlève 1 à la variable 'longueur' de la liste
        @pre: /
        @post: /
        """
        self.__length -= 1

    def first(self):
        """
        Récupère le coureur en première place
        @pre: /
        @post: retourne le coureur (type: Node)
        """
        return self.__head
    
    def set_first(self,n):
        """
        Prend un coureur et le met en première place
        @pre: prend le noeud (type: Node)
        @post: /
        """
        self.__head = n

    def search(self, c):
        """
        Cherche la place d'un coureur dans le classement
        @pre: prend le coureur (type: Coureur)
        @post: retourne sa place (type: int)
        """
        pointer = self.first()
        if pointer == None:
            return -1
        count = 1
        while pointer.value().coureur() != c:
            count += 1
            if pointer.next() == None:
                return -1
            pointer = pointer.next()
        return count
        
    def add(self, r):
        """ 
        Ajoute un coureur dans la liste et le met au bon endroit selon son temps (ordre croissant)
        @pre:  prend le résultat du coureur (type: Resultat)
        @post: /
        """
        if not isinstance(r, Resultat): # Vérifie si r est bien un résultat
            raise ValueError("OrderedLinkedList ne prend en charge seulement des données de type Resultat")
        pointer = self.first()
        if pointer == None: # Si il n'y a pas de noeuds, alors il crée le premier
            self.set_first(Node(r))
            self.inc_size()
            return
        else:
            if r < pointer.value(): # Si le temps est meilleur que le premier, il le met devant
                self.set_first(Node(r, pointer))
                self.inc_size()
                return
            while True: # While qui ne s'arrête seulement si un coureur plus grand que r est trouvé
                if pointer.next() == None: # S'il n'y a pas de noeud suivant, alors il place le coureur en dernier
                    pointer.set_next(Node(r))
                    self.inc_size()
                    break
                if r < pointer.next().value(): # Si le suivant est plus grand, alors il se met avant lui
                    pointer.set_next(Node(r, pointer.next()))
                    self.inc_size()
                    break
                pointer = pointer.next() # Passe le pointeur au noeud suivant


    def print(self):
        """
        Renvoie sous forme de chaine de caractère la liste des classements
        @pre: /
        @post: Retourne une chaine de caractère avec le nom du coureur, son temps et son numéro de classement tel que:
            1> Glineur: 00:05:30
            2> Remacle: 10:10:55
        """
        s = ""
        pointer = self.first()
        if pointer == None:
            return ""
        classement = 1
        while True:
            if pointer == None:
                break
            s += str(classement) + "> " + pointer.value().coureur().nom() + ": " + str(pointer.value().temps()) + "\n"
            pointer = pointer.next()
            classement += 1
        if s == "":
            return "[Classement vide]"
        return s

    def get_node(self, c):
        """
        Récupère le résultat du nème coureur
        @pre: numéro de classement (type: int)
        @post: retourne le résultat du coureur (type: Resultat)
        """
        n = self.search(c)
        pointer = self.first()
        if pointer == None or n == -1: # Si il n'y a pas de premier coureur ou pas dans la liste, ne cherche pas
            return
        for _ in range(n-1): # Fais autant de next pour arriver au coureur 
            pointer = pointer.next()
        return pointer.value() # Retourne le coureur

    def remove(self, c):
        """
        Supprime complètement un coureur du classement
        @pre: prend un coureur (type: Coureur)
        @post: /
        """
        pointer = self.first()
        if pointer == None: # Si le classement est vide
            return
        elif pointer.value().coureur() == c and pointer.next() == None: # Si le coureur à supprimer est le seul dans le classement
            self.set_first(None)
            self.dec_size()

        while pointer.next() != None: # Si il existe des coureurs après le premier
            if pointer.next().value().coureur() == c: # Si le coureur suivant est égal au coureur à supprimer
                if pointer.next().next() != None: # Si il existe un coureur deux places après
                    pointer.set_next(pointer.next().next()) # Il passe alors le coureur suivant
                    self.dec_size()
                else:
                    pointer.set_next(None) # S'il n'existe pas de coureur deux places après il place juste le next à None
                    self.dec_size()
                    return
            pointer = pointer.next() # Il avance pointer de une place
            if pointer == None: # Check si le pointeur existe encore
                return