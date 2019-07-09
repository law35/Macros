

def sedentary():
	"""Determines macro for sedentary individuals."""
	
	sed = 11
	
	while True:
		try:
			body_weight = int(raw_input("Enter the client's weight in lbs:> "))
		except ValueError:
			print "Please enter numbers only."
			continue
		else:
			break
		
	print "Protein needs: %.2f grams" % body_weight
		
	fats = (body_weight * 0.6)#Calculates fats needed.
	print "Fat needs: %.2f grams max." % fats
		
	protein_fat_cal = ((body_weight * 4) + (fats * 9))#Finds the sum of protein & fat calories.
	cal = (body_weight * sed)#Calculates needed.calories 
	print "Carbohydrate needs: %.2f grams." % (( cal - protein_fat_cal) /4)#Calculates carbohydrates.
	print "Calories needed: %.2f cal" % cal