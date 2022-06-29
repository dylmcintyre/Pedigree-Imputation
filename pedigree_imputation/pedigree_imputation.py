"""Main module."""


import faulthandler


class Individual:
    def __init__ (self, pedigree_numb, id_numb, father, mother, sex, age):
        self.ped=None
        self.pedigree_numb = pedigree_numb
        self.sex = sex
        self.age = age
        self.father = father
        self.mother = mother
        self.id_numb = id_numb
        
    @property
    def siblings(self):
        siblings= {}
        for ind in self.ped.individuals.values():
            if self.mother ==0 or self.father==0:
                pass
            #this insures Individuals without mother or father values aren't included
            if self.id_numb != ind.id_numb and self.mother == ind.mother and self.father == ind.father:
               siblings[ind.id_numb]=ind
                #adds sibling to dictionary using id_numb as key
        return(siblings)

    def impute_age(self):
        if int (self.age) != 0:
            return(self.age)
        elif len(self.siblings) == 0:
            return(0)
        else:
            count =0
            total=0
            s= self.siblings
            for sib in s.values():
                count += 1
                total += int (sib.age)
            return int (total/count)
#5 refers to the age of the individual



             
class Pedigree:
    def __init__ (self, individuals):
        self.individuals = individuals
        for id in self.individuals:
            individuals[id].ped= self
            #This refers to each individual object and sets their pedigree as the current one.

    def print_info(self, filename=None):
         for ind in self.individuals.values():
            print(ind.pedigree_numb + " " + ind.id_numb + " " + ind.father + " " + ind.mother + " " + ind.sex + " " + str(ind.age))
         return[]
    
    def impute_age(self):
        for ind in self.individuals.values():
            ind.age=ind.impute_age()
            
               
def import_ped(pedfile, mapfile = None):
    individuals= {}
    with open(pedfile,'r') as file:
        for line in file:
            data_list=[]
            data_list=line.split()
            individuals[data_list[1]]=Individual(data_list[0], data_list[1], data_list[2], data_list[3], data_list[4], data_list[5])
                # This puts each object into the dictionary with ID_numb as the key.
    return(Pedigree(individuals))




p= import_ped("Fam12.ped")
p.impute_age()
p.print_info()