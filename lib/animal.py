class Animal:
    all_animals = []

    def __init__(self, species, weight, nickname, zoo):
        self.species = species
        self.weight = weight
        self.nickname = nickname
        self.zoo = zoo
        Animal.all_animals.append(self)
    

    @classmethod
    def find_by_species(cls, species):
        return [ a for a in cls.all_animals if a.species == species]
        # animal_list = []
        # for animal in cls.all_animals:
        #     if animal.species == species:
        #         animal_list.append(animal)
        # return animal_list
    
