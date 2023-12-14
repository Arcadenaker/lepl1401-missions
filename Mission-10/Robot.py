class Robot:
    
    def __init__(self, nom):
        """
        Initialise un objet Robot avec un nom et un historique vide.
        """
        self.__nom = nom
        self.__history = []

    def nom(self) :
        """
        Retourne le nom du robot.
        """
        return self.__nom

    def clear_history(self):
        """
        Cette fonction nettoie l'historique (pratique pour les tests).
        """
        self.__history = []

    def history(self):
        """
        Renvoie l'historique des actions effectuées par le TurtleBot.

        @post: Une liste des actions effectuées.
        """
        return self.__history
    
    def turn_left(self):
        """
        Ajoute l'action "turn_left" à l'historique.
        """
        self.__history.append(["left"])

    def turn_right(self):
        """
        Ajoute l'action "turn_right" à l'historique.
        """
        self.__history.append(["right"])

    def move_backward(self, distance):
        """
        Ajoute l'action "move_backward" avec la distance à l'historique.
        """
        self.__history.append(["backward", distance])

    def move_forward(self, distance):
        """
        Ajoute l'action "move_forward" avec la distance à l'historique.
        """
        self.__history.append(["forward", distance])

    def unplay(self):
        """
        Annule toutes les actions précédemment effectuées par le TurtleBot en inversant l'historique.
        """
        actions = self.history()  # Sauvegarde l'historique
        actions.reverse()  # Retourne la liste
        self.clear_history()  # Supprime l'historique une première fois pour éviter une boucle infinie
        for action in actions:  # Boucle qui permet de faire toutes les actions en sens inverse
            if action[0] == "forward":
                self.move_backward(action[1])
            elif action[0] == "backward":
                self.move_forward(action[1])
            elif action[0] == "left":
                self.turn_right()
            elif action[0] == "right":
                self.turn_left()
        self.clear_history()  # Supprime l'historique une deuxième fois pour retirer le nouvel
                              # historique qui s'est fait en faisant unplay() 
    
    def __str__(self) :
        """
        Imprime un string du type "R2-D2@(100,100) angle: 0.0" représentant le nom,
        les coordonnées et l'orientation du robot.
        """
        return str(self.nom()) + "@(" + str(round(self.x())) + "," + \
               str(round(self.y())) +") angle: "+str(self.angle())
