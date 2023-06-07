from factory import FactoryProducer


def my_func():

    try:
        color_factory = FactoryProducer().get_factory(is_light_color=False)
        color1 = color_factory.get_color('red')
        color1.paint()

        light_color_factory = FactoryProducer().get_factory(is_light_color=True)
        color2 = light_color_factory.get_color('red')
        color2.paint()

    except ValueError as e:
        print("Sorry, I can't get your color!")


if __name__ == '__main__':
    my_func()
