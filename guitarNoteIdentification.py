# Python 3.7.4

import random


def test(notes, guitarStrings, frets):
	testLength = input("\nHow many questions long should this test to be? ")

	try:
		testLength = int(testLength)
		if testLength < 1:
			int("a")
	except:
		print("Please enter an integer greater than 0.")
		return test(notes, guitarStrings, frets)

	print("Please enter notes as the capitalized note letter on its own ",
        "or followed by '#' or lowercase 'b'.")
	score = 0
	for i in range(testLength):
		answer = noteIdentification(notes, guitarStrings, frets)
		if answer:
			score += 1

	print("\nTest complete! Your score is {}/{}.".format(score, testLength))


def noteIdentification(notes, guitarStrings, frets):
	"""
	For string values in square brackets, make sure guitar is tuned by running
	guitarNoteTrainer.py, then check guitar.json
	"""
	string = random.choice(guitarStrings)
	stringNo = string["stringNo"]
	fretNumber = random.randint(0, frets)
	noteText = string["notesOnString"][fretNumber]

	answer = input("\nWhat note is on string {} and fret {}? ".format(
		stringNo, fretNumber)
	)

	if answer in noteText:
		print("Correct.")
		return True
	else:
		print("Wrong.")
		return False
	

