from draw import DrawAPI


class Shape:

    def __init__(self):
        self.draw_api = DrawAPI()


class Circle(Shape):

    def __init__(self, x, y, radius):
        super().__init__()
        self.shape_name = 'Circle'
        self.x = x
        self.y = y
        self.radius = radius

    def draw_in_red(self):
        self.draw_api.draw_red(self.shape_name)

    def draw_in_blue(self):
        self.draw_api.draw_blue(self.shape_name)


class Square(Shape):

    def __init__(self, side_length):
        super().__init__()
        self.shape_name = 'Square'
        self.side_length = side_length

    def draw_in_green(self):
        self.draw_api.draw_green(self.shape_name)
