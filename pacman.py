import turtle
import random
import time

lives=3
score=0

#the game screen/window
window = turtle.Screen()
window.tracer(0)
window.title('PAC MAN')
window.bgcolor('black')
window.setup(600,600)

#Pac-Man 
pacman = turtle.Turtle()
pacman.speed(0)
pacman.penup()
pacman.color('blue')
pacman.shape('circle')
pacman.direction='stop'

#Enemies which come in random order
enemies = []
for x in range(5):
    enemy = turtle.Turtle()
    enemy.penup()
    enemy.color('red')
    enemy.shape('turtle')
    enemy.speed=0.5
    #coordinates for enemies to enter
    x=random.randint(-280,280)
    y=random.randint(-280,280)
    enemy.setposition(x,y)
    enemies.append(enemy)

#to mention the score nd the number of lives 
pen=turtle.Turtle()
pen.speed(0)
pen.color('blue')
pen.penup()
pen.goto(0,245)
pen.pendown()
pen.write('Score:{} Lives:{}'.format(score,lives),align='center',font=('Courier',36))
pen.hideturtle()

# Food present in random position of screen
foods = []
for _ in range(30):
    food=turtle.Turtle()
    food.speed(0)
    food.penup()
    food.color('yellow')
    food.shape('circle')
    food.shapesize(stretch_wid=0.4,stretch_len=0.4)
    x=random.randint(-280,280)
    y=random.randint(-280,280)
    food.setposition(x,y)
    foods.append(food)
    
#enemy movement in random
def enemyMovement():
    for enemy in enemies:
        y=enemy.ycor()
        x=enemy.xcor()
        y+=enemy.speed
        x+=enemy.speed
        enemy.sety(y)
        enemy.setx(x)

#Pac-Man movement control under user 
def movement():
    if pacman.direction=='up':
        y=pacman.ycor()
        y+=0.5
        pacman.sety(y)

    if pacman.direction=='down':
        y=pacman.ycor()
        y-=0.5
        pacman.sety(y)

    if pacman.direction=='left':
        x=pacman.xcor()
        x-=0.5
        pacman.setx(x)

    if pacman.direction=='right':
        x=pacman.xcor()
        x+=0.5
        pacman.setx(x)

#directions Pac-Man move 
def moveUp():
    pacman.direction='up'

def moveDown():
    pacman.direction='down'

def moveLeft():
    pacman.direction='left'

def moveRight():
    pacman.direction='right'
    
window.listen()
window.onkeypress(moveUp,'Up')
window.onkeypress(moveDown,'Down')
window.onkeypress(moveLeft,'Left')
window.onkeypress(moveRight,'Right')


while True:
    window.update()#updating the screen 
#Pac-Man loses a life if he meets the end of screen
    if pacman.xcor()>300 or pacman.xcor()<-300 or pacman.ycor()>300 or pacman.ycor()<-300:
        lives-=1
        pen.clear()
        pen.write('Score:{} Lives:{}'.format(score,lives),align='center',font=('Courier',36))
        time.sleep(1)
        pacman.goto(0,0)
    if lives==0:
        score=0
        lives=3
        pen.clear()
        pen.write('Score:{} Lives:{}'.format(score,lives),align='center',font=('Courier',36))
        time.sleep(1)
        pacman.goto(0,0)
#Score increses as they collect more food           
    for food in foods:
        if pacman.distance(food)<10:
            score+=1
            pen.clear()
            pen.write('Score:{} Lives:{}'.format(score,lives),align='center',font=('Courier',36))
            x=random.randint(-280,280)
            y=random.randint(-280,280)
            food.goto(x,y)
    for enemy in enemies:
        if enemy.xcor()>300 or enemy.xcor()<-300 or enemy.ycor()>300 or enemy.ycor()<-300:
             x=random.randint(-280,280)
             y=random.randint(-280,280)
             enemy.goto(x,y)
             enemyMovement()
#Pac-Man loses a life whn encountered by a enemy
    for enemy in enemies:
        if pacman.distance(enemy)<10:
            lives-=1
            pen.clear()
            pen.write('Score:{} Lives:{}'.format(score,lives),align='center',font=('Courier',36))
            time.sleep(1)
            pacman.goto(0,0)            
    movement()
    enemyMovement()
