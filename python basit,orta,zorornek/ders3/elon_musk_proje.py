import turtle
import random
import winsound
pencere = turtle.Screen()
pencere.bgcolor("black")
pencere.title("elon musk projesi")
pencere.bgpic("uzay.gif")
pencere.setup(width=600, height=600)


turtle.register_shape("ates.gif")
turtle.register_shape("dusman.gif")
turtle.register_shape("oyuncu.gif")

oyuncu=turtle.Turtle()
oyuncu.color("yellow")
oyuncu.speed(0)
oyuncu.shape("oyuncu.gif")
oyuncu.setheading(90)
oyuncu.penup()
oyuncu.goto(0,-250)
oyuncu_hizi=20


ates=turtle.Turtle()
ates.color("green")
ates.speed(0)
ates.shape("ates.gif")
ates.setheading(90)
ates.penup()
ates.goto(0,-240)
ates_hizi= 20
ates.hideturtle()
ates.turtlesize(1,1)
ates_kontrol = True

hedefler=[]
for i in range(7):
    hedefler.append(turtle.Turtle())
for hedef in hedefler:
    hedef.color("red")
    hedef.speed()
    hedef.turtlesize(1,1)
    hedef.shape("dusman.gif")
    hedef.penup()
    hedef.setheading(90)
    x=random.randint(-280,280)
    y=random.randint(180,260)
    hedef.goto(x,y)


def atesgit():
    y = ates.ycor()
    y = y+ates_hizi
    ates.sety(y)

def solagit():
    x = oyuncu.xcor()
    x = x-oyuncu_hizi
    if x < -300:
        x = -300
    oyuncu.setx(x)

def sagagit():
    x = oyuncu.xcor()
    x = x+oyuncu_hizi
    if x > 300:
        x = 300
    oyuncu.setx(x)

def ates_et():
    global ates_kontrol
    winsound.PlaySound("lazer.wav",winsound.SND_ASYNC)
    x=oyuncu.xcor()
    y = oyuncu.ycor()+20
    ates.goto(x,y)
    ates.showturtle()
    ates_kontrol=True

pencere.listen()
pencere.onkey(solagit,"Left")
pencere.onkey(sagagit,"Right")
pencere.onkey(ates_et,"space")


while True:

    if ates_kontrol:
        atesgit()
    for hedef in hedefler :
        y=hedef.ycor()
        y=y-2
        hedef.sety(y)
        if hedef.distance(ates) < 20:
            ates.hideturtle()
            hedef.hideturtle()
            hedefler.pop(hedefler.index(hedef))
            winsound.PlaySound("patlama.wav",winsound.SND_ASYNC)
