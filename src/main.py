#!/usr/bin/env python3

import sys
import json
import sort_items
import item_lists
import extra_tools


#Sort by item name then power level
sorting = [lambda x: (item_lists.melee.index(x['type']), x['power']),	#Melee
		   lambda x: (item_lists.ranged.index(x['type']), x['power']),	#Ranged
		   lambda x: (item_lists.armour.index(x['type']), x['power']),	#Armour
		   lambda x: (item_lists.artefact.index(x['type']), x['power']),#Artefacts
		   lambda x: (x['type'], x['power'])]							#Unknown

#Name of the file to be loaded
file_name = sys.argv[1]

#Load the json dats from file
f = open(file_name)
data = json.load(f)
f.close()

#Get the inventories
inventory_items = data['items']
chest_items = data['storageChestItems']

#Remove equipped items
equipped = []
not_equipped = []
for i in range(len(inventory_items)):
	if not 'inventoryIndex' in inventory_items[i]:
		equipped.append(inventory_items[i])
	else:
		not_equipped.append(inventory_items[i])

#Print out the not equipped items
extra_tools.print_nice(not_equipped)

#Sort the items
inventory_items = equipped + sort_items.run(not_equipped, sorting)
chest_items = sort_items.run(chest_items, sorting)

#Write the sorted inventories back to the dictionary
data['items'] = inventory_items
data['storageChestItems'] = chest_items

#Write dictionary to outfile
new_file = file_name.rsplit(".", 1)[0] + "_sorted.json"
out_file = open(new_file, "w")
json.dump(data, out_file, indent = 1)
out_file.close()
