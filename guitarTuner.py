#!/usr/bin/env python

"""
Coded with Python 3.7.4
"""

import json
import itertools

GUITAR_FILE = "guitar.json"
NOTE_FILE = "equalTempermentNotes.json"

with open(NOTE_FILE, "r") as readFile:
    """
    The variable "notes" is a list of lists, where each sublist represents a note
    and each element in that sublist is a valid string name for that note. 
    For example, the note A is represented with the sublist ["A"], and the note 
    "C" is represented with the sublist ["C", "B#"].
    All function definitions that have "notes" will call this variable.  
    """
    notes = json.load(readFile)["notes"]


def tuneGuitar(notes):
    """
    Main function of this document. Writes whatever tuning the user inputs when 
    tuneGuitarPrompt() is called into the file defined as GUITAR_FILE. 
    """
    tuningIndexes, tuningText, frets = tuneGuitarPrompt(notes)

    with open(GUITAR_FILE, "w") as writeFile:
        count = 0
        guitarStrings = [None]*len(tuningIndexes)
        for openNoteIndex in tuningIndexes[::-1]:
            notesOnString = determineNotesOnString(openNoteIndex, frets)
            guitarStrings[count] = {"stringNo": count+1, 
                "notesOnString": notesOnString
            }
            count += 1
        data = {"strings": guitarStrings}
        data["tuningText"] = tuningText
        data["frets"] = frets
        json.dump(data, writeFile, indent=4)

    return data


def determineNotesOnString(openNoteIndex, frets):
    notesOnString = [openNoteIndex]*(frets+1) # +1 accounts for the open note
    notesCycle = itertools.cycle(notes)

    currentCycle = openNoteIndex
    for i in range(openNoteIndex+1):
        currentCycle = next(notesCycle)
    
    for i in range(0, frets+1):
        notesOnString[i] = currentCycle
        currentCycle = next(notesCycle)
    return notesOnString


def tuneGuitarPrompt(notes):
    """
    Prompts user to input the number of strings their guitar has, and
    the tuning of each string.
    """
    stringNumber = getGuitarStringInput()
    print("Your guitar has {} strings.".format(stringNumber))

    tuningIndexes=[None]*stringNumber
    tuningText=[None]*stringNumber
    for guitarString in range(stringNumber):
        inputNote, noteNumber = tuneGuitarStringInput(guitarString, notes)
        tuningIndexes[stringNumber-guitarString-1] = noteNumber
        tuningText[stringNumber-guitarString-1] = inputNote

    tuningText = "".join(tuningText)
    print("From strings {} to 1, your guitar is tuned as {}.".format(
        stringNumber, tuningText)
    )

    frets = fretboardPrompt()
    return tuningIndexes, tuningText, frets


"""
Following two functions are input prompts that loop until the user inputs a
valid response.
"""
def fretboardPrompt():
    frets = input("Finally, how many frets does your guitar have? ")
    try:
        frets = int(frets)
        if frets < 0:
            #Go to except branch if frets is an int less than zero.
            int("a")
    except:
        print("Please enter an integer greater than or equal to zero.")
        return fretboardPrompt()
    
    print("Your guitar has {} fret(s).".format(frets))
    return frets


def tuneGuitarStringInput(guitarString, notes):
    inputNote = input("What is string {} tuned to? ".format(guitarString+1))
    noteNumber = validNote(inputNote, notes)
    if noteNumber > -1:
        return inputNote, noteNumber
    else:
        print("Please enter a note as the capitalized note letter on its own ",
            "or followed by '#' or lowercase 'b'.")
        return tuneGuitarStringInput(guitarString, notes)


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
    index = 0
    for note in notes:
        if inputNote in note:
            return index
        index += 1
    return -1
