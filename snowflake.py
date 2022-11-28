import turtle
turt = turtle.Turtle()
turt.speed(5000)
turtle.colormode(255)
import random
def koch(l):
  if l >3 :
    koch(l/3)
    turt.left(60)
    koch(l/3)
    turt.right(120)
    koch(l/3)
    turt.left(60)
    koch(l/3)
  else:
    turt.forward(l)
    
def snowflake(l):
  for _ in range (4):
    koch(l)
    turt.right(90)
for i in range(50):
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  turt.color((r,g,b))
  turt.fillcolor((r,g,b))
  turt.penup()
  turt.goto(random.randint(-300,300), random.randint(-300,300))
  turt.pendown()
  snowflake(random.randint(30,100))

