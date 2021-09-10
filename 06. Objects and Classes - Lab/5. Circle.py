class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = float(diameter) / 2

    def calculate_circumference(self):
        circumfence = 2 * self.__pi * float(self.radius)
        return circumfence

    def calculate_area(self):
        circle_area = self.__pi * float(diameter ^ 2)
        return circle_area

    def calculate_area_of_sector(self, angle):
        area_of_sector = self.radius ** 2 * angle / 2
        return area_of_sector


diameter = input()
angle = input()
circle = Circle(10)

print(f"{circle.calculate_circumference():.2f}")
# print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")


