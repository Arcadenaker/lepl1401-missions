class Article :
    def __init__(self,d,p):
        """
        @pre:  d un string décrivant l'article
               p un float représentant le prix HTVA en EURO d'un exemplaire de cet article 
        @post: Un article avec description d et prix p a été créé.
        Exemple: Article("carte graphique", 119.49)
        """
        self.__description = d
        self.__prix = p
        
    def description(self) :
        """
        @post: retourne la description textuelle décrivant l'article.
        """
        return self.__description

    def prix(self) :
        """
        @post: retourne le prix d'un exemplaire de cet article, hors TVA.
        """
        return self.__prix
        
    def taux_tva(self):
        """
        @post: retourne le taux de TVA (même valeur pour chaque article)
        """    
        return 0.21   # TVA a 21%

    def tva(self):
        """
        @post: retourne la TVA sur cet article
        """    
        return self.prix() * self.taux_tva()
 
    def prix_tvac(self):
        """
        @post: retourne le prix d'un exemplaire de cet article, TVA compris.
        """
        return self.prix() + self.tva()

    def __str__(self):
        """
        @post: retourne un string decrivant cet article, au format: "{description}: {prix}"
        """
        return "{0}: {1:.2f} EUR".format(self.description(), self.prix())

no_facture = 0

class Facture:
    nbr_art = 0
    nbr_art_tot = 0
    poids_tot = 0
    element_fragile = False
    def __init__(self, d, a_list):
        """
        @pre  d est un string court décrivant la facture;
              a_list est une liste d'objets de type Article.
        @post Une facture avec une description d et un liste d'articles a_list été crée.
        Exemple: Facture("PC Store - 22 novembre", [ Article("carte graphique", 119.49) ])
        """
        self.__description = d
        self.__articles = a_list
        
    def description(self) :
        """
        @post: retourne la description de cette facture.
        """
        return self.__description
    
    def __str__(self):
        """
        @post: retourne la représentation string d'une facture, à imprimer avec la méthode print() d'une instance Article/ArticlePiece.
        """
        s = self.entete_str()
        totalPrix = 0.0
        totalTVA = 0.0
        for art in self.__articles :
            s += self.article_str(art)
            totalPrix = totalPrix + art.prix()
            totalTVA = totalTVA + art.tva()
        s += self.totaux_str(totalPrix, totalTVA)
        return s

    def entete_str(self, bordereau=False):
        """
        @pre: art une instance de la classe Article ou ArticlePiece
        @post: retourne une représentation string de l'entête de la facture, comprenant le descriptif
               et les entêtes des colonnes.
        """
        global no_facture
        if not bordereau:
            return "Facture " + self.__description + "\n" \
                + self.barre_str() \
                + "| {0:<40} | {1:>10} | {2:>10} | {3:>10} |\n".format("Description","prix HTVA","TVA","prix TVAC") \
                + self.barre_str()
        else:
            no_facture += 1
            return "Livraison - Facture No " + str(no_facture) + " : " + self.__description + "\n" \
                + self.barre_str() \
                + "| {0:<40} | {1:>10} | {2:>10} | {3:>10} |\n".format("Description","poids/pce","nombre","poids") \
                + self.barre_str()

    def barre_str(self):
        """
        @post: retourne un string représentant une barre horizontale sur la largeur de la facture
        """
        barre_longeur = 83
        return "="*barre_longeur + "\n"

    def article_str(self, art, bordereau=False):
        """
        @pre:  art une instance de la classe Article ou ArticlePiece
        @post: retourne un string correspondant à une ligne de facture pour l'article art
        """
        if not bordereau:
            description = art.description()
            if type(art) == ArticlePiece:
                description = str(art.nombre())+" * "+description
            return "| {0:40} | {1:10.2f} | {2:10.2f} | {3:10.2f} |\n".format(description, art.prix(), art.tva(), art.prix_tvac())
        else:
            description = art.description()+""
            if art.piece().fragile():
                description = art.description()+" (!)"
                self.element_fragile = True
            poids_unitaire = art.piece().poids()
            self.nbr_art += art.nombre()
            self.poids_tot += art.nombre()*poids_unitaire
            self.nbr_art_tot += 1
            return "| {0:40} | {1:>10} | {2:>10} | {3:>10} |\n".format(description, str(poids_unitaire)+"kg", int(art.nombre()), str(round(art.nombre()*poids_unitaire,3))+"kg")

    def totaux_str(self, prix, tva, bordereau=False):
        """
        @pre:  art une instance de la classe Article ou ArticlePiece 
               prix un float représentant le prix total de la facture en EURO
               tva un float représentant le TVA total de la facture en EURO
        @post: retourne un string représentant une ligne de facture avec les totaux prix et tva,
               à imprimer en bas de la facture
        """
        if not bordereau:
            return self.barre_str() \
                + "| {0:40} | {1:10.2f} | {2:10.2f} | {3:10.2f} |\n".format("T O T A L", prix, tva, prix+tva) \
                + self.barre_str()
        else:
            nbr_articles = "{} article{}".format(self.nbr_art_tot, "s" if self.nbr_art_tot > 1 else "") 
            return self.barre_str() \
                + "| {0:40} | {1:10} | {2:>10} | {3:>10} |\n".format(nbr_articles, "", int(self.nbr_art), str(round(self.poids_tot,3))+"kg") \
                + self.barre_str() \
                + "{}".format("(!) *** livraison fragile ***\n" if self.element_fragile else "")
        
    def nombre(self, pce) :
        """
        @pre:  pce une instance de la classe Piece
        @post: retourne le nombre d'articles de type ArticlePiece dans la facture,
               faisant référence à une pièce qui est égale à pce,
               en totalisant sur tous les articles qui contiennent une telle pièce.
        """
        n=0
        for art in self.__articles:
            if art == pce:
                n+=1
        return n
    
    def print_livraison(self):
        """
        @post: retourne la représentation string d'une facture, à imprimer avec la méthode print() d'une instance Article/ArticlePiece.
        """
        s = self.entete_str(True)
        totalPrix = 0.0
        totalTVA = 0.0
        for art in self.__articles :
            s += self.article_str(art, True)
            totalPrix = totalPrix + art.prix()
            totalTVA = totalTVA + art.tva()
        s += self.totaux_str(totalPrix, totalTVA, True)
        return s

