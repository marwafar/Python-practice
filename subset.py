def flattent(plants):

    result=[]
    for plant in plants:
        if isinstance(plant,list):
            flat_list=flattent(plant)
            result+=flat_list
        else:
            result.append(plant)

    return result

nested_planets = ['mercury', 'venus', ['earth'], 'mars', \
    [['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]

print(flattent(nested_planets))