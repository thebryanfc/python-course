# while loop = a statemt that will execute it's block of code,
#               as long as it's condition remains true

name = ""

while len(name) == 0:
    name = input("Enter your name: ")
print(f"Hello {name}")