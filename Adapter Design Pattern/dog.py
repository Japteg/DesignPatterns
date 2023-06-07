import abc


class DogInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def walk(self, point_a, point_b):
        pass


class Dog(DogInterface):

    def walk(self, point_a, point_b):
        print('tip tap tip tap tip tap')
        print(f'I am going from {point_a} to {point_b}')
        print('tip tap tip tap tip tap')
