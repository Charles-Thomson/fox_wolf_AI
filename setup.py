import tkinter as tk
from tkinter import *

import board

def set_up(parent,node_size,board_height,board_width):
        alive_fox_locations = []
        alive_wolf_locations = []

        board_canvas = board.board(parent,node_size,board_height,board_width)
        built_canvas = board_canvas.build_canvas(parent,board_height,board_width,node_size)

        populate_board_with_fox(built_canvas,node_size,alive_fox_locations)
        populate_board_with_wolf(built_canvas, node_size, alive_wolf_locations)

        return alive_fox_locations ,alive_wolf_locations, built_canvas

def populate_board_with_fox(built_canvas,node_size,alive_fox_locations):
        
        alive_fox = draw_fox_at_start_location(5,5,node_size,built_canvas)
        alive_fox_locations.append(alive_fox)

        

        
def populate_board_with_wolf(built_canvas,node_size,alive_wolf_locations):
        #wolf_object = wolf_AI.wolf_AI(built_canvas)
        alive_wolf = draw_wolf_at_start_location(4,4,node_size,built_canvas)
        alive_wolf_locations.append(alive_wolf)

        alive_wolf = draw_wolf_at_start_location(8,4,node_size,built_canvas)
        alive_wolf_locations.append(alive_wolf)

        alive_wolf = draw_wolf_at_start_location(6,4,node_size,built_canvas)
        alive_wolf_locations.append(alive_wolf)

        alive_wolf = draw_wolf_at_start_location(2,4,node_size,built_canvas)
        alive_wolf_locations.append(alive_wolf)


def draw_fox_at_start_location(start_location_x,start_location_y,node_size,board_canvas):
        x1 = start_location_x * node_size
        y1 = start_location_y * node_size
        x2 = x1 + node_size
        y2 = y1 + node_size
        print("Start location",x1,y1,x2,y2)
        
        alive_fox = board_canvas.create_rectangle(x1,y1,x2,y2, fill="blue") 
        
        return alive_fox

def draw_wolf_at_start_location( start_location_x,start_location_y, node_size, board_canvas):
        x1 = start_location_x * node_size
        y1 = start_location_y * node_size
        x2 = x1 + node_size
        y2 = y1 + node_size
        wolf = board_canvas.create_rectangle(x1,y1,x2,y2,fill="red")
        # wolf_location_data = board_canvas.coords(wolf)
        return wolf