class City:
    def __init__(self, city, region, country, people):
        self.city = city
        self.region = region
        self.country = country
        self.people = people

object = City('New York', 'State Island','USA', 5000000)
print('city:', object.city, 'region:', object.region, 'country:', object.country, 'people:', object.people)
