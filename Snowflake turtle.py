import turtle
import random
snowflake = turtle.Turtle()
turtle.Screen().bgcolor("black")
colors = ["blue", "white", "Sky blue"]
snowflake.color("White")

for i in range(10):
    for i in range(2):
        snowflake.forward(100)
        snowflake.right(60)
        snowflake.forward(100)
        snowflake.right(120)
    snowflake.right(36)
    snowflake.color(random.choice(colors))


    
