import turtle
screen = turtle.getscreen()

from turtle import *
import math

# set turtle
def initializeTurtle():
    shape("turtle")
    speed(4)

# basic circle drawing
def drawCircle(lineStart, radius, headingAngle=0, lineThickness=3, lineColour="light blue", fillColour="cornflower blue"):
    pensize(lineThickness)
    pencolor(lineColour)
    fillcolor(fillColour)
    penup()
    goto(lineStart)
    setheading(headingAngle)
    pendown()
    begin_fill()
    circle(radius)
    end_fill()

# basic line drawing
def drawLine(lineStart, lineEnd, lineThickness=5, lineColour="purple"):
    pensize(lineThickness)
    pencolor(lineColour)
    penup()
    goto(lineStart)
    pendown()
    goto(lineEnd)

# arc based on points
def drawArc(lineStart, radius, arcAngle, lineThickness=1, headingAngle=0, lineColour="dark slate gray", fillColour="pale turquoise"):
    pensize(lineThickness)
    pencolor(lineColour)
    fillcolor(fillColour)
    penup()
    goto(lineStart)
    pendown()
    begin_fill()
    setheading(headingAngle)
    circle(radius, extent=arcAngle)
    end_fill()

# polyline connected based on points
def drawPolyLine(lineStart, points, lineColour="steel blue", lineThickness=1, fillColour="thistle"):
    pensize(lineThickness)
    pencolor(lineColour)
    fillcolor(fillColour)
    penup()
    goto(lineStart)
    pendown()
    begin_fill()
    x, y = lineStart
    for point in points:
        dx, dy = point
        goto(x + dx, y + dy)
    goto(lineStart)

    end_fill()
    penup()

def generatesquarecorners(i):
    return [(i, 0), (i, i), (0, i), (0, 0)]

# tests

# lines
def testLines():
    lineStart = (0, 0)
    lineEnd = (-100, 100)
    drawLine(lineStart, lineEnd)

    lineStart = (200, 200)
    lineEnd = (-200, -200)
    drawLine(lineStart, lineEnd, lineThickness=4, lineColour="blue")

# circles
def testCircles():
    start1 = (-200, 100)
    radius = 40
    drawCircle(start1, radius)
    start2 = (200, -100)
    radius = 60
    drawCircle(start2, radius, fillColour="dark blue")
    drawLine(start1, start2, lineThickness=3)
    start3 = (-100, -200)
    radius = 80
    drawCircle(start3, radius, lineThickness=5)
    start4 = (0, 200)
    radius = 60
    drawCircle(start4, radius, lineColour="pink", lineThickness=4, fillColour="cornflower blue")
    drawLine(start3, start4, lineThickness=3, lineColour="purple")

# circles with different heading angles
def testmoreCircles():
    start = (0, 0)
    radius = 100
    drawCircle(start, radius, headingAngle=90, fillColour="azure")
    drawCircle(start, radius, headingAngle=270, fillColour="cornflower blue")

# arcs
def testArcs():
    start = (0, 0)
    radius = 100
    drawArc(start, radius, arcAngle=180, lineThickness=8)
    drawArc(start, radius, arcAngle=180, lineThickness=8, headingAngle=90, lineColour="dark red")
    drawArc(start, radius, arcAngle=180, lineThickness=8, headingAngle=180, lineColour="cornflower blue")
    drawArc(start, radius, arcAngle=180, lineThickness=8, headingAngle=270, lineColour="dark sea green")
    start = (-180, -220)
    radius = 350
    drawArc(start, radius, arcAngle=60, headingAngle=330, lineColour="steel blue", fillColour="steel blue")

# polylines
def testPolyLines():
    squareShape = [(70, 0), (70, 70), (0, 70), (0, 0)]
    drawPolyLine((200, 200), squareShape)
    drawPolyLine((-200, 200), squareShape, lineColour="purple", lineThickness=3, fillColour="light blue")
    biggerSquareShape = generatesquarecorners(100)
    drawPolyLine((-200, -200), biggerSquareShape, fillColour="purple")
    triangleShape = [(200, 0), (100, 100), (0, 0)]
    drawPolyLine((100, -100), triangleShape, fillColour="dark sea green")

# drawing a STRAWBERRY!! ice cream
def drawIceCream():
    drawCircle((0, 0), 100, lineThickness=4, lineColour="pink", fillColour="lightpink")
    fillcolor("wheat")
    begin_fill()
    drawLine((0, -200), (100, 50), lineThickness=2, lineColour="tan")
    drawLine((100, 50), (-100, 50), lineThickness=2, lineColour="tan")
    drawLine((-100, 50), (0, -200), lineThickness=2, lineColour="tan")
    end_fill()
    drawArc((34, 185), 30, arcAngle=180, headingAngle=90, lineColour="orange red", fillColour="tomato")
    drawLine((53, 154), (76, 133), lineThickness=5, lineColour="pale violet red")
    drawLine((-50, 152), (-73, 134), lineThickness=6, lineColour="pale violet red")
    drawLine((25, 158), (10, 130), lineThickness=5, lineColour="pale violet red")
    drawLine((-25, 150), (-10, 139), lineThickness=6, lineColour="light salmon")
    drawLine((-45,136), (-50, 164), lineThickness=5, lineColour="light salmon")
    drawLine((-30, 90), (24, 116), lineThickness=6, lineColour="light salmon")
    hideturtle()


# final function
def main():
# tests
    initializeTurtle()
    testLines()
    clear()
    testCircles()
    testmoreCircles()
    clear()
    testArcs()
    clear()
    testPolyLines()
    clear()
#drawing ice cream
    drawIceCream()
main()