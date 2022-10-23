from random import betavariate
import turtle


def draw_body(skk):
    body_length = 20
    body_width = 5
    for x in range(5):
        skk.forward(15)
        skk.right(18)

    for x in range(5):
        skk.forward(body_length)

    for x in range(5):
        skk.forward(15)
        skk.right(18)

    for x in range(5):
        skk.forward(body_width)

    for x in range(5):
        skk.forward(15)
        skk.right(18)

    for x in range(5):
        skk.forward(body_length)

    print(skk.pos())

    for x in range(5):
        skk.forward(15)
        skk.right(18)

    for x in range(5):
        skk.forward(body_width)

    print(skk.pos())


def draw_head(skk):
    skk.penup()
    skk.goto(-10, 73)
    skk.pendown()
    for x in range(20):
        skk.forward(13)
        skk.right(20)


def draw_tail(skk):
    skk.penup()
    skk.goto(-5.85, -195)
    skk.pendown()
    skk.setheading(270)
    skk.forward(60)


def draw_left_leg(skk, position):
    legCoordinates = ()
    if position == 1:
        legCoordinates = (-64.85, -54.85)
    elif position == 2:
        legCoordinates = (-64.85, -94.85)
    else:
        legCoordinates = (-64.85, -144.85)

    skk.penup()
    skk.goto(legCoordinates)
    skk.pendown()
    skk.setheading(180)
    skk.forward(30)
    skk.left(30)
    skk.forward(60)


def draw_left_leg_top(skk): draw_left_leg(skk, 1)
def draw_left_leg_middle(skk): draw_left_leg(skk, 2)
def draw_left_leg_bottom(skk): draw_left_leg(skk, 3)


def draw_right_leg(skk, position):
    legCoordinates = ()
    if position == 1:
        legCoordinates = (54.85, -54.85)
    elif position == 2:
        legCoordinates = (54.85, -94.85)
    else:
        legCoordinates = (54.85, -144.85)

    skk.penup()
    skk.goto(legCoordinates)
    skk.pendown()
    skk.setheading(0)
    skk.forward(30)
    skk.right(30)
    skk.forward(60)


def draw_right_leg_top(skk): draw_right_leg(skk, 1)
def draw_right_leg_middle(skk): draw_right_leg(skk, 2)
def draw_right_leg_bottom(skk): draw_right_leg(skk, 3)


def draw_left_eye(skk):
    skk.penup()
    skk.goto(-15, 55)
    skk.pendown()
    for x in range(20):
        skk.forward(3)
        skk.right(20)


def draw_right_eye(skk):
    skk.penup()
    skk.goto(20, 50)
    skk.pendown()
    for x in range(20):
        skk.forward(3)
        skk.right(20)


def draw_left_antenna(skk):
    skk.penup()
    skk.goto(-20, 70)
    skk.setheading(160)
    skk.pendown()
    skk.forward(50)


def draw_right_antenna(skk):
    skk.penup()
    skk.goto(10, 70)
    skk.setheading(30)
    skk.pendown()
    skk.forward(50)


class BeetleParts:
    BODY = {"key": "BODY", "draw": draw_body}

    HEAD = {"key": "HEAD", "draw": draw_head}

    LEFT_LEG_TOP = {"key": "LEFT_LEG_TOP", "draw": draw_left_leg_top}
    LEFT_LEG_MIDDLE = {"key": "LEFT_LEG_MIDDLE", "draw": draw_left_leg_middle}
    LEFT_LEG_BOTTOM = {"key": "LEFT_LEG_BOTTOM", "draw": draw_left_leg_bottom}

    RIGHT_LEG_TOP = {"key": "RIGHT_LEG_TOP", "draw": draw_right_leg_top}
    RIGHT_LEG_MIDDLE = {"key": "RIGHT_LEG_MIDDLE",
                        "draw": draw_right_leg_middle}
    RIGHT_LEG_BOTTOM = {"key": "RIGHT_LEG_BOTTOM",
                        "draw": draw_right_leg_bottom}

    TAIL = {"key": "TAIL", "draw": draw_tail}

    LEFT_ANTENNA = {"key": "LEFT_ANTENNA", "draw": draw_left_antenna}
    RIGHT_ANTENNA = {"key": "RIGHT_ANTENNA", "draw": draw_right_antenna}

    LEFT_EYE = {"key": "LEFT_EYE", "draw": draw_left_eye}
    RIGHT_EYE = {"key": "RIGHT_EYE", "draw": draw_right_eye}


def draw_beetle(parts, title="hello"):
    window = turtle.Screen()
    turtle.TurtleScreen._RUNNING = True
    window.bgcolor("white")
    window.title(title)
    window.clear()

    skk = turtle.Turtle()

    for part in parts:
        part["draw"](skk)

    turtle.done()
