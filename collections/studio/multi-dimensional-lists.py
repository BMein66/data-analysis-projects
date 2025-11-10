food = "water bottles,meal packs,snacks,chocolate"
equipment = "space suits,jet packs,tool belts,thermal detonators"
pets = "parrots,cats,moose,alien eggs"
sleep_aids = "blankets,pillows,eyepatches,alarm clocks"

# a) Use split to convert the strings into four cabinet lists. Alphabetize the contents of each cabinet.
food_list = food.split(',')
food_list.sort()
print(food_list)

equipment_list = equipment.split(',')
equipment_list.sort()
print(equipment_list)

pets_list = pets.split(',')
pets_list.sort()
print(pets_list)

sleepaids_list = sleep_aids.split(',')
sleepaids_list.sort()
print(sleepaids_list)


# b) Initialize a cargo_hold list and add the cabinet lists to it. Print cargo_hold to verify its structure.
cargohold = [[food_list], [equipment_list], [pets_list], [sleepaids_list]]
print(cargohold)


# c) Query the user to select a cabinet (0 - 3) in the cargo_hold.
question = int(input('Select a cabinet (0-3) in the cargo hold:'))




# d) Use bracket notation and format to display the contents of the selected cabinet. If the user entered an invalid number, print an error message.
selected_cabinet = cargohold[question]
print (selected_cabinet)

#I can't get this part to work:
#if question > len(cargohold):
    #print ("Please print a number between 0 and 3")
#I can't get that part to work





# e) Modify the code to query the user for BOTH a cabinet in cargo_hold AND a particular item. Use the in method to check if the cabinet contains the selected item, then print “Cabinet ____ DOES/DOES NOT contain ____.”
#this was my best guess and it doesn't work. 
question_cabinet = int(input('Select a cabinet (0-3) in the cargo hold:'))
question_item = int(input('Select an item number (0-3) from that cabinet:'))
print(f"Cabinet {cargohold[question_cabinet]} contains {cargohold[question_cabinet, question_item]}.")
