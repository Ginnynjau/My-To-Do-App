#Parent Class
class Pets:
    dogs = []
    
    def __init__(self, dogs):
         self.dogs = dogs

#Parent Class
class Dog:
   def __init__ (self, name, age):
       self.name = name
       self.age = age
       self.is_hungry = True 

   def eat(self):
       self.is_hungry = False

#Instances of dogs
my_dogs = [Dog("Tom", 6), Dog("Fletcher", 7), Dog("Larry", 9)]

my_pets = Pets(my_dogs)

print ("I have {} dogs." .format(len(my_pets.dogs)))
for dog in my_pets.dogs:
    print("{} is {}. " .format(dog.name, dog.age))

print("And they're all mammals, of course.")


are_dogs_hungry = False

for dog in my_pets.dogs:
    dog.eat()
    if dog.is_hungry:
        are_dogs_hungry = True

if are_dogs_hungry:
    print ("My dogs are hungry.")
else:
    print ("My dogs are not hungry.")
