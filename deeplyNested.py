
 import turtle
import random
turtle_Shapes = ["classic","arrow","turtle","circle","square","triangle"]
bob = turtle.Turtle()
bob.color("green")
bob.shape(random.choice(turtle_Shapes))    

 
tim = turtle.Turtle()
tim.color("orange")
tim.shape(random.choice(turtle_Shapes))    

rob = turtle.Turtle()
rob.color("pink")
rob.shape(random.choice(turtle_Shapes))    

def what_nested(r):
  bob.penup()
  bob.goto(50,50)
  bob.pendown()
  rob.penup()
  rob.goto(-50,-50)
  rob.pendown()
  if r == 0:
        print ("I could not draw a circle with radius=0")
  elif r>10 :
    if r< 20:
      if r!= 11:
        bob.circle(r)
        rob.circle(r)
        tim.circle(r*2)
  else:
    bob.circle(r*2)
    rob.circle(r*3)
    tim.circle(r*6)
what_nested(int(input("Enter a radius:")))

def what_chained(r):
  bob.penup()
  bob.goto(50,50)
  bob.pendown()
  rob.penup()
  rob.goto(-50,-50)
  rob.pendown()
  if r == 0:
        print ("I could not draw a circle with radius=0")
  elif r>10 and r< 20 and r!= 11:
      bob.circle(r)
      rob.circle(r)
      tim.circle(r*2)
  else:
    bob.circle(r*2)
    rob.circle(r*3)
    tim.circle(r*6)
what_chained(int(input("Enter a radius:")))