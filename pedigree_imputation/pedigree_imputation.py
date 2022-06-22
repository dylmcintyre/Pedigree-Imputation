"""Main module."""

individuals= []

class Individual:
    def __init__ (self, pedigree_numb, id_numb, father,  mother, sex, age= None):
        self.ped=None
        self.pedigree_numb = pedigree_numb
        self.sex = sex
        self.age = age
        self.father = father
        self.mother = mother
        self.id_numb = id_numb
        
    @property
    def siblings(self):
        siblings= []
        for ind in self.ped.individuals:
            if self.id_numb != ind.id_numb and self.mother == ind.mother and self.father == ind.father:
               siblings.append(ind)
                #adds sibling to list
        return(siblings)
             
class Pedigree:
    def __init__ (self, individuals):
        self.individuals = individuals
        for ind in self.individuals:
            ind.ped= self


    def print_info(self, filename):
         # print the pedigree information
         return[]
               
def import_ped(pedfile, mapfile = None):
    individuals= []
    with open(pedfile,'r') as file:
        for line in file:
            data_list=line.split()
            individuals.append(Individual(data_list[0], data_list[1], data_list[2], data_list[3], data_list[4]))
                # not passing in age right now because I am not sure which column it is in.
    return(Pedigree(individuals))





#for testing(will delete)
"""p= import_ped("Fam12.ped")
s= p.individuals[0].siblings
for ind in s:
    print(ind.id_numb)
        """