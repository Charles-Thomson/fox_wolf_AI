from AI import moves
import tkinter as tk
from tkinter import *

def choose_move(fox, built_canvas):
    move_fox_up(fox, built_canvas)


def move_fox_up(fox,built_canvas):
    print("move up")
    built_canvas.move(fox, 0, - 20 )


    # This shows that we can pull fox from list , get its coords and move it and it will save it back into the array     
def fox_detect_in_range(alive_fox_locations,alive_wolf_locations,built_canvas, node_size):
        # currently only using one fox
        fox = alive_fox_locations[0]
        fox_x1,fox_y1,fox_x2,fox_y2 = built_canvas.coords(fox)

        wolfs_in_range = set()

        for wolf in alive_wolf_locations:
            wolf_x1,wolf_y1,wolf_x2,wolf_y2 = built_canvas.coords(wolf)

            if wolf_x1 in range(int(fox_x1 - 60),int(fox_x1 + 60) ) and wolf_y1 in range(int(fox_y1 - 60),int(fox_y1 + 60)):
                wolfs_in_range.add(wolf)

            if wolf_x2 in range(int(fox_x2 - 60),int(fox_x2 + 60) ) and wolf_y2 in range(int(fox_y2 - 60),int(fox_y2 + 60)):
                wolfs_in_range.add(wolf)
        
        print("wolfs in range",wolfs_in_range)
        determine_move_priority(wolfs_in_range,built_canvas,fox,node_size)

def determine_move_priority(wolfs_in_range,built_canvas,fox,node_size):
    possible_moves = []
    
    fox_x, fox_y = convert_to_short_coords(fox,built_canvas, node_size )
    
    # All fox move prioritys
    move_prioritys = moves.get_moves(fox_x,fox_y)

    for wolf in wolfs_in_range:
        wolf_x, wolf_y = convert_to_short_coords(wolf, built_canvas, node_size )
        wolf_short_coords = (wolf_x, wolf_y)
        print("wolf coords: ",wolf_short_coords,"Fox coords: ",fox_x,fox_y )

        # this works
        move = (list(move_prioritys.keys())[list(move_prioritys.values()).index(wolf_short_coords)])
        possible_moves.append(move)

    print(possible_moves)
    
            
        
#    for wolf in wolfs_in_range:
#        wolf_x1,wolf_y1,wolf_x2,wolf_y2 = built_canvas.coords(wolf)
#
#        # Prioritty 1 - Wolf is one move away from fox
#        
#        # One node right
#        if (wolf_x1 == fox_x1 + 20) and (wolf_y1 == fox_y1):
#            possible_moves.append("R1")
#
#        # One node left
#        if (wolf_x1 == fox_x1 - 20) and (wolf_y1 == fox_y1):
#            possible_moves.append("L1")
#
#        # One node down
#        if (wolf_x1 == fox_x1) and (wolf_y1 == fox_y1 + 20):
#            possible_moves.append("D1")
#
#        # One node up
#        if (wolf_x1 == fox_x1) and (wolf_y1 == fox_y1 - 20):
#            possible_moves.append("U1")
#
# Prioritty 2 - Wolf is two move(s) away from fox
    
def convert_to_short_coords(animal,built_canvas, node_size):
    x1,y1,x2,y2 = built_canvas.coords(animal)

    x = (x1 / node_size)
    y = (y1 / node_size)

    return x,y 






        






            
        

        
        # getting the current coords
       # test_fox_coords = built_canvas.coords(test_fox)
        

        #print("fox and test wolf", test_fox,test_wolf)
        


        
        