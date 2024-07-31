try:
    with open('C:\\Users\\20\\Documents\\30\\proyecto.txt') as files:
        print(files.read())
except FileNotFoundError:
    print("That file was not found")

