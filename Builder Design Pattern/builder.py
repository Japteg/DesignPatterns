import abc
from pizza import Pizza


class BuilderInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def set_pizza_size(self, size: int):
        pass

    @abc.abstractmethod
    def add_extra_cheese(self):
        pass

    @abc.abstractmethod
    def add_topping(self, topping: str):
        pass

    @abc.abstractmethod
    def add_oregano(self):
        pass

    @abc.abstractmethod
    def make_thin_crust(self):
        pass

    @abc.abstractmethod
    def get_pizza(self):
        pass


class PizzaBuilder(BuilderInterface):

    def __init__(self):
        self._product = Pizza()

    def set_pizza_size(self, size: int):
        self._product.set_size(size)
        return self

    def add_extra_cheese(self):
        self._product.add_item('Extra cheese')
        return self

    def add_topping(self, topping: str):
        self._product.add_item(topping)
        return self

    def add_oregano(self):
        self._product.add_item('Oregano')
        return self

    def make_thin_crust(self):
        self._product.set_crust('Thin')
        return self

    def get_pizza(self):
        return self._product
