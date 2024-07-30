#keyword arguments = arguments preceded by an identifier when we pass them to a function
#               the order of the arguments doesn´t matter, unlike positional arguments
#               python knows the names of the arguments thah our function receives

def hello(first,middle, last):
    print(f"Hello {first} {middle} {last}")
hello(last="figuerao",first="bryan",middle="yaziel")