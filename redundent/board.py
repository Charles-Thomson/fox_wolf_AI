from platform import node
import tkinter as tk
from tkinter import *
from dataclasses import dataclass

class board():
    def __init__(self,node_size: int ,board_height: int ,board_width: int) -> None:
        self.node_size = node_size
        self.board_height = board_height
        self.board_width = board_width
        self.number_of_rows, self.number_of_columns = self.SetRowsAndColumns(board_height, board_width,node_size)
        

    def SetRowsAndColumns(self,board_height: int, board_width: int, node_size: int ) -> None:
        """Set the number of rows and columns"""

        number_of_rows = int(board_height / node_size)
        number_of_columns = int(board_width / node_size)

        return number_of_rows,number_of_columns

    def BuildCanvas(self,board_height: int,board_width: int ,node_size: int) -> Canvas:
        """Build the Canvas"""

        board_canvas = Canvas(width = board_width, height = board_height, bg = "white")
        board_canvas.pack(pady = 20)
        drawn_board_canvas = self.DrawGrid(self.number_of_rows,self.number_of_columns,node_size,board_canvas)

        return drawn_board_canvas

    def DrawGrid(self,rows: int,columns: int,node_size: int ,board_canvas: Canvas) -> Canvas:
        """Draw the drid onto the canvas"""
        
        for row in range(rows):
            for col in range(columns):
                x1 = (col * node_size)
                y1 = (row * node_size)
                x2 = x1 + node_size
                y2 = y1 + node_size
                
                board_canvas.create_rectangle(x1,y1,x2,y2, outline="black", fill="white")
        return board_canvas
    
    

if __name__ == "__main__":
    root = tk.Tk()
    board = board(root)
    root.mainloop()