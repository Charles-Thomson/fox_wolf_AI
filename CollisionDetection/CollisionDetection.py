import collections


class CollisionDetection:
    def __init__(self, canvas_data):
        self.numeber_of_rows = canvas_data.number_of_rows
        self.number_of_columns = canvas_data.number_of_columns
        self.Animals_moving_to = []

    def PossibleNewLocation(
        self, current_animal_location: tuple, potential_move: tuple
    ) -> tuple:
        """Helper to find the new location of a given move"""

        return tuple(sum(x) for x in zip(current_animal_location, potential_move))

    def MoveValidation(
        self, current_animal_location: tuple, potential_moves: list[tuple]
    ) -> tuple:
        """Check each given move for collision"""

        while True:
            if potential_moves is []:
                print("Returning no move")
                return (0, 0)
            potential_move = collections.Counter(potential_moves).most_common()[0][0]
            potential_new_location = self.PossibleNewLocation(
                current_animal_location, potential_move
            )

            if self.CollisionChecking(potential_new_location):
                return potential_move
            else:
                potential_moves = [
                    move for move in potential_moves if move != potential_move
                ]

            return ()

    def AStartCollisionChecking(self, potential_move_to: tuple):
        """Checking for A* alg - Doesn't add to the Animls_moveing_to list"""

        if self.CheckForAnimalCollision(
            potential_move_to
        ) and self.CheckingBoarderCollision(potential_move_to):
            return True
        else:
            return False

    def CollisionChecking(self, potential_move_to: tuple) -> bool:
        """Returning True if the potential move is non-colliding"""

        if self.CheckForAnimalCollision(
            potential_move_to
        ) and self.CheckingBoarderCollision(potential_move_to):
            self.Animals_moving_to.append(potential_move_to)
            return True
        else:
            return False

    def CheckForAnimalCollision(self, potential_move_to) -> bool:
        """Check for collison with another animal of the same type"""

        if potential_move_to in self.Animals_moving_to:

            return False
        else:
            return True

    def CheckingBoarderCollision(self, potential_move_to) -> bool:
        """Check for collision with the boundries of the map"""

        animal_next_move_X, animal_next_move_Y = potential_move_to
        if animal_next_move_X < 0 or animal_next_move_Y < 0:
            return False
        if (
            animal_next_move_X > self.numeber_of_rows - 1
            or animal_next_move_Y > self.number_of_columns - 1
        ):  # -1 due to the canvas starting at 0
            return False
        return True

    def MoveList(self) -> None:
        """Helper fucntion - used as a test point"""
        print(self.Animals_moving_to)
