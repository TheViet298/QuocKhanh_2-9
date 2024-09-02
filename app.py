import turtle
import time

# Hàm để cài đặt kích thước cửa sổ
def setwindowsize(x=640, y=640):
    turtle.setup(x, y)
    turtle.setworldcoordinates(0, 0, x, y)

# Hàm để vẽ từng pixel
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

# Hàm để vẽ ngôi sao vàng với hiệu ứng chạy theo viền
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
        time.sleep(0.5)  # Dừng một chút để tạo hiệu ứng vẽ viền
    star.end_fill()
    star.hideturtle()
    turtle.update()
    time.sleep(1)

# Hàm để hiển thị dòng chữ
def draw_text(text, start_x, start_y):
    turtle.penup()
    turtle.goto(start_x, start_y)
    turtle.color("white")
    turtle.hideturtle()
    turtle.write(text, font=("Arial", 24, "bold"), align="center")
    turtle.update()
    time.sleep(1)

# Cài đặt kích thước cửa sổ
setwindowsize(600, 400)

# Vẽ nền đỏ với hiệu ứng pixel chạy
for x in range(60):
    for y in range(40):
        drawpixel(x, y, (218, 41, 28), 10)

# Đợi một chút sau khi vẽ nền
time.sleep(1)

# Tính toán vị trí trung tâm và vẽ ngôi sao vàng
star_center_x = 300
star_center_y = 200
star_size = 100

draw_star_outline(star_center_x - 50, star_center_y + 50, star_size)

# Căn chỉnh để dòng chữ nằm dưới ngôi sao
text_start_x = star_center_x
text_start_y = star_center_y - star_size - 40  # Dòng chữ nằm dưới ngôi sao
draw_text("Mừng Quốc Khánh 2/9/2024", text_start_x, text_start_y)

# Để cửa sổ không tự đóng
turtle.done()
