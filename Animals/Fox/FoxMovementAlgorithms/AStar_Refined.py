"""
    AStar movement algorithm refined for the use case
    ***
    1. Only find the first step in the path - Find the lowest value closest node
    2. Map all nodes to include multiple paths(Wolfs)
    3. The algorithm will be reversed so we want the highest value


    To do:
        1. Create the basic alg 
        2. Set the values for each node around the fox 
        3. Add in the additional values for multiple paths(wolfs)

"""

from Animals.SharedFunctunality import HelperFunctions

class ChildNode:
    """Custom node class - used for the children of the Fox location node """

    def __init__(self,location: tuple, adjacent_location: tuple ):
        self.location = location 
        self.adjacent_location = adjacent_location

        self.value = 0


def Algorithm(fox: object, collision_detection: object, canvas_data: object) -> None:
    """Find the value of each node around the Fox based on each nodes distance from a wolf"""

    preditor_locations = fox.animal_move_data.animals_in_range
    fox_location = fox.animal_move_data.animal_location
    
    adjacent_nodes = []
    adjacent_locations = [(1,1),(1,0),(1,-1),(0,-1),(-1,0),(-1,-1),(-1,1),(0,1)]

    # Create the nodes
    for adjacent_location in adjacent_locations:
        node_location = tuple(sum(x) for x in zip(fox_location, adjacent_location))
        new_node = ChildNode(node_location, adjacent_location)
        adjacent_nodes.append(new_node)

    # Set the nodes value based on location of preditors
    for node in adjacent_nodes:
        value = 0
        for preditor_location in preditor_locations:

            distance_from_node_x = abs(node.location[0] - preditor_location[0])
            distance_from_node_y = abs(node.location[1] - preditor_location[1])

            distance_value = max(distance_from_node_x,distance_from_node_y)

            value += distance_value
        
        node.value = value

    # No move in nothing in range
    if preditor_locations == []:
        fox.animal_move_data.animal_next_move = (0,0) 
        return


    adjacent_nodes.sort(key= lambda x: x.value, reverse=True )

    good_node_moves = adjacent_nodes # Taking the 3 'best' moves <- testing passing all 

    good_moves = [node.adjacent_location for node in good_node_moves]
    
    fox.animal_move_data.animal_next_move = HelperFunctions.RebuildDetermineBestMove(fox_location,good_moves, collision_detection)








