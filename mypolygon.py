import turtle
import random


valera = turtle.Turtle()
valera.color("#CBF078")
valera.shape("turtle")
valera.pensize(3)
valera.speed()
valera.forward(100)
valera.right(90)
valera.forward(100)
valera.right(90)
valera.forward(100)
valera.right(90)
valera.forward(100)

alex = turtle.Turtle()
alex.color("#F8F398")
alex.shape("turtle")
alex.speed()
alex.pensize(3)
alex.left(90)
alex.forward(100)
alex.left(90)
alex.forward(100)
alex.left(90)
alex.forward(100)
alex.left(90)
alex.forward(100)

bob = turtle.Turtle()
bob.color("#F1B963")
bob.shape("turtle")
bob.speed()
bob.pensize(3)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)

tim = turtle.Turtle()
tim.color("#E46161")
tim.shape("turtle")
tim.speed()
tim.pensize(3)
tim.right(90)
tim.forward(100)
tim.right(90)
tim.forward(100)
tim.right(90)
tim.forward(100)
tim.right(90)
tim.forward(100)

varvara = turtle.Turtle()
varvara.color("#FF6F3C")
varvara.shape("turtle")
varvara.pensize(3)
varvara.forward(50)
varvara.right(90)
varvara.forward(50)
for _ in range(12):
  varvara.right(90)
for i in range(3):
  varvara.right(90)
  varvara.forward(100)
for _ in range(2):
  varvara.right(90)
  varvara.forward(50)

mary = turtle.Turtle()
mary.color("#A2C11C")
mary.shape("turtle")
mary.pensize(3)
for i in range(3):
  mary.right(90)
  mary.forward(100)
mary.right(180)
mary.circle(100)
mary.right(90 + 90 + 90)
mary.forward(100)


for i in range (10):
  
   turtle.colormode(255)
   r = random.randint(0,255)
   g = random.randint(0,255)
   b = random.randint(0,255)
   print(r,g,b)
   tim.color((r,g,b))
   tim.fillcolor((r,g,b))
   tim.begin_fill()
   
   turtle_Shapes = ["classic","arrow","turtle","circle","square","triangle"]
   shape = random.choice(turtle_Shapes)
   tim.shape(shape)         
             
   pos1 = random.randint(-100,100)
   pos2 = random.randint(-100,100)
   tim.penup()
   tim.goto(pos1,pos2)
   tim.pendown()  
   
   tim.circle(random.randrange(5,40))
   tim.end_fill()
  