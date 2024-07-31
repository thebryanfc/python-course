import os 

source = "C:\\Users\\20\\Documents\\30\\proyecto.txt"
destination = "C:\\Users\\20\\Desktop\\proyecto.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print(f"{source} was moved")
except FileNotFoundError:
    print(f"{source} was not found")