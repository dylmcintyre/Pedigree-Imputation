"""Main module."""

individuals= []

class Individual:
    def __init__ (self, pedigree_numb, id_numb, father, mother, sex, age):
        self.ped=None
        self.pedigree_numb = pedigree_numb
        self.sex = sex
        if(age==0):
            self.age = None
        else:
            self.age=age
        self.father = father
        self.mother = mother
        self.id_numb = id_numb
        
    @property
    def siblings(self):
        siblings= {}
        for id in self.ped.individuals.keys():
            if self.mother ==0 or self.father==0:
                pass
            #this insures Individuals without mother or father values aren't included
            if self.id_numb != self.ped.individuals[id].id_numb and self.mother == self.ped.individuals[id].mother and self.father == self.ped.individuals[id].father:
               siblings[self.id_numb]=self
                #adds sibling to dictionary using id_numb as key
        return(siblings)

    @property
    def impute_age(self):
        count =0
        total=0
        for key in self.siblings.keys():
            count += 1
            total += int (self.siblings[key].age)
        return int (total/count)
#5 refers to the age of the individual



             
class Pedigree:
    def __init__ (self, individuals):
        self.individuals = individuals
        for id in self.individuals:
            individuals[id].ped= self
            #This refers to each individual object and sets their pedigree as the current one.

    def print_info(self, filename):
         # print the pedigree information
         return[]
               
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
print(p.individuals['11'].impute_age)

#6/24 note: problem with impute age function itself