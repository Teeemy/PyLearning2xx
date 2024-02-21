class Car: # class
    color = None
    model = None
    year = None

    def car_details(self):
        print("Your car details is", self.color, self.model,self.year) # method

car_color = input("Enter your car Color \n") # getting details frm user
car_model = input("Enter your car Model \n")
car_year = input("Enter your car Year \n")

# creating a car obj ref
car_obj_ref = Car()

# set value of the car details
car_obj_ref.color = car_color
car_obj_ref.model = car_model
car_obj_ref.year = car_year

car_obj_ref.car_details()

