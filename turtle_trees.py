import turtle
import random

turtle.colormode(255)

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()
t5 = turtle.Turtle()
turtles = [ t1,t2,t3,t4,t5]

def branch(branch_lengh, angle):
  #one branch
  branch_grow_index = random.uniform(0.5, 0.9)
  angle = random.randint(20, 40)
  if branch_lengh > 2:
    t.forward(branch_lengh)
    t.left(angle)
    branch(branch_lengh * branch_grow_index, angle)
    t.right(angle * 2)
    branch(branch_lengh * branch_grow_index, angle)
    t.left(angle)
    t.backward(branch_lengh)



  

x = -100
for t in turtles:
  angle = random.randint(20, 40)
  branch_lengh= random.randint(60, 80)
  t.speed(500)
  t.left(90) #turns them up
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  t.color((r,g,b))
  t.fillcolor((r,g,b))
  x = x + random.randint(80,150)
  t.penup()
  t.goto(x, random.randint(-100,100))
  t.pendown()
  branch(branch_lengh,angle)