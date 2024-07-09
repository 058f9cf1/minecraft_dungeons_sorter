import item_lists
import extra_tools


def categorise(items):
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
	return [melee, ranged, armour, artefact, unknown]


def sort(items, sorting):
	#Group items by type
	categories = categorise(items)
	
	#Sort each group by sorting
	for i in range(len(categories)):
		categories[i] = sorted(categories[i], key=sorting[i])

	#Check if any items haven't been grouped and display if not
	if categories[4] != []:
		print("**WARNING** The following items are unsorted:")
		extra_tools.print_nice(categories[4])
		input("Press enter to continue")
	
	#Concatenate all groups into one list
	total = categories[0] + categories[1] + categories[2] + categories[3] + categories[4]

	#Set inventoryIndex to the index of the item in total
	for i in range(len(total)):
		total[i]['inventoryIndex'] = i + 1
	
	return total
