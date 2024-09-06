Start: 2020

Python Project

Application to visualize pathfinding algorithms in a 2D environment.

The environment is defined as a 2D space. Predator and prey animals are generated and placed within the environment. The goal of the prey is to evade the predator.

SetUp:
- Defines animal data, start location, color, type, etc.
- Reader for animal data.
- Setup for movement algorithms and object spawning in the environment (draw functions)

GUI:
- Handled by the Tkinter package.
- Draws the environment as a 2D grid.

Collision Detection:
- Handles detection of object collisions within the environment.
- Handles move validation.

Movement  Algorithms:
- A* based pathfinding algorithms with alterations for use case optimization and optimal move calculations.
- "Basic" movement algorithm that follows the path of a target object.

Helper Functions:

- Functions to detect the range of one object from another.
- Updates object data after movement.
- Conversions for coordinate data.

DataBase(DB):
- Rudimental implimentation , not yet fuully used

