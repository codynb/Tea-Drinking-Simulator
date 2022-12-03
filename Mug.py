#Cody Brown, Mug Project, 02 Dec 2022

#Stage 1: making the teaMug class
class teaMug:
    """Represents a mug of tea


    attributs: height, radius, material, handle, color, shape,
    empty_weight, thickness, capacity"""

mug = teaMug

#Attributes
mug.height = 4 #in inches
mug.radius = 2 #in inches
mug.material = 'pottery'
mug.handle = True
mug.color = 'red'
mug.shape = 'Cylinder'
mug.empty_weight = 8 #in ounces
mug.thickness = .25 #in inches
mug.capacity = 4 #in cups

#Stage 2: tea drinking simulation
import time

def prt_list(list):
    for j in list:
        print(j, flush=True)
        if len(j) < 70:
            time.sleep(2)
        else:
            time.sleep(3)

giving_mug = ['Here is a nice mug that has 4 cups of tea inside!',
            'There there, go ahead and drink some!']

prt_list(giving_mug)

def tea_drinking_simulation(x):
    if 0<= x <= 4:
        tea_remaining = mug.capacity - x
        return f'There are {tea_remaining} cups left'
    else:
        return 'That is impossible!'


x = int(input("How much tea did you drink (in cups)\n"))

print(tea_drinking_simulation(x))
