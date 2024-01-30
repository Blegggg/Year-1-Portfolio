from turtle import *  #imports turtle to start creating a shape

sides = input("how many sides?")
if sides == "4":
    print("Square")
    size = input("how big: small or large?")
if size == "small":
    color('yellow', 'purple')
    begin_fill()   #begins the drawing
    for i in range(0, 10): #loops 10 times
        forward(50)   #length of square
        right(90)    #angle of square
        forward(50)
        right(90)
        forward(50)
        right(90)
        forward(50)
        right(90)
        end_fill()  #stops drawing and finishes loo
        done() 
if size == "large":
       color('yellow', 'purple')
begin_fill()   #begins the drawing
for i in range(0, 10): #loops 10 times
        forward(100)   #length of square
        right(90)    #angle of square
        forward(100)
        right(90)
        forward(100)
        right(90)
        forward(100)
        right(90)
        end_fill()  #stops drawing and finishes loo
        done() 
if sides== "3":
    print("Triangle")
    color('yellow', 'purple')
    begin_fill()
    for i in range(0, 10):
        color('yellow', 'purple')
begin_fill()
forward(30)  #first turn
right(60)
forward(30)
right(60)
end_fill() #finishes drawing shape
done()