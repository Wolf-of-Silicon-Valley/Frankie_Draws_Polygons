import _tkinter
import turtle
import time
import math
import keyboard

t = turtle.Turtle()
wn = turtle.Screen()
global directions
directions = ''
global in_radius
in_radius = None


def tPolygon():
    global in_radius
    global directions
    wn.title('Frankie the Turtle Draws Regular Polygons')
    wn.setup(width=800, height=600, startx=0, starty=0)
    wn.mode(mode='standard')
    wn.bgcolor('chartreuse')
    t.shape('turtle')
    t.shapesize(stretch_wid=1.1, stretch_len=1.1)
    t.speed(3)
    t.pensize(3)
    t.dot(15, 'black')
    t.penup()

    def question():
        global directions
        directions = wn.textinput('Help Frankie the Turtle!', 'Frankie the Turtle wants to draw some shapes.\n'
                                  'Directions for letting Frankie know what you want him to draw:\n\n'
                                  'For Frankie the Turtle to draw a(n):\n\n'
                                  '\t1) regular polygon, enter any number above 3.\n'
                                  "\t2) circumscribed circle, enter 'O' (capitalized o).\n"
                                  "\t3) inscribed circle, enter 'o' followed by a space and the number of sides\n"
                                  "\t     the shape you want Frankie to draw a inscribed circle for has.\n\n"
                                  "<Enter 'u' to use the back arrow as an undo button. When complete,\n"
                                  "\t press 'SPACE' twice to return to the prompt.>\n"
                                  "<Press 'SPACE' to continue after each command.>\n"
                                  "<To clear and continue, enter 'c'.>\n"
                                  "<To exit, enter 'e'.>\n\n")

    def directions_digit():
        if n % 2 == 0:
            t.penup()
            t.color('blue')
            t.setposition(0, in_radius)
            for i in range(n + 1):
                if i == 0:
                    t.showturtle()
                    t.setheading(180)
                    t.pendown()
                    t.forward(half_inrad_side)
                elif i == n:
                    t.showturtle()
                    t.left(180 - interior_theta)
                    t.forward(half_inrad_side)
                else:
                    t.showturtle()
                    t.left(180 - interior_theta)
                    t.forward(side_length_inrad)

        elif n % 2 != 0:
            t.penup()
            t.color('black')
            t.setposition(0, circum_radius)
            for i in range(n):
                if i == 0:
                    t.showturtle()
                    t.setheading(270 - half_interior_theta)
                    t.pendown()
                    t.forward(side_length_circum)
                else:
                    t.showturtle()
                    t.left(180 - interior_theta)
                    t.forward(side_length_circum)

    def directions_O():
        circum_radius = 250
        t.penup()
        t.showturtle()
        t.setposition(0, circum_radius)
        t.pendown()
        t.setheading(180)
        t.color('red')
        t.circle(circum_radius)
        t.penup()

    def directions_o():
        global in_radius
        if directions == 'o':
            t.showturtle()
            t.penup()
            t.setposition(0, in_radius)
            t.setheading(180)
            t.color('red')
            t.pendown()
            t.circle(in_radius)
            t.penup()
        elif directions[-1].isdigit():
            num = directions[-1]
            n = int(num)
            circum_radius = 250
            in_radius = circum_radius * math.cos(math.radians(180 / n))
            t.showturtle()
            t.penup()
            t.setposition(0, in_radius)
            t.setheading(180)
            t.color('red')
            t.pendown()
            t.circle(in_radius)
            t.penup()

    def directions_undo():
        while True:
            if keyboard.is_pressed('left'):
                t.undo()
            elif keyboard.is_pressed('space'):
                break

    def directions_c():
        tPolygon()

    def directions_exit():
        t.hideturtle()
        t.reset()
        t.hideturtle()
        t.penup()
        t.setposition(0, 50)
        wn.bgcolor('black')
        t.color('chartreuse')
        t.pendown()
        t.hideturtle()
        style = ('Impact', 70, 'normal')
        t.write(arg='Frankie says:', move=False, font=style, align='center')
        t.penup()
        t.hideturtle()
        t.setposition(0, -70)
        time.sleep(0.5)
        t.pendown()
        t.write(arg='"Goodbye, friend!"', move=False, font=style, align='center')
        time.sleep(1.5)
        exit()
    count = 1

    while True:
        global directions
        global in_radius
        try:
            if count == 1:
                question()
                if directions is None:
                    exit()
                elif directions.isdigit():
                    n = int(directions)
                    circum_radius = 250
                    in_radius = circum_radius * math.cos(math.radians(180 / n))
                    interior_theta = ((n - 2) * 180) / n
                    half_interior_theta = interior_theta / 2
                    side_length_circum = circum_radius * (2 * math.sin(math.radians(180 / n)))
                    side_length_inrad = in_radius * (2 * math.tan(math.radians(180 / n)))
                    half_inrad_side = side_length_inrad / 2
                    directions_digit()
                elif directions == 'O':
                    directions_O()
                elif 'o' in directions:
                    directions_o()
                elif directions == 'e':
                    directions_exit()
                else:
                    question()
                count += 1

            elif count > 1:
                t.hideturtle()
                keyboard.wait('space')
                t.showturtle()
                question()
                if directions is None:
                    exit()
                elif directions.isdigit():
                    n = int(directions)
                    circum_radius = 250
                    in_radius = circum_radius * math.cos(math.radians(180 / n))
                    interior_theta = ((n - 2) * 180) / n
                    half_interior_theta = interior_theta / 2
                    side_length_circum = circum_radius * (2 * math.sin(math.radians(180 / n)))
                    side_length_inrad = in_radius * (2 * math.tan(math.radians(180 / n)))
                    half_inrad_side = side_length_inrad / 2
                    directions_digit()
                elif directions == 'O':
                    directions_O()
                elif 'o' in directions:
                    directions_o()
                elif directions == 'u':
                    directions_undo()
                elif directions == 'c':
                    directions_c()
                elif directions == 'e':
                    directions_exit()

        except (_tkinter.TclError, turtle.Terminator, NameError) as error:
            if error:
                exit()


tPolygon()
