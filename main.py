# it's a ressource manangement game for the numworks

import kandinsky as ks

buildings : dict ={ #every building in the game stored with their tech lvl requierment, modifier and cost
 "tent":(0,(0.0002,"Population"),(10,"Metal")),
 "campire":(0,(0.0001,"Food"),(10,"Metal")),
 "furnace_basic": (1,(0.0001,"Metal"),(10,"Metal")),
 "field_basic":(1,(0.0005,"Food"),(10,"Metal")),
 "house_basic":(1,(0.0005,"Population"),(10,"Metal")),
 "walls_basic":(2,(0.0005,"Military"),(10,"Metal"))
}


def building(ressources : dict, tech_lvl : int):
    available : list = []
    for name,value in buildings.items():
        if value[0] == tech_lvl and ressources[value[2][1]][0] >= value[2][0]:
            available.append((name,value))
    print(1)
    for i in range(len(available)):
        print(f"{i}. {available[i][0]}")
    print("E. Exit")
    choice = input()
    if choice=="E":
        print("exited")
    else: 
        print(ressources)
        ressources[available[int(choice)][1][2][1]][0] -= available[int(choice)][1][2][0]
        ressources[available[int(choice)][1][2][1]][1] += available[int(choice)][1][1][0]
        print (ressources)




#======================================================================================
def mainloop():
    ressources : dict = {
        "Population" : [0,0.1],
        "Military" : [0,0.1],
        "Metal" : [10,0.1],
        "Food" : [0,0.1],
        "Building_material_age" : [0,0.1],
        "Gold" : [0,0.1],
        #"Energy" : -1,
        #"Fuel" : -1,
    }
    while True:
        for ressource in ressources.values():
            ressource[0] +=round(10*ressource[1])
        building(ressources,1)

mainloop()