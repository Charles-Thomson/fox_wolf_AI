from platform import node
import tkinter as tk
from tkinter import *

class board(tk.Frame):
    def __init__(self,parent,node_size,board_height,board_width):
        self.node_size = node_size
        self.board_height = board_height
        self.board_width = board_width
        self.root = Tk()
        

    def build_canvas(self,root,board_height,board_width,node_size):
        rows = int(board_height / node_size)
        columns = int(board_width / node_size)
        

        canvas_width = columns * node_size
        canvas_height = rows * node_size

        board_canvas = Canvas(self.root, width =canvas_width, height = canvas_height, bg = "white")
        board_canvas.pack(pady = 20)
        drawn_board_canvas = self.draw_canvas_grid(rows,columns,node_size,board_canvas)

        return drawn_board_canvas

    def draw_canvas_grid(self,rows,columns,node_size,board_canvas):
        for row in range(rows):
            for col in range(columns):
                x1 = (col * node_size)
                y1 = (row * node_size)
                x2 = x1 + node_size
                y2 = y1 + node_size
                
                board_canvas.create_rectangle(x1,y1,x2,y2, outline="black", fill="white")
        return board_canvas
    
    

#if __name__ == "__main__":
#    root = tk.Tk()
#    board = board(root)
#    root.mainloop()