class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area
        self.is_big = self.check_if_big()
        self.population_density = self.population / self.area

    def check_if_big(self):
        return self.population > 20000000 or self.area > 3000000

    def compare_population_density(self, other_country):
        if self.population_density > other_country.population_density:
            return f"{self.name} has bigger density"
        elif self.population_density < other_country.population_density:
            return f"{self.name} has less density as {other_country.name}"
        else:
            return f"{self.name} has same density as {other_country.name}"

Croatia = Country('Croatia', 3998589, 56594)
United_Kingdom = Country('United_Kingdom', 67838492, 242900)
Lithuania = Country('Lithuania', 2710000, 635000)

print(Croatia.is_big)
print(Lithuania.is_big)
print(United_Kingdom.is_big)

print(Lithuania.population_density)
print(Croatia.population_density)
print(United_Kingdom.population_density)

print(Lithuania.compare_population_density(Croatia))
