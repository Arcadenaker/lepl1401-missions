import turtle
t = turtle.Turtle()
t.speed("fastest")
#Définis un titre à la fenêtre
turtle.title("Mission 3")
t.up()
#Définis la taille de la fenêtre
t.screen.setup(960,540)

#Définition des constantes de couleur 
#pour un rendu plus vivant
EU_YELLOW = "#FFCC00"
BE_YELLOW = "#FDDA24"
GE_YELLOW = "#FFCE00"
EU_BLUE = "#003399"
BE_RED = "#EF3340"
DU_RED = "#AE1C28"
FR_RED = "#EF4135"
GE_RED = "#DD0000"
LU_RED = "#F6343F"
DU_BLUE = "#21468B"
FR_BLUE = "#0055A4"
GK_BLUE = "#0D5EAF"
LU_CYAN = "#00A2E1"

def square(size, color):
    t.color(color)
    t.pendown()
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()
    t.penup()

def rectangle(width, height, color):
    t.color(color)
    t.pendown()
    t.begin_fill()
    #Trace les 4 côtés du rectangle 
    #Si le côté est pair -> 0,2 -> longeur
    #Si le côté est impair -> 1,3 -> largeur
    for i in range(4):
        if i%2==0:
            t.forward(width)
        else:
            t.forward(height)
        t.right(90)
    t.end_fill()
    t.penup()

def star(width, color):
    t.color(color)
    t.setheading(0)
    t.fillcolor(color)
    t.begin_fill()
    #La boucle ci-dessous permet de créer une étoile
    #de manière simple et efficace
    for _ in range(5):
        t.right(144)
        t.forward(width)
    t.end_fill()
    t.setheading(0)
       
#"vertical" est un paramètre booléen qui précise si les rectangles du
#drapeau doivent être vertical
def three_color_flag(width, color1, color2, color3, vertical=False):
    t.down()
    colors = [color1, color2, color3]
    if bool(vertical) == True:
        height = (2*width)/9 
        for i in range(3):
            rectangle(width, height, colors[i])
            t.right(90)
            t.forward(height)
            t.left(90)
    else:
        #width est divisé par 3 pour les rectangles du drapeau
        width = width/3
        #Dans les consignes on nous donne les proportions 3/2, height
        #vaut 2/3, il ne manque donc plus qu'à multiplier par 2
        height = 2*width
        for i in range(3):
            rectangle(width, height, colors[i])
            t.forward(width)
    t.up()

#Définition des différents drapeaux limitrophes
#______________________________________________
def belgian_flag(width):
    three_color_flag(width, "black", BE_YELLOW, BE_RED)

def french_flag(width):
    three_color_flag(width, FR_BLUE, "white", FR_RED)

def dutch_flag(width):
    three_color_flag(width, DU_RED, "white", DU_BLUE, True)

def german_flag(width):
    three_color_flag(width, "black", GE_RED, GE_YELLOW, True)

def luxemburg_flag(width):
    three_color_flag(width, LU_RED, "white", LU_CYAN, True)
#______________________________________________

def european_flag(width):
    height = (2*width)/3
    init = t.pos()
    rectangle(width, height, EU_BLUE)
    #Va au milieu du drapeau avec un décalage de la moitié d'une étoile 
    #(width/17)/2 = width/34 pour que toutes les étoiles soient centrées
    t.goto(init[0]+width/2+width/34, init[1]-height/2)
    center_flag = t.pos()
    t.up()
    #Création des 12 étoiles
    for i in range(12):
        t.right(30)
        t.forward(width/5)
        t.down()
        #width/17 est une taille arbitraire décidée pour
        #une meilleure ressemblance au drapeau
        star(width/17, EU_YELLOW)
        t.setheading(30*(i+1))
        t.up()
        t.goto(center_flag)

#Définition de la fonction pour créer le drapeau grèque
def greek_flag(width):
    init = t.pos()
    height = (2*width)/3
    rectangle(width, height, GK_BLUE)
    height_line = height/9
    #Dessine les 4 lignes blanches
    for i in range(1,9,2):
        t.goto(init[0], init[1]-i*height_line)
        rectangle(width, height_line, "white")
        
    #Dessine les 4 carrés bleus
    t.goto(init)
    square(2*height_line, GK_BLUE) #Supérieur gauche

    t.goto(init[0]+3*height_line, init[1])
    square(2*height_line, GK_BLUE) #Supérieur droit

    t.goto(init[0], init[1]-3*height_line)
    rectangle(2*height_line,height_line, GK_BLUE) #Inférieur droit 
                                                                          #Je fais des rectangles au lieu des carrés
    t.goto(init[0]+3*height_line, init[1]-3*height_line)                  #pour les 2 inférieurs car cela ne change rien esthétiquement
    rectangle(2*height_line,height_line, GK_BLUE) #Inférieur gauche       #et règle une inprécision dû certainement à un arondi
    
    #Dessine la croix entre les carrés
    t.goto(init[0]+2*height_line, init[1])
    rectangle(height_line, 5*height_line, "white")
    t.goto(init[0], init[1]-2*height_line)
    rectangle(5*height_line, height_line, "white")

#Placement des drapeaux

#Drapeau UE
t.goto(-150, 40)
european_flag(300)

#Les 4 drapeaux supérieurs
t.goto(-350, 200)
german_flag(120)
t.goto(-200, 200)
dutch_flag(120)
t.goto(-50, 200)
greek_flag(120)
t.goto(100, 200)
luxemburg_flag(120)
t.goto(250, 200)
french_flag(120)

#Drapeau belge gauche
t.goto(-425, -75)
t.setheading(30)
belgian_flag(175)

#Drapeau belge droit
t.goto(270, 5)
t.setheading(-30)
belgian_flag(175)

#Quitte le programme lors d'un click sur
#la fenêtre
t.screen.exitonclick()