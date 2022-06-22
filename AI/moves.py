def get_bad_moves(fox_x,fox_y):
    print("coords in move:", fox_x, fox_y)
# All moves for location of foxs  
    bad_moves = {

    # Layout of moves around fox(F)
    #  1  2  3
    #  4  F  5
    #  6  7  8

    # format " not possible moves" - wolf location 
    # 4 closest nodes 
    " 3 5 8": (fox_x + 1, fox_y),
    " 1 4 6": (fox_x - 1 , fox_y),
    " 6 7 8 ": (fox_x , fox_y + 1), 
    " 1 2 3 ": (fox_x , fox_y - 1),

    # 4 corner nodes inner set
    " 5 7 8": (fox_x + 1 , fox_y + 1),
    " 4 2 1": (fox_x - 1 , fox_y - 1),
    " 2 5 3": (fox_x + 1 , fox_y - 1),
    " 4 7 6": (fox_x - 1 , fox_y + 1),

    # 4 center of each side outer row 
    " 3 5 8 ": (fox_x + 2 , fox_y ),
    " 1 4 6 ": (fox_x - 2 , fox_y ),
    " 6 7 8 ": ( fox_x , fox_y + 2),
    " 1 2 3 ": ( fox_x , fox_y - 2 ),  
    
    # Nodes on outer row not inc center of row 
    " 5 8 ": (fox_x + 2 , fox_y + 1 ),
    " 3 5 ": (fox_x + 2 , fox_y - 1 ),
    
    " 6 4 ": (fox_x - 2 , fox_y + 1 ),
    " 1 4 ": (fox_x - 2 , fox_y - 1 ),
   
    " 6 7 ": ( fox_x - 1 , fox_y + 2),
    " 8 7 ": ( fox_x + 1, fox_y + 2),

    " 2 3 ": ( fox_x + 1 , fox_y - 2 ),
    " 1 2 ": ( fox_x - 1, fox_y - 2 ),  

    # 4 moves away - cornor of outer rows 
    " 1 ": (fox_x - 2 , fox_y - 2 ),
    " 6 ": (fox_x - 2 , fox_y + 2 ),
    " 8 ": (fox_x + 2 , fox_y + 2 ),
    " 3 ": (fox_x + 2 , fox_y - 2 )
     }

    return bad_moves