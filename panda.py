import turtle as t

canvas = t.Screen()
canvas.bgcolor("blue")
canvas.screensize(500,500)


def circle(r,colour):
  t.fillcolor(colour)
  t.begin_fill()
  t.circle(r)
  t.end_fill()

def face():
  t.penup()
  t.setposition(0,35)
  t.pendown()
  circle(40,'white')

def ear():
  t.penup()
  t.setposition(35,100)
  t.pendown()
  circle(20,'black')
  t.penup()
  t.setposition(-35,100)
  t.pendown()
  circle(20,'black')

def eyecircle():
  t.penup()
  t.setposition(-15,80)
  t.pendown()
  circle(10,'black')
  t.penup()
  t.setposition(15,80)
  t.pendown()
  circle(10,'black')

def eye():
  t.penup()
  t.setposition(-15,80)
  t.pendown()
  circle(5,'white')
  t.penup()
  t.setposition(15,80)
  t.pendown()
  circle(5,'white')

def nose():
  t.penup()
  t.setposition(0,60)
  t.pendown()
  circle(5,'black')

def whiskers():
  t.penup()
  t.setposition(-30,70)
  t.pendown()
  t.right(15)
  t.forward(30)
  t.penup()
  t.setposition(-30,60)
  t.pendown()
  t.left(15)
  t.forward(30)
  t.penup()
  t.setposition(3,67)
  t.pendown()
  t.left(15)
  t.forward(30)
  t.penup()
  t.setposition(3,60)
  t.pendown()
  t.right(15)
  t.forward(30)

def mouth():
  t.penup()
  t.setposition(-30,60)
  t.pendown()
  t.right(90)
  t.circle(20,180)
  

  
face()
ear()
eyecircle()
eye()
nose()
whiskers()
mouth()