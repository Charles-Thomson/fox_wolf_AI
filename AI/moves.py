def get_moves(fox_x,fox_y):

# All moves for location of foxs  
    moves = {
    # 4 closest nodes 
    "move_L1": (fox_x + 1, fox_y),
    "move_R1": (fox_x - 1 , fox_y),
    "move_U1": (fox_x , fox_y + 1), 
    "move_D1": (fox_x , fox_y - 1),

    # 4 corner nodes inner set
    "move_L2": (fox_x + 1 , fox_y + 1),
    "move_R2": (fox_x - 1 , fox_y - 1),
    "move_D2": (fox_x + 1 , fox_y - 1),
    "move_U2": (fox_x - 1 , fox_y + 1),

    # 4 center of each side outer row 
    "move_B_L2": (fox_x + 2 , fox_y ),
    "move_B_R2": (fox_x - 2 , fox_y ),
    "move_B_U2": ( fox_x , fox_y + 2),
    "move_B_D2": ( fox_x , fox_y - 2 ),  
    
    # Nodes on outer row not inc center of row 
    "move_A_L3": (fox_x + 2 , fox_y + 1 ),
    "move_B_L3": (fox_x + 2 , fox_y - 1 ),
    
    "move_A_R3": (fox_x - 2 , fox_y + 1 ),
    "move_B_R3": (fox_x - 2 , fox_y - 1 ),
   
    "move_A_U3": ( fox_x - 1 , fox_y + 2),
    "move_B_U3": ( fox_x + 1, fox_y + 2),

    "move_A_D3": ( fox_x + 1 , fox_y - 2 ),
    "move_A_D3": ( fox_x - 1, fox_y - 2 ),  

    # 4 moves away - cornor of outer rows 
    "move_R4": (fox_x - 2 , fox_y - 2 ),
    "move_D4": (fox_x - 2 , fox_y + 2 ),
    "move_U4": (fox_x + 2 , fox_y + 2 ),
    "move_D4": (fox_x + 2 , fox_y - 2 )
     }

    return moves