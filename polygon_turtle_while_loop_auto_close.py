import turtle as t
import math
import keyboard as k
import time


def tPolygon():

    count = 1
    while True:
        if count == 1:

            # turtle and screen setup
            t.title('Frankie the Turtle Draws Regular Polygons')
            t.setup(width=800, height=500, startx=0, starty=0)
            t.mode(mode='standard')
            t.bgcolor('chartreuse')
            t.shape('turtle')
            t.shapesize(stretch_wid=1.1, stretch_len=1.1)
            t.speed(1)
            t.pensize(3)

            # For user input
            m = t.textinput('Help Frankie!', 'Frankie the Turtle wants to draw a regular polygon.\n'
                            'Help him decide how many sides it should have!\n\n'
                            '*minimum of 3 sides*\n\n'
                            'When finished either:\n'
                            "1) hit 'enter' to help Frankie draw another regular polygon!\n"
                            '2) simply wait to discontinue.\n')
            n = int(m)
            angles = ((n - 2) * 180) / n
            sides = (n * n)

            # turtle color
            if n % 2 == 0:
                t.color('blue')
            elif n % 2 != 0:
                t.color('black')

            # polygon
            t.penup()
            '''uses formula for circumradius to center regular polygon (Rc = s / (2sin(pi/n)))'''
            t.setposition(0, sides / (2 * math.sin(math.pi / n)))
            for i in range(n):
                if i == 0:
                    t.setheading(270 - (angles / 2))
                    t.pendown()
                    t.forward(sides)
                else:
                    t.left(180 - angles)
                    t.forward(sides)

            # while loop for ending or repeating
            t.hideturtle()
            start_time = time.time()
            while True:
                end_time = time.time()
                if end_time - start_time > 5:

                    # Frankie says goodbye
                    t.reset()
                    t.hideturtle()
                    t.penup()
                    t.setposition(0, 50)
                    t.bgcolor('black')
                    t.color('chartreuse')
                    t.pendown()
                    t.hideturtle()
                    style = ('Impact', 70, 'normal')
                    t.write(arg='Frankie says:', move=False, font=style, align='center')
                    t.penup()
                    t.hideturtle()
                    t.setposition(0, -70)
                    t.pendown()
                    time.sleep(1)
                    t.write(arg='"Goodbye, friend!"', move=False, font=style, align='center')
                    time.sleep(2)
                    exit()
                else:
                    if k.is_pressed('enter'):
                        count += 1
                        break
                    else:
                        continue

        elif count > 1:
            while True:

                # turtle and screen setup
                t.reset()
                t.title('Frankie the Turtle Draws Regular Polygons')
                t.setup(width=800, height=500, startx=0, starty=0)
                t.mode(mode='standard')
                t.bgcolor('chartreuse')
                t.shape('turtle')
                t.shapesize(stretch_wid=1.1, stretch_len=1.1)
                t.speed(1)
                t.pensize(3)

                # For user input
                m = t.textinput('Help Frankie!', 'Frankie the Turtle wants to draw a regular polygon.\n'
                                                 'Help him decide how many sides it should have!\n\n'
                                                 '*minimum of 3 sides*\n\n'
                                                 'When finished either:\n'
                                                 "1) hit 'enter' to help Frankie draw another regular polygon!\n"
                                                 '2) simply wait to discontinue.\n')
                n = int(m)
                angles = ((n - 2) * 180) / n
                sides = (n * n)

                # turtle color
                if n % 2 == 0:
                    t.color('blue')
                elif n % 2 != 0:
                    t.color('black')

                # polygon
                t.penup()
                '''uses formula for circumradius to center regular polygon (Rc = s / (2sin(pi/n)))'''
                t.setposition(0, sides / (2 * math.sin(math.pi / n)))
                for i in range(n):
                    if i == 0:
                        t.setheading(270 - (angles / 2))
                        t.pendown()
                        t.forward(sides)
                    else:
                        t.left(180 - angles)
                        t.forward(sides)

                # while loop for ending or repeating
                t.hideturtle()
                start_time = time.time()
                while True:
                    end_time = time.time()
                    if end_time - start_time > 5:

                        # Frankie says goodbye
                        t.reset()
                        t.hideturtle()
                        t.penup()
                        t.setposition(0, 50)
                        t.bgcolor('black')
                        t.color('chartreuse')
                        t.pendown()
                        t.hideturtle()
                        style = ('Impact', 70, 'normal')
                        t.write(arg='Frankie says:', move=False, font=style, align='center')
                        t.penup()
                        t.hideturtle()
                        t.setposition(0, -70)
                        t.pendown()
                        time.sleep(1)
                        t.write(arg='"Goodbye, friend!"', move=False, font=style, align='center')
                        time.sleep(2)
                        exit()
                    else:
                        if k.is_pressed('enter'):
                            count += 1
                            break
                        else:
                            continue
                continue


tPolygon()
