from AI import moves
import tkinter as tk
from tkinter import *

def choose_move(fox, built_canvas):
    move_fox_up(fox, built_canvas)


def move_fox_up(fox,built_canvas):
    print("move up")
    built_canvas.move(fox, 0, - 20 )



# break down the list of wolfs to only give those in 2 node range of the fox      
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
        determine_bad_moves(wolfs_in_range,built_canvas,fox,node_size)

def determine_bad_moves(wolfs_in_range,built_canvas,fox,node_size):
    bad_moves = ""
    fox_x, fox_y = convert_to_short_coords(fox,built_canvas, node_size )
    
    ref_for_bad_moves = moves.get_moves(fox_x,fox_y)

    for wolf in wolfs_in_range:
        wolf_x, wolf_y = convert_to_short_coords(wolf, built_canvas, node_size )
        wolf_short_coords = (wolf_x, wolf_y)

        bad_moves += (list(ref_for_bad_moves.keys())[list(ref_for_bad_moves.values()).index(wolf_short_coords)])

    not_useable_moves = " ".join(set(bad_moves))
    print("not usable moves", not_useable_moves)
    
def convert_to_short_coords(animal,built_canvas, node_size):
    x1,y1,x2,y2 = built_canvas.coords(animal)

    x = (x1 / node_size)
    y = (y1 / node_size)

    return x,y 






        






            
        

        
        # getting the current coords
       # test_fox_coords = built_canvas.coords(test_fox)
        

        #print("fox and test wolf", test_fox,test_wolf)
        


        
        