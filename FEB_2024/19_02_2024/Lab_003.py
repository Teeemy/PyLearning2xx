# create a car objct
# Car is the class name
# object - Tesla,Lambo

class Car :
    name = None
    color = None
    model = None
    speed = None
    engine = None

    def start_engine(self):
        print("Starting engine")

    def drive(self):
        print("Drive car")

    def car_break(self):
        print("Car break")

    def who_is_driving(self):
        print("I am driving " + self.name)# self here is an instance variable. it used
                                        #to accesss variable name

tesla_obj_ref = Car()
lambo_obj_ref = Car()

tesla_obj_ref.name = "Tesla"
lambo_obj_ref.name = "Lambo"

tesla_obj_ref.who_is_driving()
lambo_obj_ref.who_is_driving()
