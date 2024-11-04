class Animal:
    def __init__(self, name, age=0, health_level=50, happiness_level=50):
        self.name = name
        self.age = age
        self.health_level = health_level
        self.happiness_level = happiness_level
        
    
    def display_info(self):
        print("Name:" ,self.name , "Health Level:", self.health_level, "Happiness Level:", self.happiness_level)
     
     
    def feed(self):
        self.happiness_level +=10
        self.health_level+=10
        print(f"{self.name} has been fed. Health and happiness increased!")
           

        