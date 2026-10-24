class Planet:
    def __init__(self, name, planet_type, star):
        self.name = name
        self.planet_type = planet_type
        self.star = star

        l = [name, planet_type, star]

        for item in l:
            if not isinstance(item, str):
                raise TypeError('name, planet type, and star must be strings')

        if '' in l:
            raise ValueError('name, planet_type, and star must be non-empty strings')

    def orbit(self):
        return f'{self.name} is orbiting around {self.star}...'

    def __str__(self):
        return f'Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}'

planet_1 = Planet('Earth','terrestrial planet','Sun')
planet_2 = Planet('Mars','terrestrial planet','Sun')
planet_3 = Planet('Jupyter','terrestrial planet','Sun')

print(planet_1)
print(planet_2)
print(planet_3)

print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())