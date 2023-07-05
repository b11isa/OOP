class Country:
    def __init__(self, name, continent, people, capital, code):
        self.name = name
        self.continent = continent
        self.people = people
        self.capital = capital
        self.code = code

object = Country('USA', 'AMERICA','VAWE MNOGO', 'WASHINGTON', '+1')
print('name:', object.name, 'continent:', object.continent, 'people:', object.people, 'capital:', object.capital, 'code:', object.code)