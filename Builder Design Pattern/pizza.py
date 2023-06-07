class Pizza:

    def __init__(self):
        self._ingredients = []
        self._size = 0
        self._crust = 'Thick'

    def set_size(self, size: int):
        self._size = size

    def set_crust(self, crust: str):
        self._crust = crust

    def add_item(self, item: str):
        self._ingredients.append(item)

    def description(self):
        print('******** Your Pizza Summary *********')
        print(f'Your pizza is of size {self._size}')
        print(f'Your pizza has {self._crust} crust')
        print('Pizza ingredients are as follows: ')
        for index, item in enumerate(self._ingredients):
            print(f'{index+1}: {item}')
        print(f'Total items: {len(self._ingredients)}')

