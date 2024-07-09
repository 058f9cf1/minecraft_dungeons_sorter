#!/usr/bin/env python3

import sys
import json

import sort_items
import item_lists
import saves
import extra_tools


#Get the save file from the argument if provided
if(len(sys.argv) > 1):
	file_name = sys.argv[1]
	if not saves.valid_json(file_name):
		print("Provided file not a valid json file")
		file_name = None

#Otherwise, search for save files
else:
	file_name = saves.search()

#If a valid file
if(not file_name == None):
	#Load the json data from file
	with open(file_name) as f:
		data = json.load(f)

	#Get the inventories
	inventory_items = data['items']
	chest_items = data['storageChestItems']

	#Remove equipped items
	equipped = []
	not_equipped = []
	for item in inventory_items:
		if not 'inventoryIndex' in item:
			equipped.append(item)
		else:
			not_equipped.append(item)

	#Print out the not equipped items
	print("Items to be sorted:")
	extra_tools.print_nice(not_equipped)
	extra_tools.print_nice(chest_items)

	#Sort by item name then power level
	sorting = [lambda x: (item_lists.melee.index(x['type']), x['power']),	#Melee
			   lambda x: (item_lists.ranged.index(x['type']), x['power']),	#Ranged
			   lambda x: (item_lists.armour.index(x['type']), x['power']),	#Armour
			   lambda x: (item_lists.artefact.index(x['type']), x['power']),#Artefacts
			   lambda x: (x['type'], x['power'])]							#Unknown

	#Sort the items
	inventory_items = equipped + sort_items.sort(not_equipped, sorting)
	chest_items = sort_items.sort(chest_items, sorting)

	#Write the sorted inventories back to the dictionary
	data['items'] = inventory_items
	data['storageChestItems'] = chest_items

	#Write dictionary to outfile
	new_file = file_name.rsplit(".", 1)[0] + "_sorted.json"
	with open(new_file, "w") as out_file:
		json.dump(data, out_file, indent = 1)
