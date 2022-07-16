import NewSetUp as setup
from AI import NewFoxAI
from AI import NewWolfAI
import tkinter as tk


class main():
    def __init__(self,parent,node_size, board_height, board_width):
        self.node_size = node_size
        self.board_height = board_height
        self.board_width = board_width
        self.canvas_data, self.foxs, self.wolfs = setup.main(self.node_size,self.board_height,self.board_width)
        self.testNewFoxAI()
        self.testNewWolfAI()

    def testNewFoxAI(self):
        NewFoxAI.MainFoxAI(self.foxs, self.wolfs,self.canvas_data)

    def testNewWolfAI(self):
        NewWolfAI.MainWolfAI(self.wolfs,self.foxs,self.canvas_data)
    


        #  Do next:  
        #   Refactoring
        # - Moving Algoritms into own class and giving enumeration <- done 
        # - Each aniaml gets algorithm assigned <- done
        # - Loop each animal and call the algorithm <- done for foxs
        # 
        # - refactor move calls for animals
        # - need new detectionn of collision and death 
        
        
        #
        #  Fox movment needs to be improved
        #  - Move over to a better way to detect and move 
        #  - issue with finding the best move and carrying in out <- possibalycollision checking issue
        #  
        #  Issues: 
        #  Collision is currently quite clunky - find a better way 
        #  Fox move has bug -> more moves can be made but freezes in place
        # 
        # 
        #look at logging instead of print /?

        # start looking at reverse A* 


if __name__ == "__main__":
    root = tk.Tk()
    main = main(root, 20,500,500)
    root.mainloop()

 