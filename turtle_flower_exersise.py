import turtle
for i in range(9):
  turtle.circle (80,90)
  turtle.left (90)
  turtle.circle (80,90)
  turtle.right(230)


t= turtle.Turtle()

for angle in range(0, 360, 60):
  t.color("red")     
  t.seth(angle) 
  t.circle(100,90)
  t.left(90)
  t.circle(100,90)
  t.ht()


for angle in range(0,360,12):
  t.circle(200,40)
  t.left(140)
  t.circle(200,40)

  for angle in range(0,360,12):
  t.circle(300,30)
  t.left(150)
  t.circle(300,30)