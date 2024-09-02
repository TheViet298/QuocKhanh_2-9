import turtle

# Tạo màn hình
wn = turtle.Screen()
wn.title("Cờ Tổ Quốc Việt Nam")
wn.bgcolor("white")

pen = turtle.Turtle()
pen.speed(3)

# Hàm vẽ hình chữ nhật
def draw_rectangle(color, width, height):
    pen.begin_fill()
    pen.fillcolor(color)
    for _ in range(2):
        pen.forward(width)
        pen.right(90)
        pen.forward(height)
        pen.right(90)
    pen.end_fill()
    
pen.penup()
pen.goto(-150, 100)  # Di chuyển đến vị trí bắt đầu
pen.pendown()
draw_rectangle("red", 300, 200)

# Hàm vẽ sao vàng 5 cánh
def draw_star(x, y, radius):
    pen.penup()
    pen.goto(x, y)  
    pen.setheading(-72)
    pen.pendown()
    pen.color("yellow")
    pen.begin_fill()
    for _ in range(5):
        pen.forward(radius)
        pen.right(144)
    pen.end_fill()

# Vẽ sao vàng ở giữa lá cờ
draw_star(0, 30, 100)
#thêm text
pen.penup()
pen.goto(0, -170)  
pen.color("black")
pen.write("Mừng Quốc Khánh 2/9/2024", align="center", font=("Arial", 24, "bold"))

# Hoàn tất
pen.hideturtle()
wn.mainloop()
