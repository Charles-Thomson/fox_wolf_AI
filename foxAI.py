from tkinter import *
import tkinter as tk
from AI import AISupportingMethods
from AI import moves
import collections 


def DetectWolfsInRange(foxs,wolfs) -> None:
    for fox in foxs:
        fox.animals_in_range = AISupportingMethods.DetectAnimalsInRange(fox,wolfs)
        print("animals in range", fox.animals_in_range)