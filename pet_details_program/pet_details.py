class Pet:
    def __init__(self):
        self.__name = ""
        self.__animal_type = ""
        self.__age = 0

    def set_name(self, name):
        self.__name = str(name)

    def set_animal_type(self, animal_type):
        self.__animal_type = str(animal_type)

    def set_age(self, age):
        try:
            self.__age = int(age)
        except ValueError:
            print("Warning: Age must be a number.")
            self.__age = 0

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

if __name__ == "__main__":
    my_pet = Pet()

    print("--- Enter your Pet's details ---")

    pet_name = input("Enter your pet's name: ")
    my_pet.set_name(pet_name)

    pet_type = input("Enter what animal your pet is: ")
    my_pet.set_animal_type(pet_name)

    pet_age = input("Enter your pet's age: ")
    my_pet.set_age(pet_age)

    print("\n" + "=" * 35)
    print("--- Retrieving Stored Pet Data ---")
    print("=" * 35)

    print(f"Pet Name:         {my_pet.get_name()}")
    print(f"Animal Type:      {my_pet.get_animal_type()}")
    print(f"Age of Pet:       {my_pet.get_age()}")