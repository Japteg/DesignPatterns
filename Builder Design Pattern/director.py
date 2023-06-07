from builder import PizzaBuilder


class NonVegOverloadedPizza:

    def __init__(self):
        # self.builder = PizzaBuilder()
        pass

    def construct(self):
        return PizzaBuilder().set_pizza_size(10)\
            .make_thin_crust()\
            .add_topping('Chicke Tikka')\
            .add_oregano()\
            .add_topping('Chicken Kebab')\
            .add_topping('Onion')\
            .add_extra_cheese()\
            .get_pizza()


class VegOverloadedPizza:

    def __init__(self):
        # self.builder = PizzaBuilder()
        pass

    def construct(self):
        return PizzaBuilder().set_pizza_size(10)\
            .add_topping('Panner') \
            .add_oregano() \
            .add_topping('Baby corn') \
            .add_topping('Onion') \
            .add_extra_cheese() \
            .get_pizza()