# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file´s creation and modification times)

import shutil

# shutil.copyfile('C:\\Users\\20\\Documents\\30\\proyecto.txt','copy.txt') #src.dst
# shutil.copy('C:\\Users\\20\\Documents\\30\\proyecto.txt','copy.txt') #src.dst
shutil.copy2('C:\\Users\\20\\Documents\\30\\proyecto.txt','copy.txt') #src.dst
