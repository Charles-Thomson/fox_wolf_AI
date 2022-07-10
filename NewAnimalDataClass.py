from dataclasses import dataclass, field 
from enum import Enum, auto 
from typing import Protocol
from dataclasses import dataclass


class AnimalType(Enum):
    """Enumeration of the animal types"""
    FOX = auto()
    WOLF= auto()

@dataclass
class AnimalCoreData:
    """Core Data for each animal"""
    animal_ID: int
    animal_type: AnimalType
    animal_sigth_range: int
    animal_draw_colour: str
    
@dataclass
class AnimalMoveData:
    """Movment Data for each animal"""
    animal_location: tuple = field(default_factory = tuple )
    animals_in_range: list[tuple] = field(default_factory = list[tuple])
    animal_next_move: tuple = field(default_factory = tuple)
    animal_moving_to: tuple = field(default_factory = tuple)


# Amimal Classes

@dataclass
class Animal(Protocol):
    """Protocol animal clases must follow"""
    animal_alive: ...
    animal_core_data: ...
    animal_move_data: ... 
    
@dataclass
class Wolf:
    """Wolf - Predator """
    animal_alive: bool
    animal_core_data: AnimalCoreData
    animal_move_data: AnimalMoveData

@dataclass
class Fox:
    """Fox - Prey"""
    animal_alive: bool
    animal_core_data: AnimalCoreData 
    animal_move_data: AnimalMoveData 

    




# Test for the creation of an animal 
def SpawnNewTestAnimal() -> object:
    """Wolf Test Instance"""
    return Wolf(animal_alive = True,animal_core_data= AnimalCoreData(1, AnimalType.WOLF, 4, "red"), animal_move_data = AnimalMoveData())

def Main() -> None:
    test_animal = SpawnNewTestAnimal()
    print(test_animal)

if __name__ == "__main__":
    Main()
        