class ArticleReparation(Article):
    def __init__(self, duree):
        """
        @pre: prend la durée de réparation en paramètre
        """
        self.duree = duree

    def description(self):
        """
        @post: retourne la description de la réparation avec sa durée
        """
        return f"Reparation ({self.duree} heures)" 
    
    def prix(self):
        """
        @post: retourne le prix de la réparation
        """
        return 20 + 35 * self.duree
    
class ArticleReparationUrgente(ArticleReparation):
    def __init__(self, duree):
        """
        @pre: prend la duree de la reparation d'urgence
        """
        self.duree = duree

    def prix(self):
        """
        @post: retourne le prix de la réparation d'urgence (1.5x plus cher)
        """
        return super().prix() * 1.5
    
    def description(self):
        """
        @post: retourne la description de la réparation urgente avec sa durée
        """
        return f"Reparation URGENTE ({self.duree} heures)" 

class Piece():
    def __init__(self, d, prix, poids=0, fragile=False, TVA_reduit=False):
        """
        @pre:   prend une description de la piece
                prend le prix de la piece
                prend le poids de la piece qui est à 0kg par défaut
                prend un bool qui dit si la piece est fragile ou pas
                prend un bool qui dit si la piece a une reduction de tva
        """
        self.__description = d
        self.__prix = prix
        self.__poids = poids
        self.__fragile = fragile
        self.__TVA_reduit = TVA_reduit
    
    def description(self):
        """
        @post: retourne la description de la piece (str)
        """
        return self.__description
    
    def prix(self):
        """
        @post: retourne le prix de la piece (float)
        """
        return self.__prix
    
    def poids(self):
        """
        @post: retourne le poids de la piece (float)
        """
        return self.__poids
    
    def fragile(self):
        """
        @post: retourne un bool qui dit si le produit est fragile ou pas
        """
        return self.__fragile
    
    def tva_reduit(self):
        """
        @post: retourne un bool qui dit si le produit a une reduction de tva ou pas
        """
        return self.__TVA_reduit
    
    def __eq__(self, pce):
        """
        @post: retourne un bool qui dit si deux pièces sont égales ou pas à l'aide de la description et du prix
        """
        if self.prix() == pce.prix() and self.description() == pce.description():
            return True
        return False  

class ArticlePiece(Article):
    def __init__(self, n, pce):
        """
        @pre:   prend le nombre de pièces (float)
                prend la pièce (Piece)
        """
        self.__nbr = n
        self.__pce = pce

    def nombre(self):
        """
        @post: retourne le nombre de pièce (float)
        """
        return self.__nbr

    def piece(self):
        """
        @post: retourne la pièce (Piece)
        """
        return self.__pce
    
    def description(self):
        """
        @post: retourne une description du produit (str)
        """
        return f"{self.__pce.description()} @ {self.__pce.prix()}"
    
    def prix(self):
        """
        @post: retourne le prix total pour une piece (float)
        """
        return self.__pce.prix() * self.__nbr
    
    def taux_tva(self):
        """
        @post: retourne le taux de tva d'un produit
        """
        if self.__pce.tva_reduit():
            return 0.06
        return super().taux_tva()