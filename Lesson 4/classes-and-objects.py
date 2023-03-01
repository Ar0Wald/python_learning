class ToyCar:
    def __init__(self, color, model):
        self.color = color
        self.model = model
        self.is_running = False

    def start(self):
        self.is_running = True
        print("The", self.color, self.model,"has started.")

    def stop(self):
        self.is_running = False
        print("The", self.color,self.model,"has stopped.")

my_red_car = ToyCar("red", "Ferrari")

my_red_car.start()
my_red_car.stop()