#OPPS CONCEPT ARE
# ARE.ENCAPSULATION,ABSTRACTION,POLYMORPHISM,INHERITANCE,OBJECT AND CLASSES
#1 CLASSES are blueprint
#2 OBJECT  are real world entitu created from class
# oops concepts basically mean every obj created have features
#...Encapsulation: it means the class varibales and fuct used are closed within a closed
#bluesprint.it means wrapping or biding data variables with the method

class Car:
    name = None

    def __init__(self,name): # constructor
        self.name = name

    def printName(self):
        print(self.name)

Xuv = Car("XUV")
Xuv.printName() #from line 15, encapsulation has taken place
# def printname is binding with xuv Car

honda = Car("Honda")
honda.printName()

#encapsulation is also used to hide importannt variables



