from math import pi
import turtle
from Robot import Robot

class TurtleBot(Robot):
    def __init__(self,nom,x=0,y=0):
        super().__init__(nom)
        # On initialise Turtle
        self.__turtle = turtle.Turtle()
        self.__turtle.speed(1) # Permet de mieux voir ce que fait Turtle
        self.__turtle.penup()
        self.__x = x
        self.__y = y
        self.__angle = 0
        # On configure turtle avec les bonnes données
        self.__turtle.goto(x,y)

    def x(self):
        """
        Retourne la composante x du robot
        """
        return self.__x
    
    def y(self):
        """
        Retourne la composante y du robot
        """
        return self.__y
    
    def angle_rad(self):
        """
        Retourne l'angle en radian du robot
        @post: Retourne l'angle (float)
        """    
        return self.__angle

    def angle(self):
        """
        Retourne l'angle en degré du robot
        @post: Retourne l'angle (float)
        """     
        return (self.angle_rad() * 180 / pi) % 360
        
    def __set_x(self,x) :
        """
        Modifie la composante x du robot
        @pré: composante en x (float)
        """  
        self.__x = x
        
    def __set_y(self,y):
        """
        Modifie la composante y du robot
        @pré: composante en y (float)
        """  
        self.__y = y

    def __set_angle_rad(self,angle) :
        """
        Modifie l'angle du robot (radian)
        @pré: l'angle (int)
        """  
        self.__angle = angle

    def position(self) :
        """
        Retourne la position du robot
        @post: la position (tuple de 2 floats)
        """  
        return (self.x(),self.y())
        
    def __move(self,distance,sense):
        """
        Bouge le robot à une certaine distance
        """
        self.__turtle.pendown()
        self.__turtle.forward(sense * distance)
        self.__turtle.penup()
        position = self.__turtle.pos()
        self.__set_x(position[0])
        self.__set_y(position[1])

    def move_forward(self,distance) :
        """
        Fait avancer en avant le robot d'une certaine distance
        @pré: prend une distance (float) 
        """
        self.__move(distance,1)
        super().move_forward(distance)

    def move_backward(self,distance) :
        """
        Fait avancer en arrière le robot d'une certaine distance
        @pré: prend une distance (float) 
        """
        self.__move(distance,-1)
        super().move_backward(distance)

    def __turn(self,direction) :
        """
        Fait tourner le robot d'une certaine amplitude
        Si direction = 1 change l'angle du robot de 90 degrés vers la droite (dans le sens des aiguilles d'une montre)
        Si direction = -1 change l'angle du robot de 90 degrés vers la gauche (dans le sens contraire des aiguilles d'une montre)
        @pré: direction (-1/1) (int)
        """
        self.__set_angle_rad(self.angle_rad() - direction * pi/2)
        self.__turtle.right(direction * 90)
        
    def turn_right(self):
        """
        Fait tourner le bot dans le sens des aiguilles d'une montre
        """
        self.__turn(1)
        super().turn_right()

    def turn_left(self):
        """
        Fait tourner le bot dans le sens inverse des aiguilles d'une montre
        """
        self.__turn(-1)
        super().turn_left()

if __name__ == '__main__': # Petite suite d'instructions donnée par l'énoncé
    r2d2 = TurtleBot("R2-D2",100,100)
    r2d2.move_forward(50)
    r2d2.turn_left()
    r2d2.move_forward(50)
    r2d2.turn_left()
    r2d2.move_forward(50)
    r2d2.turn_left()
    r2d2.move_forward(50)
    r2d2.move_forward(50)
    r2d2.turn_right()
    r2d2.move_forward(50)
    r2d2.turn_right()
    r2d2.move_forward(50)
    r2d2.turn_right()
    r2d2.move_forward(50)
    r2d2.turn_right()