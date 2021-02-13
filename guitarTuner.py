#!/usr/bin/env python

"""
TODO:
    -Condense the prompt loop functions into one function.
    -Change tune guitar string function so that it saves the other names of
    the notes.
"""

import json

GUITAR_FILE = "guitar.json"
NOTE_FILE = "equal_temperment_notes.json"

with open(NOTE_FILE, "r") as read_file:
    """
    The variable "notes" is a list of lists, where each sublist represents a note
    and each element in that sublist is a valid string name for that note. 
    For example, the note A is represented with the sublist ["A"], and the note 
    "C" is represented with the sublist ["C", "B#"].
    All function definitions that have "notes" will call this variable.  
    """
    notes = json.load(read_file)["notes"]


def tuneGuitar(notes):
    """
    Main function of this document. Writes whatever tuning the user inputs when 
    tuneGuitarPrompt() is called into the file defined as GUITAR_FILE. 
    """
    tuning = tuneGuitarPrompt(notes)

    with open(GUITAR_FILE, "w") as write_file:
        count = 0
        guitarStrings = [None]*len(tuning)
        for newTuning in tuning[::-1]:
            guitarStrings[count] = {"stringNo": count+1, "openNote": newTuning}
            count += 1
        data = {"strings": guitarStrings}
        json.dump(data, write_file, indent=4)


def tuneGuitarPrompt(notes):
    """
    Prompts user to input the number of strings their guitar has, and
    the tuning of each string.
    """
    stringNumber = getGuitarStringInput()
    print("Your guitar has {} strings.".format(stringNumber))

    tuning=[None]*stringNumber
    for guitarString in range(stringNumber):
        inputNote = tuneGuitarStringInput(guitarString, notes)
        tuning[stringNumber-guitarString-1] = inputNote

    tuningStr = "".join(tuning)
    print("From strings {} to 1, your guitar is tuned as {}.".format(
        stringNumber, tuningStr)
    )
    return tuning


"""
Following two functions are input prompts that loop until the user inputs a
valid response.
"""
def tuneGuitarStringInput(guitarString, notes):
    inputNote = input("What is string {} tuned to? ".format(guitarString+1))
    if validNote(inputNote, notes):
        return inputNote
    else:
        print("Please enter a note as the capitalized note letter on its own ",
            "or followed by '#' or lowercase 'b'.")
        return tuneGuitarString(guitarString, notes)


def getGuitarStringInput():
    res = input("How many strings does your guitar have? ")
    try:
        res = int(res)
        if res < 1:
            print("Please enter a number greater than 0.")
            return(getGuitarStringInput())
    except:
        print("Please enter a number.")
        return getGuitarStringInput()
    return res


def validNote(inputNote, notes):
    """
    Checks if string "inputNote" is a note in the note system (i.e. twelve-tone equal
    temperment) specified in the list of lists "notes". 
    """
    for note in notes:
        if inputNote in note:
            return True
    return False


tuneGuitar(notes)