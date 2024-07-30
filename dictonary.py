# dictonary = a changeable, unordered collection of unique key: value pairs
#             Fast because they use hashing, allow us to access a value quickly

capitals = {'Guerrero':'Chilpancingo',
            'Argentina': 'Buenos Aires',
            'Colombia': 'medellin',
            'Usa':'Washintong DC',
            'China': 'Beijing'
            }

# capitals.update({'Germnay':'Berlin'})
# capitals.update({'Guerrero':'Iguala'})
# capitals.pop('Usa')
capitals.clear()
# print(capitals['Guerrero'])
# print(capitals.get('Germany'))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

for key,value in capitals.items():
    print(f"{key} : {value}")