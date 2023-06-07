import abc


class BirdInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def fly(self, point_a, point_b):
        pass


class Bird(BirdInterface):

    def fly(self, point_a, point_b):
        print('flap flap flap flap')
        print(f'I am going from {point_a} to {point_b}')
        print('flap flap flap flap')