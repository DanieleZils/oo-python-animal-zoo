from lib.animal import Animal

class Zoo:
    
    all = []

    def __init__(self, name, location):
        self.name = name
        self.location = location
        Zoo.all.append(self)


    @property
    def animals(self):
        return [a for a in Animal.all_animals if a.zoo == self]
    
    @property
    def animal_species(self):
        return list ( { a.species for a in self.animals} )
        # species_list = []
        # for animal in self.animals:
        #     if animal.species not in species_list:
        #         species_list.append(animal.species)
        # return species_list

    def find_by_species( self, species ):
        return [ a for a in self.animals if a.species == species ]
    
    @property
    def animal_nicknames( self ):
        return [ a.nickname for a in self.animals ]


    # def animal_nicknames(self):
    #     nicknames_list = []
    #     for animal in self.animals:
    #         nicknames_list.append(animal.nickname)
    #     return nicknames_list

    # def find_by_species(self, species):
    #     animal_list = []
    #     for animal in self.animals:
    #         if animal.species == species:
    #             animal_list.append(animal)
    #     return animal_list

    @classmethod
    def find_by_location(cls, location):
        return [ z for z in cls.all if z.location == location ]
        # zoo_list = []
        # for zoo in cls.all:
        #     if zoo.location == location:
        #         zoo_list.append(zoo)
        # return zoo_list
    