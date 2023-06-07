from factory import ColorFactory


def my_func():

    try:
        color1 = ColorFactory.get_color('red')
        color1.paint()

        color2 = ColorFactory.get_color('blue')
        color2.paint()

        color3 = ColorFactory.get_color('yellow')
        color3.paint()
    except ValueError as e:
        print("Sorry, I can't get your color!")


if __name__ == '__main__':
    my_func()
