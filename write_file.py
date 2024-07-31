
text = input("Enter your text: ")

with open ('test.tx','w') as file:
    file.write(text)