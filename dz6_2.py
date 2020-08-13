class Road:

    def __init__(self, lenght, width):
        self.__lenght = lenght
        self.__width = width


    def mass (self, mass_1kv, depth):
        self.mass_1kv = mass_1kv
        self.depth = depth
        total_mass = self.__lenght * self.__width * mass_1kv * depth
        return (f'Общая масса асфальта дорожного полотна с заданными параметрами равна: {total_mass / 1000} т')

road_1 = Road(5000, 20)
print(road_1.mass(25, 5))

