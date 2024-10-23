class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        pass

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        return "Woof!"

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        return "Meow!"

class Bird(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.species = species

    def speak(self):
        return "Tweet!"

dog = Dog("Buddy", 3, "Golden Retriever")
print(dog.speak())  # Output: Woof!

cat = Cat("Whiskers", 5, "White")
print(cat.speak())  # Output: Meow!

bird = Bird("Polly", 2, "Parrot")
print(bird.speak())  # Output: Tweet!


