from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Animals.SharedFunctionality.CollisionDetection import CollisionDetection
    from Animals.SharedFunctionality.NewAnimalDataClass import Animal
    from Board import CanvasData

"""
    AStar algorithm with the first move of the path inverted to move away from
    a target.

    Basic implementation of the Algorithm

"""


class MyNode:
    """Custome node used in the Astar Algorithm"""

    def __init__(self, parent=None, location=None):
        self.parent = parent
        self.location = location

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.location == other.location


def ReversedAStartTargetPriority(
    animal_location: tuple, target_locations: list[tuple]
) -> None:
    pass


# This can be improved
def ReversedAStarMoveInverter(move: tuple) -> tuple:
    """Invert move - give the best move away from the best path"""

    inverted_move = [0, 0]

    if move[0] == 1:
        inverted_move[0] = -1

    if move[0] == -1:
        inverted_move[0] = 1

    if move[1] == 1:
        inverted_move[1] = -1

    if move[1] == -1:
        inverted_move[1] = 1

    return tuple(inverted_move)


def ReversedAStartMovmentAlgorithm(
    fox: Animal, collision_detection: CollisionDetection, canvas_data: CanvasData
) -> None:
    """Reversed version of the AStar path finding algorithm"""

    animals_in_range = fox.move_data.animals_in_range

    if animals_in_range == []:
        fox.move_data.animal_next_move = (0, 0)  # No move
        return

    number_of_rows = canvas_data.number_of_rows
    number_of_columns = canvas_data.number_of_columns

    animal_location = fox.move_data.animal_location
    escaping_from_target = animals_in_range[0]  # Change when implemting priority

    start_node = MyNode(None, animal_location)
    start_node.g = start_node.h = start_node.f = 0

    end_node = MyNode(None, escaping_from_target)
    end_node.g = end_node.h = end_node.f = 0

    open_list = []
    closed_list = []

    # Add the start to the open list
    open_list.append(start_node)

    while len(open_list) > 0:
        # Get the current node
        current_node = open_list[0]
        current_index = 0

        lst = [loc.location for loc in open_list]
        print(lst)

        # Check if the value(f) of the open list node > current_node

        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop and append to closed_list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # <- No current guard for reccursion depth

        # Taking the path, reverse the fist step , -1 = 1 , 1 = -1
        if current_node == end_node:
            print("Escape move found")
            path = []
            current = current_node
            while current is not None:
                path.append(current.location)
                current = current.parent

            fox_current_location = fox.move_data.animal_location
            move = (
                (path[1][0] - fox_current_location[0]),
                (path[1][1] - fox_current_location[1]),
            )

            best_move = []
            best_move.append(ReversedAStarMoveInverter(move))

            fox.move_data.animal_next_move = collision_detection.MoveValidation(
                fox_current_location, best_move
            )

            break

        # Children of the current node
        children = []

        adjacent_squares = [
            (1, 1),
            (1, 0),
            (1, -1),
            (0, -1),
            (-1, 0),
            (-1, -1),
            (-1, 1),
            (0, 1),
        ]

        for new_position in adjacent_squares:

            # Location of the new node
            node_position = (
                current_node.location[0] + new_position[0],
                current_node.location[1] + new_position[1],
            )

            # Guard for in range of the cavnas

            if node_position[0] > number_of_rows - 1 or node_position[0] < 0:
                continue

            if node_position[0] > number_of_columns - 1 or node_position[1] < 0:
                continue

            # <- can add in the AStar collision detection here

            # Make the new node
            new_node = MyNode(parent=current_node, location=node_position)

            children.append(new_node)

        for current_child in children:

            # If the child alread visited break
            for child in closed_list:
                if current_child.location == child.location:
                    continue

                # Set the node values
                # G = Distance from current node to start node
                # H = Estimated distance from current node to the end node
                # F = total cost of the node (G + H)
                # This may need on less indentation
                current_child.g = current_node.g + 1
                x_distance = (child.location[0] - end_node.location[0]) ** 2
                y_distance = (child.location[1] - end_node.location[1]) ** 2
                current_child.h = x_distance + y_distance
                current_child.f = current_child.g + current_child.h

            # Check what this i for ...
            for child in open_list:
                if current_child == child and current_child.g > child.g:
                    continue

            open_list.append(current_child)
