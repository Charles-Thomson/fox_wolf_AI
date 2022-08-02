
from dataclasses import dataclass
from Animals.SharedFunctunality import HelperFuntions


def BasicMovementAlgorithm(wolf: object ,collision_detection: object, canvas_data: object) -> None: 
    """Basic process to determin best move for the animal"""

    good_moves = []
    wolf_coord_X, wolf_coord_Y = wolf.animal_move_data.animal_location

    for coord_X, coord_Y in wolf.animal_move_data.animals_in_range:
        # +x +y
        if wolf_coord_X >= coord_X and wolf_coord_Y >= coord_Y:
            good_moves.extend([(-1,-1),(0,-1),(-1,0)])
            
        # -x +y
        if wolf_coord_X <= coord_X and wolf_coord_Y >= coord_Y:
            good_moves.extend([(1,-1),(0,-1),(1,0)])
            
        # +y -x 
        if wolf_coord_X >= coord_X and wolf_coord_Y <= coord_Y:
            good_moves.extend([(-1,1),(0,1),(-1,0)])
            
        # -y -x 
        if wolf_coord_X <= coord_X and wolf_coord_Y <= coord_Y:
            good_moves.extend([(1,1),(0,1),(1,0)])

    
    wolf_current_location = (wolf_coord_X, wolf_coord_Y)
    wolf.animal_move_data.animal_next_move = HelperFuntions.RebuildDetermineBestMove(wolf_current_location,good_moves,collision_detection) # Need to work it into here!!




        
class MyNode(): 
    """Nodes used to in relation to the AStart algrithm """

    def __init__(self, parent = None, location = None):
        self.parent = parent
        self.location = location

        self.g = 0
        self.h = 0
        self.f = 0

    # Not sure on this - EQ compare the data not the object
    def __eq__(self, other):
        return self.location == other.location

def AStarTargetPriority(animal_location: tuple, target_locations: list[tuple]) -> tuple:
    """Find the highest priority target based on the distance from the hunting animal"""

    best_target = None
    target_value = 50  # set to a safe top end value

    for target in target_locations:
        value = abs(animal_location[0] - target[0]) + (animal_location[1] - target[1]) # Not taking diagonal movments into consideration
        if target_value > value:
            best_target = target
            target_value = value 

    return best_target 

def AStarMovementAlgorithm(wolf: object ,collision_detection: object,canvas_data: object) -> None:
    """A* movment algorithm for the wolf"""

    animals_in_range = wolf.animal_move_data.animals_in_range

    if animals_in_range == []:
        wolf.animal_move_data.animal_next_move = (0,0) # No Move if nothing in range
        return
        
    number_of_rows = canvas_data.number_of_rows
    number_of_columns = canvas_data.number_of_columns

    animal_location = wolf.animal_move_data.animal_location
    target = AStarTargetPriority(animal_location, animals_in_range) # <-- target not updating
    
    start_node = MyNode(None,animal_location)
    start_node.g = start_node.h = start_node.f = 0

    end_node = MyNode(None, target)    # <- Only taking the first in range
    end_node.g = end_node.h = end_node.f = 0

    open_list = []
    closed_list = []

    # Add the start to the open list
    open_list.append(start_node)
    
    while len(open_list) > 0:
        # Get the current node
        current_node = open_list[0]
        current_index = 0
    
        # Check to see if the value(f) of the a open_list node < current_node. 
        # Set current_node to be the open_list node
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # pop the current node off open_list
        # Add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Guard for maximum recursion depth 
        # Can only check upto Animal sight range ^ 3 No* nodes
        if len(closed_list) > (wolf.animal_core_data.animal_sight_range ** 3) :
            print("no move found based on recursion depth")
            wolf.animal_move_data.animal_next_move = (0,0)
            break
        
        # Check to see if the end node has been found
        # If so return the path to he end
        # clean this up
        if current_node == end_node:
            print("Found path")
            path = []
            current = current_node
            while current is not None:
                path.append(current.location)
                current = current.parent
            path.reverse()
            
            wolf_current_location = wolf.animal_move_data.animal_location
            good_move = [((path[1][0] - wolf_current_location[0] ), (path[1][1] -  wolf_current_location[1]))]
            
            wolf.animal_move_data.animal_next_move = HelperFuntions.RebuildDetermineBestMove(wolf_current_location,good_move,collision_detection) 
            print(wolf)
            break

        # Generate Children
        children = []

        # Adjacent squares 
        adjacent_squares = [(1,1),(1,0),(1,-1),(0,-1),(-1,0),(-1,-1),(-1,1),(0,1)]
        
        for new_position in adjacent_squares:
            # Location of the new node 
            node_position = (current_node.location[0] + new_position[0], current_node.location[1] + new_position[1])
        
            # Check if new postion in range
            if node_position[0] > number_of_rows - 1 or node_position[0] < 0 or node_position[1] > number_of_columns or node_position[1] < 0:
                continue # break out the loop 

            # Collision detection here <--
            if collision_detection.AStartCollisionChecking(node_position) == False:
                continue

            # Make the new Node 
            new_node = MyNode(parent = current_node, location = node_position)

            # Add new node to children
            children.append(new_node)

        # loop through the childen
        for child in children:
            
            # check if child in closed_list
            for closed_child in closed_list:
                if child.location == closed_child.location:
                    continue # break the loop

            # Set the node values
            # G = Distance from current node to star node
            # H = Estimated distance from current node to the end node
            # F = total cost of the node (G + H)
            child.g = current_node.g + 1
            child.h = (( child.location[0] - end_node.location[0]) ** 2) + ((child.location[1] - end_node.location[1]) ** 2)
            child.f = child.g + child.h

            # Check for child in the open list
            for open_child in open_list:
                if child == open_child and child.g > open_child.g:
                    continue # Break the loop

            # Add the child to the open list
            open_list.append(child)
