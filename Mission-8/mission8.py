class Duree:
    def __init__(self,h,m,s):
        """
        @pre: h, m et s sont des entiers positifs (ou zéro)
            m et s sont < 60
        @post: Crée une nouvelle durée en heures, minutes et secondes.
        """
        if not 0 <= s < 60:
            m += s//60
            s %= 60
        if not 0 <= m < 60:
            h += m//60
            m %= 60
        self.heures = h
        self.minutes = m
        self.secondes = s

    def to_secondes(self):
        """
        @pre:  -
        @post: Retourne le nombre total de secondes de cette instance de Duree (self).
        Par exemple, une durée de 8h 41m 25s compte 31285 secondes.
        """
        return self.secondes + self.minutes*60 + self.heures*60**2
    
    def to_minutes(self):
        """
        @pre:  -
        @post: Retourne le nombre total de minutes de cette instance de Duree (self).
        Par exemple, une durée de 1h 41m 30s compte 101.5 minutes.
        """
        return self.secondes/60 + self.minutes + self.heures*60

    def delta(self,d) :
        """
        @pre:  d est une instance de la classe Duree
        @post: Retourne la différence en secondes entre cette durée (self)
            et la durée d passée en paramètre.
            Cette valeur renovoyée est positif si cette durée (self)
            est plus grand que la durée d, négatif sinon.
        Par exemple, si cette durée (self) est 8h 41m 25s (donc 31285 secondes)
        et la durée d est 0h 1m 25s, la valeur retournée est 31200.
        Inversement, si cette durée (self) est 0h 1m 25s et la durée
        d est 8h 41m 25s, alors la valeur retournée est -31200.
        """
        return self.to_secondes() - d.to_secondes()

    def apres(self,d):
        """
        @pre:  d est une instance de la classe Duree
        @post: Retourne True si cette durée (self) est plus grand que la durée
            d passée en paramètre; retourne False sinon.
        """
        return self.to_secondes() > d.to_secondes()

    def ajouter(self,d):
        """
        @pre:  d est une instance de la classe Duree
        @post: Ajoute une autre durée d à cette durée (self),
            corrigée de manière à ce que les minutes et les secondes soient
            dans l'intervalle [0..60[, en reportant au besoin les valeurs
            hors limites sur les unités supérieures
            (60 secondes = 1 minute, 60 minutes = 1 heure).
            Ne retourne pas une nouvelle durée mais modifié la durée self.
        """
        self.secondes += d.secondes
        self.minutes += d.minutes
        self.heures += d.heures
        if not 0 <= self.secondes < 60:
            self.minutes += self.secondes//60
            self.secondes %= 60
        if not 0 <= self.minutes < 60:
            self.heures += self.minutes//60
            self.minutes %= 60

    def __str__(self):
        """
        @pre:  -
        @post: Retourne cette durée sous la forme de texte "heures:minutes:secondes".
        Astuce: l'expression "{:02}:{:02}:{:02}".format(heures, minutes, secondes)
        retourne le string désiré avec les nombres en deux chiffres en ajoutant
        les zéros nécessaires.
        """
        return "{:02}:{:02}:{:02}".format(self.heures, self.minutes, self.secondes)

class Chanson:
    def __init__(self,t,a,d):
        """
        @pre:  t et a sont des string, d est une instance de la classe Duree
        @post: Crée une nouvelle chanson, caractérisée par un titre t,
                un auteur a et une durée d.
        """
        self.titre = t
        self.autheur = a
        self.duree = d
    def __str__(self):
        """
        @pre:  -
        @post: Retourne un string décrivant cette chanson sous le format
            "TITRE - AUTEUR - DUREE".
            Par exemple: "Let's_Dance - David_Bowie - 00:04:05"
        """
        return f"{self.titre} - {self.autheur} - {self.duree}"
    
class Album:
    def __init__(self, numero):
        """
        @pre:  numero est un entier identifiant de facon unique cet album
        @post: Crée un nouvel album, avec comme identifiant le numero,
            et avec une liste de chansons vide.
        """
        self.id = numero
        self.liste = []
        self.duree = Duree(0,0,0)

    def add(self, chanson):
        """
        Cette méthode retourne False et ne modifie rien si lors de l'ajout de la 
        chanson l'album aurait atteint 100 chansons ou sa durée aurait dépassé 75 minutes. 
        Sinon la chanson est rajoutée à la fin de la liste des chansons de cet album, 
        la durée totale de l'album est augmentée avec la durée de la chanson, et la méthode add retourne True.
        @pre:  prend la chanson à rajouter
        @post: Retourne True si la chanson bien rajoutée à la liste de l'album sinon retourne False
                (Dans le cas ou l'album dépasse 75 minutes)
        """
        duree_in_minutes = chanson.duree.to_minutes()
        for musique in self.liste:
            duree_in_minutes += musique.duree.to_minutes()
        if duree_in_minutes > 75.0:
            return False
        self.duree.ajouter(chanson.duree)
        self.liste.append(chanson)
        return True
    
    def __str__(self):
        """
        @pre:  -
        @post: Retourne un string décrivant l'album sous le format
            Album 21 (12 chansons, 00:47:11)
            01: White_Wedding - Billy_Idol - 00:04:12
            02: Stand_And_Deliver - Adam_&_The_Ants - 00:03:33
            03: You_Spin_Me_Around - Dead_Or_Alive - 00:03:14
            ...
        """
        intro = f"Album {self.id} ({len(self.liste)} chansons, {self.duree})\n"
        for i in range(len(self.liste)):
            intro += "{:02}: {} - {} - {}\n".format(i+1, self.liste[i].titre, self.liste[i].autheur, self.liste[i].duree)
        return intro.strip()

# Partie du programme qui lit dans le fichier music-db.txt
if __name__ == "__main__":
    
    lines = open("music-db.txt", "r").readlines()
    lines = [line.strip() for line in lines]

    chansons = []
    for line in lines:
        words = line.split()
        chansons.append(Chanson(words[0], words[1], Duree(0,int(words[2]), int(words[3]))))
    album_num = 1
    album = Album(album_num)
    for c in chansons:
        if not album.add(c):
            print(f"{album}\n")
            album_num += 1
            album = Album(album_num)
            album.add(c)
    print(album)