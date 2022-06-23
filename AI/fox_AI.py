from AI import moves
import collections
import tkinter as tk
from tkinter import *

def choose_move(fox, built_canvas,best_move,not_useable_moves):
    if best_move not in not_useable_moves:
        next_move = best_move
        last_move= next_move 
    else:
        # need to implement
        print("find new move")

    match next_move:
        case "1": move_fox(fox,built_canvas,-20,-20)
        case "2": move_fox(fox,built_canvas, 0, -20)
        case "3": move_fox(fox,built_canvas, 20,-20)
        case "4": move_fox(fox,built_canvas,-20, 0)
        case "5": move_fox(fox,built_canvas, 20, 0)
        case "6": move_fox(fox,built_canvas,-20, 20)
        case "7": move_fox(fox,built_canvas, 0 , 20)
        case "8": move_fox(fox,built_canvas, 20, 20)
        case _: print("no best next move")
    
def move_fox_up(fox,built_canvas):
    print("move top left")
    built_canvas.move(fox, -20, - 20 )

def move_fox_left(fox,built_canvas):
    print("move center left")
    built_canvas.move(fox, -20, 0 )

def move_fox(fox,built_canvas, new_x, new_y):
    print("moving fox")
    built_canvas.move(fox, new_x, new_y)



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
        determine_best_and_unusable_moves(wolfs_in_range,built_canvas,fox,node_size)

def determine_best_and_unusable_moves(wolfs_in_range,built_canvas,fox,node_size):
    negtive_move_data = ""
    positive_move_data = ""
    fox_short_coords = convert_to_short_coords(fox,built_canvas, node_size )
    
    ref_for_moves = moves.get_bad_moves(fox_short_coords)

    for wolf in wolfs_in_range:
        wolf_short_coords = convert_to_short_coords(wolf, built_canvas, node_size )
        
        move_data = (list(ref_for_moves.keys())[list(ref_for_moves.values()).index(wolf_short_coords)])
        split_move_data = move_data.split("-")
        positive_move_data += split_move_data[0]
        negtive_move_data += split_move_data[1]

    if positive_move_data == "":
        best_move = ""
        print("no best move")
    else:
        best_move = find_best_move(list(positive_move_data))

    not_useable_moves = set(negtive_move_data)
    
    print("BM:", best_move)

    choose_move(fox, built_canvas,best_move,not_useable_moves)

def find_best_move(best_moves):
        return collections.Counter(best_moves).most_common(1)[0][0]

         
def convert_to_short_coords(animal,built_canvas, node_size):
    x1,y1,x2,y2 = built_canvas.coords(animal)

    x = (x1 / node_size)
    y = (y1 / node_size)

    return (x,y) 






        






            
        

        
        # getting the current coords
       # test_fox_coords = built_canvas.coords(test_fox)
        

        #print("fox and test wolf", test_fox,test_wolf)
        


        
        