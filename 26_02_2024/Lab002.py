class Car:
    name = None
    make = None
    model = None

    # def init is a special char that is automatically called whenever
    # obj is created

    def __init__(self, o_name, o_make, o_model):  # paramiterized constructor# constructor is used to change the value
        self.name = o_name
        self.make = o_make
        self.model = o_model

    def start_engine(self):
        print("Starting a car with the name " + self.name)
        print("Starting a car with the make " + self.make)
        print("Starting a car with the model " + self.model)


lambo = Car("lambo", "v2", "2001")  # obj creation
lambo.start_engine()
# when obj is created, def_init func is called to perform the func
print("-----------")
# xuv and lambo obj ae diff but they use same constructor func
Xuv = Car ("XUV", "V6", "2004")
Xuv.start_engine()