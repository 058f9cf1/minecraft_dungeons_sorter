import json

import item_lists


def order(items, sorting):
	#Group items by type
	melee = []
	ranged = []
	armour = []
	artefact = []
	unknown = []

	for item in items:
		if item['type'] in item_lists.melee:
			melee.append(item)
		elif item['type'] in item_lists.ranged:
			ranged.append(item)
		elif item['type'] in item_lists.armour:
			armour.append(item)
		elif item['type'] in item_lists.artefact:
			artefact.append(item)
		else:
			unknown.append(item)

	categories = [melee, ranged, armour, artefact, unknown]
	
	#Sort each group by sorting
	for i in range(len(categories)):
		categories[i] = sorted(categories[i], key=sorting[i])
	
	#Check if any items haven't been grouped and display if not
	if categories[4] != []:
		print("**WARNING** The following items are unsorted:")
		for item in categories[4]:
			print(item['type'])
		input("Press enter to continue.")
	
	#Concatenate all groups into one list
	total = categories[0] + categories[1] + categories[2] + categories[3] + categories[4]

	#Set inventoryIndex to the index of the item in total
	for i in range(len(total)):
		total[i]['inventoryIndex'] = i
	
	return total


def sort_items(data):
	data = json.loads(data)

	#Remove equipped items
	equipped = []
	not_equipped = []
	for item in data['items']:
		if not 'inventoryIndex' in item:
			equipped.append(item)
		else:
			not_equipped.append(item)
	
	#Print out the not equipped items
	print("Items to be sorted:\nInventory\n---------")
	for item in not_equipped:
		print(item['type'], item['power'])
	print("Chest\n-----")
	for item in data['storageChestItems']:
		print(item['type'], item['power'])

	#Sort by item name then power level
	sorting = [lambda x: (item_lists.melee.index(x['type']), x['power']),	#Melee
			   lambda x: (item_lists.ranged.index(x['type']), x['power']),	#Ranged
			   lambda x: (item_lists.armour.index(x['type']), x['power']),	#Armour
			   lambda x: (item_lists.artefact.index(x['type']), x['power']),#Artefacts
			   lambda x: (x['type'], x['power'])]							#Unknown

	#Sort the items
	data['items'] = equipped + order(not_equipped, sorting)
	data['storageChestItems'] = order(data['storageChestItems'], sorting)

	return json.dumps(data, indent=1)
