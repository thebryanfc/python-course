class Animal:
    alive = True

    def eat(self):
        print("This animal is eating")
    def sleep(self):
        print("This animal is sleeping")

class dog (Animal):
    print("This dog is running")

class cat (Animal):
    print("This ")

class lion (Animal):
    pass

Dog = dog()
Cat = cat()
Lion = lion()

print(dog.alive)
Cat.eat()
Lion.sleep()
