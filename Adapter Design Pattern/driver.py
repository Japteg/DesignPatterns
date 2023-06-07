from dog import Dog, DogInterface
from adapter import BirdAdapter


def game_controller(player: DogInterface):
    player.walk('Point A', 'Point B')


dog = Dog()
game_controller(dog)
print('\n')
bird_adapter = BirdAdapter()
game_controller(bird_adapter)
