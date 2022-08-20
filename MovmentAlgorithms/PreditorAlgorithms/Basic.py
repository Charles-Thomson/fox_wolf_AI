from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from CollisionDetection.CollisionDetection import CollisionDetection
    from Animals.NewAnimalDataClass import Animal
    from GUI.Board import CanvasData


def BasicMovementAlgorithm(
    wolf: Animal, collision_detection: CollisionDetection, canvas_data: CanvasData
) -> None:
    """Basic process to determin best move for the animal"""

    good_moves = []
    wolf_coord_X, wolf_coord_Y = wolf.move_data.animal_location

    for coord_X, coord_Y in wolf.move_data.animals_in_range:
        # +x +y
        if wolf_coord_X >= coord_X and wolf_coord_Y >= coord_Y:
            good_moves.extend([(-1, -1), (0, -1), (-1, 0)])

        # -x +y
        if wolf_coord_X <= coord_X and wolf_coord_Y >= coord_Y:
            good_moves.extend([(1, -1), (0, -1), (1, 0)])

        # +y -x
        if wolf_coord_X >= coord_X and wolf_coord_Y <= coord_Y:
            good_moves.extend([(-1, 1), (0, 1), (-1, 0)])

        # -y -x
        if wolf_coord_X <= coord_X and wolf_coord_Y <= coord_Y:
            good_moves.extend([(1, 1), (0, 1), (1, 0)])

    wolf_current_location = (wolf_coord_X, wolf_coord_Y)
    wolf.move_data.animal_next_move = collision_detection.MoveValidation(
        wolf_current_location, good_moves
    )
