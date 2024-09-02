import turtle
import time

def setwindowsize(x=640, y=640):
    turtle.setup(x, y)
    turtle.setworldcoordinates(0, 0, x, y)

def drawpixel(x, y, color, pixelsize=1):
    turtle.tracer(0, 0)
    turtle.colormode(255)
    turtle.penup()
    turtle.setpos(x * pixelsize, y * pixelsize)
    turtle.color(color)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(pixelsize)
        turtle.right(90)
    turtle.end_fill()
    turtle.update()
    time.sleep(0.01)

def draw_star_outline(x, y, size):
    star = turtle.Turtle()
    star.speed(1)
    star.penup()
    star.goto(x, y - size / 2)
    star.pendown()
    star.color("yellow")

    star.begin_fill()
    for i in range(5):
        star.forward(size)
        star.right(144)
        turtle.update()
        time.sleep(0.5)  # tạo hiệu ứng viền
    star.end_fill()
    star.hideturtle()
    turtle.update()
    time.sleep(1)

def draw_text(text, start_x, start_y):
    turtle.penup()
    turtle.goto(start_x, start_y)
    turtle.color("white")
    turtle.hideturtle()
    turtle.write(text, font=("Arial", 24, "bold"), align="center")
    turtle.update()
    time.sleep(1)

setwindowsize(600, 400)

for x in range(60):
    for y in range(40):
        drawpixel(x, y, (218, 41, 28), 10)

time.sleep(1)

# Vị trí ngôi sao
star_center_x = 300
star_center_y = 200
star_size = 100

draw_star_outline(star_center_x - 50, star_center_y + 50, star_size)

text_start_x = star_center_x
text_start_y = star_center_y - star_size - 40 
draw_text("Mừng Quốc Khánh 2/9/2024", text_start_x, text_start_y)

turtle.done()
