from color import BlueColor, RedColor, GreenColor


class Painter:

    def __init__(self):
        pass

    @staticmethod
    def paint_red():
        RedColor().paint()

    @staticmethod
    def paint_yellow():
        print('*************** YELLOW ****************')
        RedColor().paint()
        GreenColor().paint()
        print('****************************************')
