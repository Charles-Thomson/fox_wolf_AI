from dataclasses import dataclass, field
from enum import Enum
from typing import Protocol, Union

from Animals.Wolf.WolfMovementAlgorithms import Basic as WolfBasic
from Animals.Wolf.WolfMovementAlgorithms import AStar_Full

from Animals.Fox.FoxMovementAlgorithms import Basic as FoxBasic
from Animals.Fox.FoxMovementAlgorithms import AStar_MoveReversed
from Animals.Fox.FoxMovementAlgorithms import AStar_Refined


class AnimalType(Enum):
    """Enumeration of the animal types"""

    FOX = "Fox"
    WOLF = "Wolf"


class WolfMovementAlgorithm(Enum):
    BASIC = WolfBasic.BasicMovementAlgorithm
    ASTAR = AStar_Full.AStarMovementAlgorithm


class FoxMovementAlgorithm(Enum):
    BASIC = FoxBasic.BasicMovmentAlgorithm
    ASTAR = AStar_MoveReversed.ReversedAStartMovmentAlgorithm
    ASTARR = AStar_Refined.Algorithm


@dataclass
class AnimalCoreData:
    """Core Data for each animal"""

    animal_ID: int
    animal_type: AnimalType
    animal_sight_range: int
    animal_spawn_location: tuple
    animal_draw_colour: str
    animal_alive: bool = True


@dataclass
class AnimalMoveData:
    """Movment Data for each animal"""

    animal_location: tuple = field(default_factory=tuple)
    animals_in_range: list[tuple] = field(default_factory=list[tuple])
    animal_next_move: tuple = field(default_factory=tuple)
    animal_moving_to: tuple = field(default_factory=tuple)


@dataclass
class Animal(Protocol):
    """Protocol animal clases must follow"""

    core_data: ...
    move_data: ...
    animal_movement_algorithm: ...


@dataclass
class Wolf:
    """Wolf - Predator"""

    core_data: AnimalCoreData
    move_data: AnimalMoveData
    animal_movement_algorithm: Union[FoxMovementAlgorithm, WolfMovementAlgorithm]


@dataclass
class Fox:
    """Fox - Prey"""

    core_data: AnimalCoreData
    move_data: AnimalMoveData
    animal_movement_algorithm: Union[FoxMovementAlgorithm, WolfMovementAlgorithm]


def SpawnAnimal(
    animal_type: AnimalType,
    animal_location: tuple,
    animal_sight_range: int,
    animal_draw_colour: str,
    animal_movement_algorithm: Union[FoxMovementAlgorithm, WolfMovementAlgorithm],
) -> Animal:
    if animal_type == animal_type.FOX:
        return Fox(
            core_data=AnimalCoreData(
                0,
                animal_type.FOX,
                animal_sight_range,
                animal_location,
                animal_draw_colour,
            ),
            move_data=AnimalMoveData(),
            animal_movement_algorithm=animal_movement_algorithm,
        )

    if animal_type == animal_type.WOLF:
        return Wolf(
            core_data=AnimalCoreData(
                0,
                animal_type.WOLF,
                animal_sight_range,
                animal_location,
                animal_draw_colour,
            ),
            move_data=AnimalMoveData(),
            animal_movement_algorithm=animal_movement_algorithm,
        )
