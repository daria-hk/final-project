import turtle
import math

def draw_pythagorean_tree(t, depth, height):
    if depth == 0:
        return
    
    t.begin_fill()
    
    t.forward(height)
    t.left(45) 
    
    new_height = height * math.sqrt(2) / 2
    
    #виведи перше піддерево
    t.forward(new_height)
    draw_pythagorean_tree(t, depth - 1, new_height)
    
    #поверніться до квадрата та підготуйтеся до малювання іншого піддерева
    t.backward(new_height)
    t.right(90)
    t.forward(new_height)
    
    draw_pythagorean_tree(t, depth - 1, new_height)
    
    #назад до оригінальної позиції
    t.backward(new_height)
    t.left(45)
    t.backward(height)

def draw(depth):
    window = turtle.Screen()
    window.colormode(255)
    window.bgcolor("#2b3e50")
    window.title("Pythagorean Tree")

    t = turtle.Turtle()
    t.width(3)
    t.speed(-1)
    t.pencolor("white")

    height = 60  

    t.penup()
    t.right(-90)
    t.pendown()

    draw_pythagorean_tree(t, depth, height)
    
    window.mainloop()

draw(6) #тут можна змінити range
