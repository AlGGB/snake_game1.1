import turtle
import time
import random

delay = 0.1
body_segment = []
score = 0
high_score = 0

wn = turtle.Screen() 

wn.title("Snake Game")

#size
wn.setup(width=600, height=600)

wn.bgcolor("green")

#obj
head = turtle.Turtle()

head.speed(0)
head.shape("square")
head.color("blue")
head.penup()
head.goto(0, 0)
head.direction = "stop"

#food config(sneak eat)
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("black")
food.penup()
food.goto(0, 100)
food.direction = "stop"

#score
text = turtle.Turtle()
text.speed(0)
text.color("white")
text.penup()
text.goto(0, 260)
text.hideturtle()
text.write(f'Score 0        high Score: 0', align="center",font=("arial", 22))


def mov():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 10)
        
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 10)
        
    if head.direction == "right":
        y = head.xcor()
        head.setx(y + 10)
        
    if head.direction == "left":
        y = head.xcor()
        head.setx(y - 10)
        
def dirUp():
    head.direction = "up"
def dirDown():
    head.direction = "down"
def dirRight():
    head.direction = "right"
def dirLeft():
    head.direction = "left"
    
#conectar al teclado               
wn.listen()
wn.onkey(dirUp, "Up")
wn.onkey(dirDown, "Down")
wn.onkey(dirRight, "Right")
wn.onkey(dirLeft, "Left")

     
while True:
    wn.update()
    
 #colicion con la ventana
    if head.xcor() > 280 and head.xcor <-280 or head.ycor() > 280 and head.ycor() < -280:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        
#esconder segmento
        for segment in body_segment:
            segment.goto(1000, 1000)
        
        body_segment.clear()
        score = 0
        text.clear()
        text.write(f'Score {score}        high Score: {high_score}', align="center",font=("arial", 22))
      
    
 #que pasa cuando chocan con comida   
    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)
        
  #agregar nuevo segmento cuerpo a snake      
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("red")
        new_segment.penup()
        body_segment.append(new_segment)
     
 #aumento de marcador       
    score += 10
    if score > high_score:
        high_score = score
        
    text.clear()
    text.write(f'Score {score}        high Score: {high_score}', align="center",font=("arial", 22))
     
    totalSeg = len(body_segment)     
 
    for i in range(totalSeg - 1, 0, -1):
        x = body_segment[i-1].xcor()
        y = body_segment[i-1].ycor()
        body_segment[i].goto(x, y)  
    
    if totalSeg > 0:
        x = head.xcor()
        y = head.ycor()
        body_segment[0].goto(x, y)


#colicion con el propio cuerpo        
    for segment in body_segment:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            
            for segment in body_segment:
                segment.goto(1000, 1000)
                
            body_segment.clear()
            
            score = 0
            text.clear()
            text.write(f'Score {score}        high Score: {high_score}', align="center",font=("arial", 22))

        
        
    mov()
    time.sleep(delay)





turtle.done()