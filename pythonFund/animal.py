class Animal:
    def __init__(self, name, health):
        self.name = name 
        self.health = health
    def walk(self):
        self.health -=1
        return self 
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print("Health level ", self.health)
        return self 
frog = Animal('frog', 50)
frog.walk().walk().walk().run().run().display_health()
class Dog(Animal):
    def __init__(self, name, health):
        super().__init__(name, health)
        self.health = 150
    def pet(self):
        self.health +=5
        return self
Ares = Dog('Ares', 150)
Ares.walk().walk().walk().run().run().pet().display_health()
class Dragon(Animal):
    def __init__(self, name, health):
        super().__init__(name, health)
        self.health = 170
    def fly(self):
        self.health -= 10
        return self
    def display_health(self):
        super().display_health()
        print("I am a Dragon")
        return self
Drako = Dragon("Drako", 150)
Drako.fly().fly().run().walk().display_health()
