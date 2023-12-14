from orderedlinkedlist import OrderedLinkedList

class Classement :
    def __init__(self, list=[]):
        """
        Initialise Classement
        @pre: Prend éventuellement une liste si déjà une liste présente
        @post: /
        """
        self.__resultats = OrderedLinkedList(list)
        self.__size = self.__resultats.size()

    def size(self):
        """
        Retourne la longueur de la liste
        @pre: /
        @post: Retourne la longueur (type: int)
        """
        return self.__size

    def add(self,r):
        """ 
        Ajoute un coureur dans la liste et le met au bon endroit selon son temps (ordre croissant)
        @pre:  prend le résultat du coureur (type: Resultat)
        @post: /
        """
        self.__size += 1
        self.__resultats.add(r)

    def get(self,c):
        """
        Retourne le résultat d'un coureur donné.
        @pre: prend un coureur en paramètre (type: Coureur)
        @post: retourne le premier (meilleur) Resultat r du coureur c dans le
              classement. Retourne None si le coureur ne figure pas (encore)
              dans le classement.
        """
        return self.__resultats.get_node(c)

    def get_position(self,c):
        """
        Retourne la meilleure position d'un coureur dans ce classement.
        @pre: prend un coureur en paramètre (type: Coureur)
        @post: retourne un entier représentant la position du coureur c dans ce classement,
              à partir de 1 pour la tête de ce classement. Si le coureur figure plusieurs fois
              dans le classement, la première (meilleure) position est retournée.
              Retourne -1 si le coureur ne figure pas dans le classement.
        """
        position = self.__resultats.search(c)
        return position

    def remove(self,c):
        """
        Retire un résultat du classement.
        @pre: prend un coureur en paramètre (type: Coureur)
        @post: retire le premier (meilleur) résultat pour le coureur c du classement.
              c est comparé au sens de __eq__. Retourne c si un résultat a été retiré,
              of False si c n'est pas trouvé dans la liste.
        """
        self.__size -= 1
        return self.__resultats.remove(c)

    def __str__(self):
        """
        Retourne une représentation string de cet objet.
        @pre: /
        @post: Retourne une représentation de ce classement sous forme d'un string,
               avec une ligne par résultat.
        """
        return self.__resultats.print()