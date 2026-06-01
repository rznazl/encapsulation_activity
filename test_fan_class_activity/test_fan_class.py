class Fan:
    SLOW_MODE = 1
    MEDIUM_MODE = 2
    FAST_MODE = 3

    def __init__(self, speed=SLOW_MODE, radius =5.0, color="blue", on=False):
        self.__speed = speed
        self.__radius = float(radius)
        self.__color = str(color)
        self.__on = bool(on)
    def get_speed(self):
        return self.__speed

    def is_on(self):
        return self.__on

    def get_radius(self):
        return self.__radius

    def get_color(self):
        return self.__color