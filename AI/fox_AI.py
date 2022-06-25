from AI import moves
from AI import AI_supporting_methods
import collections
import tkinter as tk
from tkinter import *

def choose_move(fox, built_canvas,best_move,not_useable_moves):
    if best_move not in not_useable_moves:
        next_move = best_move
        # last_move= next_move 
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

def move_fox(fox,built_canvas, new_x, new_y):
    print("moving fox")
    built_canvas.move(fox, new_x, new_y)

# break down the list of wolfs to only give those in 2 node range of the fox      
def detect_wolfs_in_range_of_fox(alive_fox_locations,alive_wolf_locations,built_canvas, node_size):
        # currently only using one fox
        fox = alive_fox_locations[0]
        wolfs_in_range_of_fox = AI_supporting_methods.detect_animals_in_range(fox, alive_wolf_locations, built_canvas, node_size)
        print("Wolfs in range", wolfs_in_range_of_fox)

        determine_best_and_unusable_moves(wolfs_in_range_of_fox,built_canvas,fox,node_size)

def determine_best_and_unusable_moves(wolfs_in_range,built_canvas,fox,node_size):
    negtive_move_data = ""
    positive_move_data = ""
    fox_short_coords = AI_supporting_methods.convert_to_short_coords(fox,built_canvas, node_size )
    ref_for_moves = moves.get_bad_moves(fox_short_coords)

    for wolf in wolfs_in_range:
        wolf_short_coords = AI_supporting_methods.convert_to_short_coords(wolf, built_canvas, node_size )
        
        print("Fox coords",fox_short_coords,"wolf coords",wolf_short_coords )
        move_data = (list(ref_for_moves.keys())[list(ref_for_moves.values()).index(wolf_short_coords)])
        split_move_data = move_data.split("-")
        positive_move_data += split_move_data[0]
        negtive_move_data += split_move_data[1]

    if positive_move_data == "":
        best_move = ""
    else:
        best_move = find_best_move(list(positive_move_data))

    not_useable_moves = set(negtive_move_data)

    choose_move(fox, built_canvas,best_move,not_useable_moves)

def find_best_move(best_moves):
        return collections.Counter(best_moves).most_common(1)[0][0]

         







        






            
        

        
        # getting the current coords
       # test_fox_coords = built_canvas.coords(test_fox)
        

        #print("fox and test wolf", test_fox,test_wolf)
        


        
        