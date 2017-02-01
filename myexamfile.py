import turtle
def addten(n):
    n = n + 10
    return n
print(addten(10))
ben = turtle.Turtle
def DrawRectangle(Anyturtle, l, w):
    for i in range(2):
        turtle.forward(l)
        turtle.right(90)
        turtle.forward(w)
        turtle.right(90)
DrawRectangle(ben, 12, 50)
input()
def DrawPoly(Anyturtle, n):
    for x in range(n):
        turtle.forward(10)
        turtle.right(360/n)
DrawPoly(ben, 30)
input()
