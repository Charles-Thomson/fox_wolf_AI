from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Animals.SharedFunctionality.CollisionDetection import CollisionDetection
    from Animals.SharedFunctionality.NewAnimalDataClass import Animal
    from Board import CanvasData


def BasicMovmentAlgorithm(
    self: Animal, collision_detection: CollisionDetection, canvas_data: CanvasData
) -> None:
    """Basic approach to finding the next 'best' move for the fox"""

    good_moves = []
    bad_moves = []
    fox_coord_X, fox_coord_Y = self.move_data.animal_location

    for coord_X, coord_Y in self.move_data.animals_in_range:
        # +x
        if coord_X > fox_coord_X and coord_Y == fox_coord_Y:
            bad_moves.extend([(1, 0)])
            good_moves.extend([(-1, 0), (-1, -1), (-1, 1)])

        # -x
        if coord_X < fox_coord_X and coord_Y == fox_coord_Y:
            bad_moves.extend([(-1, 0)])
            good_moves.extend([(1, 0)])

        # +y
        if coord_X == fox_coord_X and coord_Y > fox_coord_Y:
            bad_moves.extend([(0, 1)])
            good_moves.extend([(0, -1)])

        # -y
        if coord_X == fox_coord_X and coord_Y < fox_coord_Y:
            bad_moves.extend([(0, -1)])
            good_moves.extend([(0, 1)])

        # +x +y
        if coord_X > fox_coord_X and coord_Y > fox_coord_Y:
            bad_moves.extend([(1, 1)])
            good_moves.extend([(-1, -1), (-1, 0), (0, -1)])

        # -x -y
        if coord_X < fox_coord_X and coord_Y < fox_coord_Y:
            bad_moves.extend([(-1, -1)])

            good_moves.extend([(1, 1), (1, 0), (0, 1)])

        # +x -y
        if coord_X > fox_coord_X and coord_Y < fox_coord_Y:
            bad_moves.extend([(1, -1)])
            good_moves.extend([(-1, 1), (-1, 0), (0, 1)])

        # -x +y
        if coord_X < fox_coord_X and coord_Y > fox_coord_Y:
            bad_moves.extend([(-1, 1)])
            good_moves.extend([(1, -1), (1, 0), (0, -1)])

    good_moves = [move for move in good_moves if move not in bad_moves]
    fox_current_location = (fox_coord_X, fox_coord_Y)
    self.move_data.animal_next_move = collision_detection.MoveValidation(
        fox_current_location, good_moves
    )
