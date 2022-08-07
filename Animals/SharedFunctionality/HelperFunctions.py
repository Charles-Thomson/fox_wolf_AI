import collections
from Animals.SharedFunctionality.CollisionDetection import CollisionDetection
from Animals.SharedFunctionality.NewAnimalDataClass import Animal
from Board import CanvasData


def DetectAnimalsInRange(
    main_animal: Animal, other_animals: list[Animal]
) -> list[tuple]:
    """Detect animals in range of the animal, returns list of (x,y)"""

    (
        main_animal_coord_X,
        main_animal_coord_Y,
    ) = main_animal.move_data.animal_location
    animals_in_range = []

    for other_animal in other_animals:
        (
            other_animal_coord_X,
            other_animal_coord_Y,
        ) = other_animal.move_data.animal_location

        condition_one = main_animal_coord_X in range(
            int(other_animal_coord_X - main_animal.core_data.animal_sight_range),
            int(other_animal_coord_X + main_animal.core_data.animal_sight_range),
        )

        condition_two = main_animal_coord_Y in range(
            int(other_animal_coord_Y - main_animal.core_data.animal_sight_range),
            int(other_animal_coord_Y + main_animal.core_data.animal_sight_range),
        )
        if condition_one and condition_two:
            animals_in_range.append(other_animal.move_data.animal_location)
    return animals_in_range


def SetAnimalMovingTo(animal: Animal) -> None:
    """Set the animal data for moving to"""

    current_location = animal.move_data.animal_location
    move_by = animal.move_data.animal_next_move

    new_coords = tuple(sum(x) for x in zip(current_location, move_by))
    animal.move_data.animal_moving_to = new_coords


def AnimalWouldMoveTo(
    animal_current_location: tuple, animal_potential_move: tuple
) -> tuple:
    """Helper function used in DeterminBestMove"""

    return tuple(sum(x) for x in zip(animal_current_location, animal_potential_move))


# Need to pass the position the animal will move to in here
def RebuildDetermineBestMove(
    animal_current_location: tuple,
    good_moves: list[tuple],
    collision_detection: CollisionDetection,
) -> tuple:

    """Finding the optimal move that is also allowed"""

    while True:
        if good_moves == []:
            print("Returning no move")
            return (0, 0)
            break
        potential_move = collections.Counter(good_moves).most_common()[0][0]
        potential_new_location = AnimalWouldMoveTo(
            animal_current_location, potential_move
        )

        if collision_detection.CollisionChecking(potential_new_location):
            return potential_move
        else:
            good_moves = [move for move in good_moves if move != potential_move]
            print(good_moves)


def MoveAnimal(animal: Animal, canvas_data: CanvasData) -> None:
    """Move the animal to new postion - move made by an ammount based on current position"""

    animal_moving_to_X, animal_moving_to_Y = animal.move_data.animal_next_move
    move_X_by, move_Y_by, x2, y2 = ConvertToLongCoords(
        animal_moving_to_X, animal_moving_to_Y, canvas_data.node_size
    )
    canvas_data.canvas.move(animal.core_data.animal_ID, move_X_by, move_Y_by)


def UpdateAnimalData(animal: Animal) -> None:
    """Update the animals location, clear other fields"""

    animal.move_data.animal_location = animal.move_data.animal_moving_to
    animal.move_data.animal_moving_to = ()
    animal.move_data.animal_next_move = ()
    animal.move_data.animals_in_range = []


def ConvertToShortCoords(animal, built_canvas, node_size) -> tuple:
    """Convert the long coordinates used by tkinter to x,y"""

    x1, y1, x2, y2 = built_canvas.coords(animal)
    x = x1 / node_size
    y = y1 / node_size

    return (x, y)


def ConvertToLongCoords(animal_x, animal_y, node_size) -> tuple:
    """Convert the short x,y coordinates back to the long coordinates"""

    x1 = animal_x * node_size
    y1 = animal_y * node_size
    x2 = x1 + node_size
    y2 = y1 + node_size

    return x1, y1, x2, y2
