from color import RedColor, BlueColor, ColorInterface


class ColorFactory:

    @staticmethod
    def get_color(color_name: str = None) -> ColorInterface:
        if color_name == 'red':
            return RedColor()

        if color_name == 'blue':
            return BlueColor()

        raise ValueError
