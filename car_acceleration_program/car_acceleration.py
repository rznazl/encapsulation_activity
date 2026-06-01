class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5
        if self.__speed < 0:
            self.__speed = 0

    def get_speed(self):
        return self.__speed

    def get_year_model(self):
        return self.__year_model

    def get_make(self):
        return self.__make

if __name__ == "__main__":
    my_car = Car("2024", "Porsche")

    print(f"Testing the Car Class for a {my_car.get_year_model()} {my_car.get_make()}:\n")
    