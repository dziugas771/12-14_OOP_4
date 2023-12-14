class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area
        self.is_big = self.check_if_big()

    def check_if_big(self):
        return self.population > 20000000 or self.area > 3000000
Croatia = Country('Croatia', 3998589, 56594)
United_Kingdom = Country('United_Kingdom', 67838492, 242900)
Lithuania = Country('Lithuania', 2710000, 635000)

print(Croatia.is_big)
print(Lithuania.is_big)
print(United_Kingdom.is_big)
