import turtle #imports so you can use turtle
window = turtle.Screen()
window.bgcolor("navy blue")


tree = turtle.Turtle()
tree.penup()
tree.color("forest green")


#leaves
def maketreeseg(size, toppos):
    tree.begin_fill()
    tree.setposition(0, toppos)
    tree.setposition(size, toppos-size)  
    tree.setposition(-size, toppos-size)
    tree.setposition(0, toppos)
    tree.end_fill()

maketreeseg(50, 20)
maketreeseg(80, 0)
maketreeseg(110, -20)



#Wood for tree
wood = turtle.Turtle()
wood.color("brown")
wood.right(90)
wood.pensize(30)
wood.penup()
wood.forward(100)
wood.pendown()
wood.forward(150)
turtle.done()