class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"ismi {self.name} va yoshi {self.age}"
    
    def __eq__(self, other): # eq = equal to (==)
        return self.age == other.age
    
    def __ne__(self, other): # eq = equal to (==)
        return self.age != other.age
    
    def __gt__(self, other): # gt = greater than
        return self.age > other.age


p1 = Person("ali", 18)
p2 = Person("vali", 16)

print(p1 != p2)
