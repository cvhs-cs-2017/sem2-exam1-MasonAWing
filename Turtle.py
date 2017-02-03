"""Create a Turtle Program that will draw a 3-dimensional cube"""
import turtle
ben = turtle.Turtle()
for i in range(4):
    ben.forward(50)
    ben.right(90)
ben.right(330)
ben.forward(50)
ben.backward(50)
ben.right(30)
ben.forward(50)
ben.right(330)
ben.forward(50)
ben.backward(50)
ben.right(120)
ben.forward(50)
ben.right(240)
ben.forward(50)
ben.backward(50)
ben.right(210)
ben.forward(50)
ben.right(150)
ben.forward(50)
ben.backward(50)
ben.right(300)
ben.forward(50)
ben.right(60)
ben.forward(50)
ben.right(30)
for i in range(4):
    ben.forward(50)
    ben.right(90)
input()
"""Import and Call the DrawRectangle(Anyturtle, l, w) function from the
file MyFile.py"""
from myexamfile.py import DrawRectangle
DrawRectangle(ben, 15, 30)
