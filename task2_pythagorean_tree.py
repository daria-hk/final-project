import turtle
import math

def draw_pythagoras_tree(t, depth, height):
    if depth == 0:
        return
    
    t.begin_fill()
    
    t.forward(height)
    t.left(45) 
    
    new_height = height * math.sqrt(2) / 2
    
    #draw first subtree
    t.forward(new_height)
    draw_pythagoras_tree(t, depth - 1, new_height)
    
    #move back to square and prepare to draw other subtree
    t.backward(new_height)
    t.right(90)
    t.forward(new_height)
    
    draw_pythagoras_tree(t, depth - 1, new_height)
    
    #back to original pos
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

    draw_pythagoras_tree(t, depth, height)
    
    window.mainloop()

draw(6) #change range
