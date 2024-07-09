import os
import json


def selection(arr, w):
	#Return a selection that is a valid option
	ans = 0
	while(not ans - 1 in range(len(arr))):
		try:
			ans = int(input("Enter " + w + " to use > "))
		except:
			continue
	return ans


def valid_json(file_name):
	#Determine if a file is a valid json file
	try:
		with open(file_name) as f:
			json.load(f)
	except:
		return False
	return True


def search():
	#Search for saved characters
	print("No file provided, searching for saves...")

	#Determine if save file path exists
	#TODO: Search other save locations (Microsoft Store, Steam) 
	save_dir = os.path.join(os.path.expanduser('~user'), 'Saved Games', 'Mojang Studios', 'Dungeons')
	if(not os.path.isdir(save_dir)):
		print("Dungeons not installed. Note: Searching for saves currently only works for Minecraft Dungeons installed via the Minecraft Launcher")
		return None

	#Get a list of all of the save files
	saves = os.listdir(save_dir)

	#If there are no save files
	if(len(saves) == 0):
		print("No saves detected")
		return None

	#If there is only one save file
	elif(len(saves) == 1):
		print("Found save:", saves[0])
		save_dir = os.path.join(save_dir, saves[0], "Characters")

	#If there are multiple save files
	else:
		print("Found", len(saves), "saves:")
		for save in saves:
			print(saves.index(save) + 1, "-", save)

		#Select one save file
		save_dir = os.path.join(save_dir, saves[selection(saves, "save") - 1], "Characters")

	#Get a list of all of the characters
	characters = [character for character in os.listdir(save_dir) if valid_json(character)]

	#If there are no characters
	if(len(characters) == 0):
		print("No characters detected. Have you decrypted your save file?")
		return None

	#If there is only one character
	elif(len(characters) == 1):
		print("Found character:", characters[0])
		return os.path.join(save_dir, characters[0])

	#If there are multiple characters
	else:
		print("Found", len(characters), "characters:")
		for character in characters:
			print(characters.index(character) + 1, "-", character)

		#Select one character
		return os.path.join(save_dir, characters[selection(characters, "character") - 1])
