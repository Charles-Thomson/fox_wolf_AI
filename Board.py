import tkinter as tk
from tkinter import *
from dataclasses import dataclass

@dataclass
class CanvasData:
    canvas: Canvas
    node_size: int
    canvas_height: int
    canvas_width: int
    number_of_rows: int 
    number_of_columns: int


def BuildCanvas(canvas_height: int, canvas_width: int, node_size: int) -> CanvasData:
    """Building the canvas and returing as part of board data"""

    canvas = Canvas(width = canvas_width, height= canvas_height, bg = "white")
    
    canvas.pack(pady = 20)
    number_of_rows, number_of_columns = CalculateRowsAndColumns(canvas_height, canvas_height, node_size)
    
    for row in range(number_of_rows):
        for col in range(number_of_columns):
            x1 = (col * node_size)
            y1 = (row * node_size)
            x2 = x1 + node_size
            y2 = y1 + node_size
                
            canvas.create_rectangle(x1,y1,x2,y2, outline="black", fill="white")

    return CanvasData(canvas, node_size, canvas_height, canvas_width, number_of_rows, number_of_columns)
    

def CalculateRowsAndColumns(canvas_height: int, canvas_width: int, node_size: int) -> int:
    """Calculate the nnumber of possible rows & columns"""

    number_of_rows = int(canvas_height/node_size)
    number_of_columns = int(canvas_width/node_size)

    return number_of_rows, number_of_columns