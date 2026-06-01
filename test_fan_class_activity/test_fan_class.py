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

    def set_speed(self, speed):
        if speed in[Fan.SLOW_MODE, Fan.MEDIUM_MODE, Fan.FAST_MODE]:
            self.__speed = speed
        else:
            raise ValueError("Invalid speed value")

    def set_on(self, on):
        self.__on = bool(on)

    def set_radius(self, radius):
        self.__radius = float(radius)

    def set_color(self, color):
        self.__color = str(color)

    def display_info(self):
        state = "ON" if self.__on else "OFF"
        print(f"Speed: {self.__speed} | Radius: {self.__radius} | Color: {self.__color} | State: {state}")

if __name__ == "__main__":
    first_fan = Fan()
    first_fan.set_speed(Fan.FAST_MODE)
    first_fan.set_radius(10.0)
    first_fan.set_color("Yellow")
    first_fan.set_on(True)

    second_fan = Fan()
    second_fan.set_speed(Fan.MEDIUM_MODE)
    second_fan.set_radius(5.0)
    second_fan.set_color("Blue")
    second_fan.set_on(False)

    print("First Fan Properties: ")
    first_fan.display_info()

    print("\nSecond Fan Properties: ")
    second_fan.display_info()