import Setup.SetUp as setup
from Animals.Fox import FoxMain
from Animals.Wolf import WolfMain

import tkinter as tk


class MainProcess:
    def __init__(self, parent, node_size, board_height, board_width):
        self.node_size = node_size
        self.board_height = board_height
        self.board_width = board_width
        self.canvas_data, self.foxs, self.wolfs = setup.main(
            self.node_size, self.board_height, self.board_width
        )
        self.run()

    def run(self) -> None:
        FoxMain.MainFoxAI(self.foxs, self.wolfs, self.canvas_data)
        WolfMain.MainWolfAI(self.wolfs, self.foxs, self.canvas_data)

        if not self.foxs:
            print("All Prey Dead")

        self.canvas_data.canvas.after(1000, self.run)

        #  Do next:
        # Clean up th movement process
        # -> Go through all the movement algs and make them follow a Abstract with set return type

        # Odd Union in the newanialDataclass file due to typeing/unions
        # Not a good long term plan ?
        # Addres line length issue


if __name__ == "__main__":
    root = tk.Tk()
    main = MainProcess(root, 20, 500, 500)
    root.mainloop()
