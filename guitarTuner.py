# Python 3.7.4

import json
import itertools

"""
The variable "notes" is a list of lists, where each sublist represents a note
and each element in that sublist is a valid string name for that note. 
For example, the note A is represented with the sublist ["A"], and the note 
"C" is represented with the sublist ["C", "B#"].
Any variable metioning noteNumber(s) is an integer referring to an index of 
"notes".  
"""

def tuneGuitar(notes, guitarFile):
    """
    Main function of this document. Writes whatever tuning the user inputs when 
    tuneGuitarPrompt() is called into JSON document guitarFile. 
    """
    openNoteNumbers, tuningText, frets = tuneGuitarPrompt(notes)

    with open(guitarFile, "w") as writeFile:
        count = 0
        guitarStrings = [None]*len(openNoteNumbers)
        for openNoteNumber in openNoteNumbers[::-1]:
            notesOnString = determineNotesOnString(openNoteNumber, notes, frets)
            guitarStrings[count] = {"stringNo": count+1, 
                "notesOnString": notesOnString
            }
            count += 1
        data = {"tuningText": tuningText}
        data["frets"] = frets
        data["strings"] = guitarStrings
        json.dump(data, writeFile, indent=4)

    return data


def determineNotesOnString(openNoteNumber, notes, frets):
    notesOnString = [openNoteNumber]*(frets+1) # +1 accounts for the open note
    notesCycle = itertools.cycle(notes)

    currentCycle = openNoteNumber
    for i in range(openNoteNumber+1):
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
    print("\nNow tuning guitar.")
    stringNumber = getGuitarStringNoInput()
    print("Your guitar has {} strings.".format(stringNumber))

    print("Enter uppercase letters for notes, '#' for sharps and 'b'" + 
        " for flats.")
    openNoteNumbers=[None]*stringNumber
    tuningText=[None]*stringNumber
    for guitarString in range(stringNumber):
        inputNote, noteNumber = tuneGuitarStringInput(guitarString, notes)
        openNoteNumbers[stringNumber-guitarString-1] = noteNumber
        tuningText[stringNumber-guitarString-1] = inputNote

    tuningText = "".join(tuningText)
    print("From strings {} to 1, your guitar is tuned as {}.".format(
        stringNumber, tuningText)
    )

    frets = fretNoInput()
    print("Your guitar has {} fret(s).".format(frets))

    return openNoteNumbers, tuningText, frets



#Input prompts + note validation

def fretNoInput():
    frets = input("Finally, how many frets does your guitar have? ")
    try:
        frets = int(frets)
        if frets < 0:
            #Go to except branch if frets is an int less than zero.
            int("a")
    except:
        print("Please enter an integer greater than or equal to zero.")
        return fretNoInput()
    
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


def getGuitarStringNoInput():
    res = input("How many strings does your guitar have? ")
    try:
        res = int(res)
        if res < 1:
            print("Please enter a number greater than 0.")
            return(getGuitarStringNoInput())
    except:
        print("Please enter a number.")
        return getGuitarStringNoInput()
    return res


def validNote(inputNote, notes):
    """
    "noteNumber" is an index in "notes".
    """
    noteNumber = 0
    for note in notes:
        if inputNote in note:
            return noteNumber
        noteNumber += 1
    return -1
