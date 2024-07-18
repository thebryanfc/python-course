# tuple = collection which is ordered and unchangeable 
#         used to group together related data

student = ("bryan", 23, "male")

print(student.count("bryan"))
print(student.index("male"))

for x in student:
    print(x)

if "bryan" in student:
    print("bryan is here")