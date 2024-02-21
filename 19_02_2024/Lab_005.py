# mulitple parameters class

class Mul_parameter:
    name = None

    def print_information(self, first_name, last_name, age):
        print("Your name is:",first_name,"Your last name is:",last_name,"Your age is:",age)

obj_ref = Mul_parameter()
obj_ref.print_information("Mariam","Temitope",32)
