import abc
from color import RedColor, BlueColor, ColorInterface, LightRedColor, LightBlueColor


class AbstractFactory(metaclass=abc.ABCMeta):

    @staticmethod
    @abc.abstractmethod
    def get_color(color_name: str):
        pass


class ColorFactory(AbstractFactory):

    @staticmethod
    def get_color(color_name: str = None) -> ColorInterface:
        if color_name == 'red':
            return RedColor()

        if color_name == 'blue':
            return BlueColor()

        raise ValueError


class LightColorFactory(AbstractFactory):

    @staticmethod
    def get_color(color_name: str = None) -> ColorInterface:
        if color_name == 'red':
            return LightRedColor()

        if color_name == 'blue':
            return LightBlueColor()

        raise ValueError


class FactoryProducer:

    @staticmethod
    def get_factory(is_light_color=False) -> AbstractFactory:
        if is_light_color:
            return LightColorFactory()
        else:
            return ColorFactory()

