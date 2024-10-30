from Animal import Animal

class Bear(Animal):
    def __init__(self, name, age=0, health_level=50, happiness_level=60):
        super().__init__(name, age, health_level, happiness_level)
        self.hibernation_level = 50  

    def feed(self):
        self.health += 10
        self.happiness += 15  
        print(f"{self.name} the bear is ready for a cozy hibernation!")