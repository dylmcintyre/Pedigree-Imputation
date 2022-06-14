"""Main module."""
class Individual:
    def __init__ (self, pedigree_numb, sex, age, father, mother, id_numb):
        self.pedigree_numb = pedigree_numb
        self.sex = sex
        self.age = age
        self.father = father
        self.mother = mother
        self.id_numb = id_numb
    @property
    def siblings(self):
        
class Pedigree:
    def __init__ (self, individuals):
        self.individuals = dict()
    def print_info(self, filename):
         # print the pedigree information
