import abc


class ColorInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def paint(self):
        pass


class RedColor(ColorInterface):

    def paint(self):
        print('I paint in Red color')


class BlueColor(ColorInterface):

    def paint(self):
        print('I paint in Blue color')
