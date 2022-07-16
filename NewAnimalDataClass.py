from dataclasses import dataclass, field 
from enum import Enum, auto 
from typing import Protocol
from dataclasses import dataclass
from AI import FoxMovementAlgorithms
from AI import WolfMovementAlgorithms

class AnimalType(Enum):
    """Enumeration of the animal types"""
    FOX = "Fox"
    WOLF = "Wolf"

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
    animal_location: tuple = field(default_factory = tuple )
    animals_in_range: list[tuple] = field(default_factory = list[tuple])
    animal_next_move: tuple = field(default_factory = tuple)
    animal_moving_to: tuple = field(default_factory = tuple)

@dataclass
class Animal(Protocol):
    """Protocol animal clases must follow"""
    animal_core_data: ...
    animal_move_data: ... 
    animal_movment_algorithm: ...
    
@dataclass
class Wolf:
    """Wolf - Predator """
    animal_core_data: AnimalCoreData
    animal_move_data: AnimalMoveData
    animal_movment_algorithm: FoxMovementAlgorithms.FoxMovementAlgoritm

@dataclass
class Fox:
    """Fox - Prey"""
    animal_core_data: AnimalCoreData 
    animal_move_data: AnimalMoveData 
    animal_movement_algorithm: WolfMovementAlgorithms.WolfMovementAlgorithm
    


def SpawnAnimal(animal_type: AnimalType, animal_location: tuple, animal_sight_range: int, animal_draw_colour: str) -> Fox:
    if animal_type == animal_type.FOX:
        return Fox(animal_core_data= AnimalCoreData(0,animal_type.FOX,animal_sight_range,animal_location,animal_draw_colour), animal_move_data= AnimalMoveData(), animal_movement_algorithm=FoxMovementAlgorithms.FoxMovementAlgoritm.BASIC)

    if animal_type == animal_type.WOLF:
        return Fox(animal_core_data= AnimalCoreData(0,animal_type.WOLF,animal_sight_range,animal_location,animal_draw_colour), animal_move_data= AnimalMoveData(), animal_movement_algorithm=WolfMovementAlgorithms.WolfMovementAlgorithm.BASIC)



def Main() -> None:
    test_animal = SpawnAnimal(AnimalType.FOX,(7,7),4,"blue")
    print(test_animal)

if __name__ == "__main__":
    Main()
        

