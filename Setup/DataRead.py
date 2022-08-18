"""
MAY CONVERT TO A CLASS 
Formatting the txt file data into Animal Spawn Data objects

Returns a list of Spawn Data objects

"""
from dataclasses import dataclass
from ast import literal_eval
from typing import Union

from Animals.SharedFunctionality.NewAnimalDataClass import (
    FoxMovementAlgorithm,
    WolfMovementAlgorithm,
)


@dataclass
class AnimalSpawnData:
    """Spawn Data of each Animal"""

    animal_type: str
    spawn_location: tuple
    sight_range: int
    movement_algorithm: Union[WolfMovementAlgorithm, FoxMovementAlgorithm, None]

    def __getitem__(self, item):
        return getattr(self, item)


def ReadInData() -> tuple[list, list]:
    """Read in the animal data from txt file"""

    data_buffer = []

    with open("Setup/AnimalData.txt", "r") as animal_file:
        for i in range(25):
            next(animal_file)  # Data starts past line 25 of file

        for line in animal_file:
            if "**ANIMAL**" not in line:
                continue

            for val in range(4):
                data_element = FormatData(animal_file.readline())
                data_buffer.append(data_element)

        spawn_data = GenerateSpawnDataObjects(data_buffer)
        foxs_spawn_data, wolfs_spawn_data = SpawnDataAnimalSeperation(spawn_data)

    # Testing point
    for data in foxs_spawn_data:
        print(data)
    for data in wolfs_spawn_data:
        print(data)

    return foxs_spawn_data, wolfs_spawn_data


def FormatData(data_element: str) -> Union[str, tuple, int]:
    """Format each data element to relervent data & type"""

    data_element = data_element.strip()
    data_element = data_element.split("=")[1]
    formatted_data_element = literal_eval(data_element)

    return formatted_data_element


def GenerateSpawnDataObjects(data_holder: list[str]) -> list[AnimalSpawnData]:
    """Generate the AnimalSpawnData Objetcs"""

    data_range = int(len(data_holder) / 4)
    spawn_data = []
    for val in range(data_range):
        new_animal = AnimalSpawnData(
            animal_type=data_holder.pop(0),
            spawn_location=data_holder.pop(0),  # type: ignore - correct after eval
            sight_range=data_holder.pop(0),  # type: ignore - correct after eval
            movement_algorithm=SetMovementAlgorithm(data_holder.pop(0)),
        )
        spawn_data.append(new_animal)

    return spawn_data


def SetMovementAlgorithm(
    movement_algorithm: str,
) -> Union[WolfMovementAlgorithm, FoxMovementAlgorithm, None]:
    """Convert the move alg string to type movement algorithm"""

    match movement_algorithm:
        case "FOX.BASIC":
            return FoxMovementAlgorithm.BASIC
        case "FOX.ASTAR":
            return FoxMovementAlgorithm.ASTAR
        case "FOX.ASTARR":
            return FoxMovementAlgorithm.ASTARR
        case "WOLF.BASIC":
            return WolfMovementAlgorithm.BASIC
        case "WOLF.ASTAR":
            return WolfMovementAlgorithm.ASTAR
        case _:
            print(f"Match error - {movement_algorithm} not valid movement algorihtm")
            return None


def SpawnDataAnimalSeperation(spawn_data: list[AnimalSpawnData]) -> tuple[list, list]:
    """Seperation of animal spwan data objects based on animal type"""

    foxs = []
    wolfs = []

    for element in spawn_data:
        animal_type = element.animal_type
        match animal_type:
            case "FOX":
                foxs.append(element)
            case "WOLF":
                wolfs.append(element)
            case _:
                print("Match error - animal type invalid")

    return foxs, wolfs


if __name__ == "__main__":
    ReadInData()
