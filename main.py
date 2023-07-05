class People:
    def __init__(self, name, birth, number, city):
        self.name = name
        self.birth = birth
        self.number = number
        self.city = city

object = People('Isaac', 19, 998998275044, 'USA')
print('name:', object.name, 'birth:', object.birth, 'number:', object.number, 'city:', object.city)