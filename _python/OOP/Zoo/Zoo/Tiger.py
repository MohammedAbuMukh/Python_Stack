from Animal import Animal

class Tiger(Animal):
    def __init__(self, name, age=0, health_level=55, happiness_level=65):
        super().__init__(name, age, health_level, happiness_level)
        self.stripe_count = 80
    
    def feed(self):
        self.health_level+=12
        self.happiness_level+=12
        print(f"{self.name} the tiger is now more vibrant!") 
          

