import turtle

# Layar
wn = turtle.Screen()
wn.title("Ping Pong")
wn.bgcolor("Black")
wn.setup(800,600)
wn.tracer(0)

# Border
border = turtle.Turtle()
border.speed(0)
border.hideturtle()
border.penup()
border.goto(-250,-250)
border.pendown()
border.pencolor("white")

for _ in range(4) :
    border.forward(500)
    border.left(90)

# Score
score1 = 0
score2 = 0
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()
pen.pencolor("White")
pen.goto(0, 230)
pen.write("Pemain 1 : {}   Pemain 2 : {}".format(score1,score2), align="center" ,font=("arial", 12, "normal"))

# Pemain 1
pemain1 = turtle.Turtle()
pemain1.speed(0)
pemain1.shape("square")
pemain1.color("White")
pemain1.shapesize(3,0.5)
pemain1.penup()
pemain1.goto(-230,0)

# Pemain 2
pemain2 = turtle.Turtle()
pemain2.speed(0)
pemain2.shape("square")
pemain2.color("White")
pemain2.shapesize(3,0.5)
pemain2.penup()
pemain2.goto(230,0)

# Bola
bola = turtle.Turtle()
bola.speed(0)
bola.shape("square")
bola.color("White")
bola.shapesize(0.5)
bola.penup()
bola.goto(0,0)
bola.dx = 0.2
bola.dy = 0.2

# Function
def pemain1_up() :
    y = pemain1.ycor()
    y += 20 
    pemain1.sety(y)

def pemain1_down() :
    y = pemain1.ycor()
    y -= 20 
    pemain1.sety(y)

def pemain2_up() :
    y = pemain2.ycor()
    y += 20 
    pemain2.sety(y)

def pemain2_down() :
    y = pemain2.ycor()
    y -= 20 
    pemain2.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(pemain1_up, "Up")
wn.onkeypress(pemain1_down, "Down")
wn.onkeypress(pemain2_up, "w")
wn.onkeypress(pemain2_down, "s")

# Main loop
while True :

    wn.update()

    # Bola Bergerak
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    # Border Cek
    if bola.ycor() > 245 :
        bola.sety(235)
        bola.dy *= -1 

    if bola.ycor() < -245 :
        bola.sety(-235)
        bola.dy *= -1 

    if bola.xcor() > 240 :
        bola.goto(0,0)
        bola.dx *= -1
        score1 += 1
        pen.clear()
        pen.write("Pemain 1 : {}   Pemain 2 : {}".format(score1,score2), align="center" ,font=("arial", 12, "normal"))

    if bola.xcor() < -240 :
        bola.goto(0,0)
        bola.dx *= -1
        score2 += 1 
        pen.clear()
        pen.write("Pemain 1 : {}   Pemain 2 : {}".format(score1,score2), align="center" ,font=("arial", 12, "normal"))

    if pemain1.ycor() > 217 :
        pemain1.sety(217)

    if pemain1.ycor() < -217 :
        pemain1.sety(-217)

    # Bola dan pemain cek
    if (bola.xcor() > 225 and bola.xcor() < 235 ) and (bola.ycor() < pemain2.ycor() + 30 and bola.ycor() > pemain2.ycor() - 30 ) :
        bola.setx(225)
        bola.dx *= -1
    
    if (bola.xcor() < -225 and bola.xcor() > -235 ) and (bola.ycor() < pemain1.ycor() + 30 and bola.ycor() > pemain1.ycor() - 30 ) :
        bola.setx(-225)
        bola.dx *= -1

    # AI 
    if pemain2.ycor() < bola.ycor() and abs(pemain2.ycor() - bola.ycor()) > 10  :
        pemain2_up()
        if pemain2.ycor() > 217 :
            pemain2.sety(217)

    elif pemain2.ycor() > bola.ycor() and abs(pemain2.ycor() - bola.ycor()) > 10  :
        pemain2_down()
        if pemain2.ycor() < -217 :
            pemain2.sety(-217)