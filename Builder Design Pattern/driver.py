from director import NonVegOverloadedPizza, VegOverloadedPizza


def pizza_restaurant():
    pizza1 = NonVegOverloadedPizza().construct()
    pizza1.description()

    pizza2 = VegOverloadedPizza().construct()
    pizza2.description()


if __name__ == '__main__':
    pizza_restaurant()
