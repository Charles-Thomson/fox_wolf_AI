def get_bad_moves(fox_short_coords):
    fox_x = fox_short_coords[0]
    fox_y = fox_short_coords[1]
# All moves for location of foxs  
    bad_moves = {

    # Layout of moves around fox(F)
    #  1  2  3
    #  4  F  5
    #  6  7  8

    # format: best resulting move - ruled out moves 
    # 4 closest nodes 
    "4-358 ": (fox_x + 1, fox_y),
    "5-146 ": (fox_x - 1 , fox_y),
    "2-678  ": (fox_x , fox_y + 1), 
    "7-123  ": (fox_x , fox_y - 1),

    # 4 corner nodes inner set
    "1-578": (fox_x + 1 , fox_y + 1),
    "8-421": (fox_x - 1 , fox_y - 1),
    "6-253": (fox_x + 1 , fox_y - 1),
    "3-476": (fox_x - 1 , fox_y + 1),

    # 4 center of each side outer row 
    "4-358": (fox_x + 2 , fox_y ),
    "5-146": (fox_x - 2 , fox_y ),
    "2-678": ( fox_x , fox_y + 2),
    "7-123": ( fox_x , fox_y - 2 ),  
    
    # Nodes on outer row not inc center of row 
    "1-58": (fox_x + 2 , fox_y + 1 ),
    "6-35": (fox_x + 2 , fox_y - 1 ),
    
    "3-64": (fox_x - 2 , fox_y + 1 ),
    "8-14": (fox_x - 2 , fox_y - 1 ),
   
    "3-67": ( fox_x - 1 , fox_y + 2),
    "1-87 ": ( fox_x + 1, fox_y + 2),

    "6-23": ( fox_x + 1 , fox_y - 2 ),
    "8-12": ( fox_x - 1, fox_y - 2 ),  

    # 4 moves away - cornor of outer rows 
    "8-1": (fox_x - 2 , fox_y - 2 ),
    "3-6": (fox_x - 2 , fox_y + 2 ),
    "1-8": (fox_x + 2 , fox_y + 2 ),
    "6-3 ": (fox_x + 2 , fox_y - 2 )
     }

    return bad_moves