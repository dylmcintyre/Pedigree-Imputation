"""Main module."""

individuals= []

class Individual:
    def __init__ (self, pedigree_numb, id_numb, father,  mother, sex, age= None):
        self.pedigree_numb = pedigree_numb
        self.sex = sex
        self.age = age
        self.father = father
        self.mother = mother
        self.id_numb = id_numb
        
        @property
        def siblings(self):
            siblings= []
            for x in individuals:
                if self.father == x[2] and self.mother == x[3]:
                    siblings.append(x[2])
                    #adds sibling ID numbers to list
             
class Pedigree:
    def __init__ (self, individuals):
            self.individuals = dict()
    def print_info(self, filename):
         # print the pedigree information
         return[]
               
def import_ped(pedfile, mapfile):
    with open(pedfile,'r') as file:
        for line in file:
            data_list=line.split()
            individuals.append(Individual(data_list[0], data_list[1], data_list[2], data_list[3], data_list[4]))
                # not passing in age right now because I am not sure which column it is in.
            
