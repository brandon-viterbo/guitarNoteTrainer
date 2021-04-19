#!/usr/bin/env python

# Python 3.7.4

import guitarTuner
import guitarNoteIdentification
import json

GUITAR_FILE = "guitar.json"
NOTE_FILE = "notes.json"
TUNE_INPUT = "T"
ID_INPUT = "I"
EXIT_INPUT = "E"


with open(NOTE_FILE, "r") as readFile:
    NOTES = json.load(readFile)["notes"]

def main():
    try:
        with open(GUITAR_FILE, "r") as readFile:
            guitar = json.load(readFile)
            guitarStrings = guitar["strings"]
            guitarTuning = guitar["tuningText"]
            frets = guitar["frets"]
    except:
        print("\nBefore anything else, please tune your virtual guitar.")
        guitarTuner.tuneGuitar(NOTES, GUITAR_FILE)
        return main()

    print("\nWelcome to guitar note trainer! Your guitar is tuned to {}.".format(
        guitarTuning)
    )
    userInput = input(("Press '{}' to test note identification, '{}' to " +  
        "change your guitar's tuning, or '{}' to exit: ").format(
            ID_INPUT, TUNE_INPUT, EXIT_INPUT)
        )

    userInput = userInput.upper()
    if userInput == ID_INPUT:
        guitarNoteIdentification.test(NOTES, guitarStrings, frets)
    elif userInput == TUNE_INPUT:
        guitarTuner.tuneGuitar(NOTES, GUITAR_FILE)
    elif userInput == EXIT_INPUT:
        print("\nThank you for using Guitar Note Trainer!")
        print("See you later!")
        exit()
    else:
        print("Invalid input. Please try again.\n")
    return main()


main()
