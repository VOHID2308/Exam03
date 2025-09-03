class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name}"

class Dog(Animal):
    def bark(self):
        return f"Woof! Woof!"

d = Dog("Rex")
print(d.name)
print(d.bark())