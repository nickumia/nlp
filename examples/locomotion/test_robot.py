
from robot import Robot2DDot


def test_robot_move_right():
    a = Robot2DDot()
    for i in range(5):
        a.move()

    assert a.getPosition() == [5, 0]


def test_robot_move_up():
    a = Robot2DDot(initial_heading=90)
    for i in range(5):
        a.move()

    assert a.getPosition() == [0, 5]


def test_robot_move_left():
    a = Robot2DDot(initial_heading=180)
    for i in range(5):
        a.move()

    assert a.getPosition() == [-5, 0]


def test_robot_move_down():
    a = Robot2DDot(initial_heading=270)
    for i in range(5):
        a.move()

    assert a.getPosition() == [0, -5]


def test_robot_move_up_down_right():
    a = Robot2DDot(initial_heading=0)
    for i in range(4):
        a.move(30)
        a.move(-30)

    assert a.getPosition() == [7.464, 2.0]
