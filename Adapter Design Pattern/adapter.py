from dog import DogInterface
from bird import Bird


class BirdAdapter(DogInterface):

    def __init__(self):
        self.bird = Bird()

    def walk(self, point_a, point_b):
        self.bird.fly(point_a, point_b)

