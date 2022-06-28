from tkinter import *
from dataclasses import *

# Currently beng used to test data classes

@dataclass
class animal:
    animal_type: str 
    animal_location: tuple
    animal_sight_range: int 
    animal_next_move: tuple
    animal_alive: bool

def SpawnNewAnimal(animal_type, animal_location, animal_sight_range) -> animal:
    return animal(animal_type = animal_type, animal_location=animal_location, animal_next_move = (), animal_alive = True, animal_sight_range = animal_sight_range)

def main() -> None:
    new_animal = SpawnNewAnimal(animal_type = "Fox",animal_location = (5,5), animal_sight_range = 5)
    print(new_animal)
    
    



if __name__ == "__main__":
    main()
