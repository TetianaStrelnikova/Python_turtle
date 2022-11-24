'''1. Write a function called square that takes a parameter named t, which is a turtle. It
should use the turtle to draw a square.
Write a function call that passes bob as an argument to square, and then run the
program again.
'''
'''2. Add another parameter, named length, to square. Modify the body so length of the
sides is length, and then modify the function call to provide a second argument. Run
the program again. Test your program with a range of values for length.
'''
'''3. Make a copy of square and change the name to polygon. Add another parameter
named n and modify the body so it draws an n-sided regular polygon. Hint: The
exterior angles of an n-sided regular polygon are 360/n degrees.
'''
'''4. Write a function called circle that takes a turtle, t, and radius, r, as parameters and
that draws an approximate circle by calling polygon with an appropriate length and
number of sides. Test your function with a range of values of r.
Hint: figure out the circumference of the circle and make sure that length * n =
circumference.
'''
'''5. Make a more general version of circle called arc that takes an additional parameter
angle, which determines what fraction of a circle to draw. angle is in units of degrees,
so when angle=360, arc should draw a complete circle.
'''
#1
import turtle

t = turtle.Turtle()
t.color("red")
t.shape("turtle")

lenght = int(input("What is thr lenght? "))

def square(t, l):
  for i in range(4):
    t.forward(l)
    t.right(90)
square(t, lenght)

n = int(input("How many sides?? "))

def polygon(t, l, n):
  t.color("red")
  t.shape("turtle")
  for i in range(n):
    t.right(360 / n)
    t.forward(l)
polygon(t, lenght, n)

radius = int(input("What  is the radius? "))

def circle(t, r):
  t.circle(r)
circle(t, radius)

angle = int(input("What is the angle ? "))

def arc(t, r, a):
  t.circle(r, a)
arc(t, radius, angle)
