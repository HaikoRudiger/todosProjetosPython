import turtle 

colors = ["red" , "purple" , "blue" , "green", "orange", "black"]
my_pen = turtle.Pen()
turtle.speed(500)
turtle.bgcolor("White")
for n in range(360):
   my_pen.pencolor(colors[n % 6])
   my_pen.width(n/100 + 1)
   my_pen.forward(n)
   my_pen.left(59)