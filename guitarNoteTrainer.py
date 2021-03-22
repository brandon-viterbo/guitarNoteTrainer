#!/usr/bin/env python

import guitarTuner
import random
import json

GUITAR_FILE = "guitar.json"
NOTE_FILE = "equalTempermentNotes.json"
TUNE_INPUT = "T"
ID_INPUT = "I"
EXIT_INPUT = "E"

"""
TODO:
1)    Make input loops for start menu
        -Tune Guitar?
        -Note identity test?
        -Exit
"""

with open(NOTE_FILE, "r") as readFile:
    notes = json.load(readFile)["notes"]

def menuLoop(notes):
    with open(GUITAR_FILE, "r") as readFile:
        guitar = json.load(readFile)
        guitarStrings = guitar["strings"]
        guitarTuning = guitar["tuningText"]

    print("Welcome to guitar note trainer! Your guitar is tuned to {}.".format(
        guitarTuning)
    )
    userInput = input(("Press '{}' to test note identification, '{}' to " +  
        "change your guitar's tuning, or '{}' to exit: ").format(
            ID_INPUT, TUNE_INPUT, EXIT_INPUT)
        )

    userInput = userInput.upper()
    if userInput == ID_INPUT:
        return identifyNotesLoop(notes)
    elif userInput == TUNE_INPUT:
        print("\nNow tuning guitar.")
        guitarTuner.tuneGuitar(notes)
        print("\n")
        return menuLoop(notes)
    elif userInput == EXIT_INPUT:
        print("Thank you for using Guitar Note Trainer!")
        print("See you later!")
    else:
        print("Invalid input. Please try again.\n")
        return menuLoop(notes)
    return


def identifyNotesLoop(notes):
    print("TODO: Test Note Identification.")
    return

menuLoop(notes)

exit()