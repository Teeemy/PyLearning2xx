class Mul_parameter:
    name = None # this is a class variable
    

    def print_information(self, first_name, last_name, age):
       # a = 10 # this is a local variable available within this func
        print("Your name is:",first_name,"Your last name is:",last_name,"Your age is:",age)


obj_ref = Mul_parameter()
obj_ref.print_information("Mariam","Temitope",32)
