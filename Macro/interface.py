from sed import sedentary
from moderate import moderate
from active import active
from very_active import veryactive

print "+----------------------------------------------------------------------------+"
print "|                               Macro Calculator                             |"
print "+----------------------------------------------------------------------------+"
print "|                            Developed by C.Lawshea.                         |"
print "+----------------------------------------------------------------------------+"

def interface():
	"""Interface with input error handling."""
	
	answer = str(raw_input("Sedentary lifestyle, little to no exercise?(Y or N):> "))
	
	if answer.upper() == "Y":
		return sedentary()
	elif answer.upper() == "N":
		answer = str(raw_input("Moderately active job or exercise 2 to 3 times per week?(Y or N):> "))
		
		if answer.upper() == "Y":
			return moderate()
		elif answer.upper() == "N":
			answer = str(raw_input("Active job and exercise 2 to 3 times per week?(Y or N):> "))
			
			if answer.upper() == "Y":
				return active()
			elif answer.upper() == "N":
				return veryactive()
			else:
				print "Please enter Y for yes or N for no."
				interface()
		else:
			print "Please enter Y for yes or N for no."
			interface()
	else:
		print "Please enter Y for yes or N for no."
		interface()
		
		
interface()