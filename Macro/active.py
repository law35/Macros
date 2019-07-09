

def active():
	"""Determines macro for active individuals."""
	
	active = 13
	
	while True:
		try:
			body_weight = int(raw_input("Enter the client's weight in lbs:> "))
		except ValueError:
			print "Please enter only numbers."
			continue
		else:
			break
			
	print "Protein needs: %.2f grams" % body_weight
		
	fats = (body_weight * 0.6) #Calculates fats needed.
	print "Fat needs: %.2f grams min." % fats
		
	protein_fat_cal = ((body_weight * 4) + (fats * 9))#Finds the sum of protein & fat calories.
	cal = (body_weight * active) #Calculates calories needed.
	print "Carbohydrate needs: %.2f grams." % (( cal - protein_fat_cal) /4)#Calculates carbohydrates.
	print "Calories needed: %.2f cal" % cal