import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 5 - Spirograph ########

screen=t.Screen()
screen.bgcolor("black")

tim.speed("fastest")
def draw_spirograph(no_of_gaps):
  for _ in range(100):
    tim.color(random_color())
    tim.circle(100)
    current_heading=tim.heading()
    tim.setheading(current_heading + no_of_gaps)

draw_spirograph(5)
screen.exitonclick()



import colorgram 
colors = colorgram.extract("image.jpg",10)
print(colors)
rgb_colors=[]
for color in colors:
  r = color.rgb.r
  g = color.rgb.g
  b = color.rgb.b
  new_color=(r,g,b)
  rgb_colors.append(new_color)

print(rgb_colors)