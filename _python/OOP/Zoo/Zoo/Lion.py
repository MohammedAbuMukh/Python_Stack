from Animal import Animal

class Lion(Animal):
    def __init__(self, name, age=0, health_level=60, happiness_level=60):
        super().__init__(name, age, health_level, happiness_level)
        self.roar_power = 100
    
    def feed(self):
        self.health_level+=15
        self.happiness_level+=10
        print(f"{self.name} the lion has been fed. Roar power is high!") 
          
        
        