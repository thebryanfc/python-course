#str.format() = optional method that gives users
#               more control when displaying output

animal = "cow"
item = "moon"

# print("The "+animal+" jumped over the "+item)
# print(f"The {animal} jumped over the {item}")
# print("The {} jumped over the {}".format(animal,item)) 
#print("The {0} jumped over the {1}".format(animal,item)) #positional argument
print("The {animal} jumped over the {item}".format(animal="cow",item="moon"))#keyword argument