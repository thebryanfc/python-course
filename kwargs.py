#**kwargs = parameter that will pack all arguments into a dictionary
#        useful so that a function can accept a varying amount of keyword arguments

def hello(**kwargs):
    # print(f"Hello {kwargs['first']} {kwargs['last']}")
    print("hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ") 
hello(title="Engineer" ,first="bryan", middle="yaziel", last="figueroa")