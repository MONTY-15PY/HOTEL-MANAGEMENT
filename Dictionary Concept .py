'''
syntax:

var_name = {key:value, key:value2}

'''

# Step 1 Intitialize a Dict
menu = {} # empty


#Step 2 How To add element
menu["Rabri Faluda"] = 60 
menu["Lassi"]        = 40
menu["Cup icecream"] = 20

#print(menu)





#Step 3 How to remove a elements

#del menu[" Rabri Faluda"]
#print(menu)


#Step 4 How To Acces perticular key

faluda = menu["Rabri Faluda"]
#print(faluda)

#Step 5 How to update
menu["Rabri Faluda"] = 90
#print(menu)


# How to clear dictionary
#menu.clear()
#print(menu)

# How to find a length of a dictionary
print(menu)
print(len(menu))
