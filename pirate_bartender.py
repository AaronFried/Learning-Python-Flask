import random

def find_preferences():
	
	questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
	}
	
	preferences = {}

	for question in questions:

		taste = input(("\n" + questions[question] + " Type Y/N and press enter. ")).lower()
		if taste != "y" and taste != "n":
			print("Arrrrgh, ye landlubber, we don't serve ye if you don't follow directions! No " + question + 
				" ingredients for you, whether you like them or not! \n")
		elif taste == "y":
			preferences[question] = True
		else:
			preferences[question] = False

	return preferences
	

def new_drink(preferences):

	ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
	}

	new_drink = []

	for preference in preferences:
		if preferences[preference] == True:
			new_drink.append(random.choice(ingredients[preference]))

	print("\nArgh! Yer drink has the following ingredients: "+ str(new_drink))

	return new_drink


if __name__ == "__main__":
	while True:
		want_a_drink = taste = input(("\nWant a drink? Type Y/N and press enter. ")).lower()
		if want_a_drink != "y" and want_a_drink != "n":
			print("Arrrrgh, ye landlubber, we don't serve ye if you don't follow directions! No " + question + 
				" ingredients for you, whether you like them or not! \n")
		elif want_a_drink == "y":
			new_drink(find_preferences())
		else:
			print("\nDrive safe!")
			break

		

