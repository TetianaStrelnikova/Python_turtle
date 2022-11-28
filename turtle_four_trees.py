import turtle
import random
turtle.Screen().bgcolor("black")
turtle.colormode(255)

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t2.left(90)
t3 = turtle.Turtle()
t3.left(180)
t4 = turtle.Turtle()
t4.left(270)

turtles = [ t1,t2,t3,t4]

def branch(branch_lengh, angle):
  #one branch
  branch_grow_index = 0.8
  angle = 30
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
  
  t.speed(1000)
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  t.color((r,g,b))
  t.fillcolor((r,g,b))
  branch(30,90)

