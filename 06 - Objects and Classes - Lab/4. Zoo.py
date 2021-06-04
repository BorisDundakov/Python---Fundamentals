class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "bird":
            self.birds.append(name)
        elif species == "fish":
            self.fishes.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        if species == "mammal":
            return f"{species.capitalize()}s in {self.zoo_name}: {', '.join(self.mammals)}\nTotal animals: {Zoo.__animals} "

        elif species == "bird":
            return f"{species.capitalize()}s in {self.zoo_name}: {', '.join(self.birds)}\nTotal animals: {Zoo.__animals} "

        if species == "fish":
            return f"{species.capitalize()}es in {self.zoo_name}: {', '.join(self.fishes)}\nTotal animals: {Zoo.__animals} "



outside_class_zoo_name = input()
zoo = Zoo(outside_class_zoo_name)

number = int(input())
zoo_kvp = {}
for el in range(number):
    species, name = input().split()
    zoo.add_animal(species, name)

final_spiecie = input()

print(zoo.get_info(final_spiecie))
