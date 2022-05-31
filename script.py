import turtle
import random
import math

def draw_circle(turtle, color, size, x, y):
  turtle.penup()
  turtle.color(color)
  turtle.fillcolor(color)
  turtle.goto(x,y)
  turtle.begin_fill()
  turtle.circle(size/2)
  turtle.end_fill()
  turtle.pendown()
tommy = turtle.Turtle()
tommy.shape("turtle")
tommy.speed(100)
nb_cercles=35
nb_etages=32
colors = []
for i in range(nb_cercles):
  R = random.randint(0,255)
  V = random.randint(0,255)
  B = random.randint(0,255)
  colors.append((R, V, B))
def cercles(P_radius, P_width, i):
  radius = P_radius + P_width * 1.17
  width = (2 * math.pi * radius/nb_cercles) * 0.8
  for j in range(nb_cercles):
    angle = 2 * math.pi/nb_cercles * j + i * math.pi
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    draw_circle(tommy, colors[random.randint(0, nb_cercles - 1)], width, x, y)
  if (i <= nb_etages):
    cercles(radius, width, i+1)
cercles(1, 1, 1)