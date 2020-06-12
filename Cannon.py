import turtle
import math
import random
import time



wn = turtle.Screen()
wn.setup(width =820, height = 620)
wn.title("cannon by Gnaneswar")
wn.bgcolor("black")
wn.tracer(0)
# draw border
border=turtle.Turtle()
border.ht()
border.penup()
border.goto(-380,-250)
border.pendown()
border.color("red")
border.goto(400,-250)
border.goto(400,230)
border.goto(-380,230)
border.goto(-380,-250)
border.penup()
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
score=0
level=1
pen2=turtle.Turtle()
pen2.speed(0)
pen2.penup()
pen2.hideturtle()
pen2.goto(350,280)

pen3=turtle.Turtle()
pen3.speed(0)
pen3.penup()
pen3.hideturtle()
pen3.goto(-350,280)
#create multiple enemies
enemies=[]
for _ in range(4):
    enemy=turtle.Turtle()
    enemy.penup()
    enemy.color("red")
    enemy.shape("circle")
    enemy.goto(random.randint(300,400),random.randint(-200,200))
    #append enemy to enemies list
    enemies.append(enemy)

#cannon class
class Cannon():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 45
        self.shape = "triangle"
        self.power = 10
        
    def rotate_left(self):
        self.angle += 10
        
    def rotate_right(self):
        self.angle -= 10
        
    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.shape)
        pen.shapesize(0.5, 1)
        pen.setheading(self.angle)
        pen.stamp()
#cannonball class
class Cannonball():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.shape = "circle"
        self.state = "ready"
    
    def update(self, g):
        if self.state == "fire":
            self.x += self.dx
            self.y += self.dy
            self.dy += g
            
            if self.y < -300:
                self.state = "ready"
    
    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.shape)
        pen.shapesize(0.25, 0.25)
        pen.stamp()
        
    def fire(self):
        if self.state == "ready":
            self.x = cannon.x
            self.y = cannon.y
            self.dx = math.cos(math.radians(cannon.angle)) * cannon.power
            self.dy = math.sin(math.radians(cannon.angle)) * cannon.power
            self.state = "fire"
        

cannon = Cannon(-250, -200)
cannon.render(pen)
cannonball = Cannonball(-250, -200)
cannonball.render(pen)
# keyboard bindings
wn.listen()
wn.onkeypress(cannonball.fire, "space")
wn.onkeypress(cannon.rotate_left, "Left")
wn.onkeypress(cannon.rotate_right, "Right")
g=-0.1
gh=100
lives=3
increase=0.5
pause=False
while not pause:
    pen.clear()
    cannonball.update(g)
    cannon.render(pen)
    cannonball.render(pen)
    #iterate through the enemies
    for enemy in enemies:
        a=cannonball.x-enemy.xcor()
        b=cannonball.y-enemy.ycor()
        distance=math.sqrt((a**2)+(b**2))
        # colistion
        if distance<20:
            enemy.goto(random.randint(300,400),random.randint(-200,200))
            score+=10
        if enemy.xcor()<-380:
            #decrease lives
            lives-=1
            enemy.goto(random.randint(300,400),random.randint(-200,200))
        enemy.setx(enemy.xcor()-increase)
    pen2.clear()
    pen2.color("white")
    pen2.write("Level: {}".format(level),move=False,align="center",font=("courier",15,"normal"))
    pen3.clear()
    pen3.color("white")
    pen3.write("               Score: {}    Lives: {}".format(score,lives),move=False,align="center",font=("courier",15,"normal"))
    #simple level system
    if lives==0:
        print("Game Over")
        pause=True
    if score==gh:
        level+=1
        gh+=100
        increase+=0.1
    wn.update()
    time.sleep(0.01)
wn.mainloop()
