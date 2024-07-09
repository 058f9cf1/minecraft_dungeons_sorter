def print_nice(categories):
#Output a formatted table to the terminal
	#Make sure the argument is a 1-dimensional list
	if not isinstance(categories[0], list):
		categories = [categories]

	type_length = 0
	power_length = 0

	#Get the maximum length of a row
	for category in categories:
		for i in category:
			tl = len(i['type'])
			pl = len(str(i['power']))
			if tl > type_length:
				type_length = tl
			if pl > power_length:
				power_length = pl
	type_length += 1

	#Calculate total row length
	total_length = 5 + type_length + power_length + 1

	#Print table
	print("{0:4} {1:{2}} {3}".format("Indx", "Name", type_length, "Power"))
	print("-" * total_length)
	for category in categories:
		for i in category:
			j = -1
			if 'inventoryIndex' in i:
				j = i['inventoryIndex']
			print("{0:<4} {1:{2}} {3}".format(j, i['type'], type_length, i['power']))
		print("")
