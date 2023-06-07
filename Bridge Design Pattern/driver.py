from shape import Square, Circle


def my_func():

    square = Square(5)
    square.draw_in_green()

    circle = Circle(0, 0, 5)
    circle.draw_in_red()
    circle.draw_in_blue()


my_func()