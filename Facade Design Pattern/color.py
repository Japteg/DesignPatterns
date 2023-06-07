import abc


class ColorInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def paint(self):
        pass


class RedColor(ColorInterface):

    def paint(self):
        print('I paint in RED color')


class BlueColor(ColorInterface):

    def paint(self):
        print('I paint in BLUE color')


class GreenColor(ColorInterface):

    def paint(self):
        print('I paint in GREEN color')