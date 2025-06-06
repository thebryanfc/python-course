import os
import shutil

path = "C:\\Users\\20\\Desktop\\proyecto.txt"
try:
    # os.remove(path) #delete a file
    # os.rmdir(path)  # delete an empty directory
    shutil.rmtree(path) # delete a directory containing files
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print(f"{path} was delete")