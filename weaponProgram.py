from multiprocessing.sharedctypes import Value
import weaponClass as w
import csv


'''
- Craete a program that will read the contents of the file 'weapons.txt'. Each record in the file represents the specs to a weapon.
- Create an instance of the weapon object for each record. 
- Create a dictionary that will contain the name of the weapon as the key and the number of bullets as the value. 
- Print out details of each weapon using the object's methods only (as per comments below). 
- Fire all bullets of the weapon and print a countdown of bullets remaining (run exe file to visualize, HINT: use end='\r' in your print statement).
- Print out the name of the weapon and the number of bullets from the dictionary.

HINT: Follow the comments for each line to help with the logic of the problem.
'''


# create a file object to open the file in read mode
weapon1 = open("weapons.csv", 'r')

# create a csv object from the file object
weapon_file = csv.reader(weapon1, delimiter=',')

#skip the header row
next(weapon_file)

#create an empty dictionary named 'weapons_dict'
weapons_dict = {}

#use a for loop to iterate through every row of the csv file
for record in weapon_file:
    #use variables for name,speed and range (optional)
    name = record[0]
    speed = record[1]
    weaponrange = record[2]

  #  print(record[0]+record[1]+record[2])
    # create an instance of the weapon object using the 
    # specs from the csv file (name,speed and range) 
    my_weapon = w.Weapon(name, speed, weaponrange)
   


    # append the name and bullet count to 'weapons_dict'
    my_weapon.set_bullets()
   # weapons_dict['name'] = name
    #weapons_dict['bullet'] = my_weapon.get_bullets()
    weapons_dict[name] = my_weapon.get_bullets()

    

    # print out the name of the weapon using the appropriate method of the object 
    print("\n")
    print("Name: ", my_weapon.get_name())

    # print out the speed of the weapon using the appropriate method of the object
    print("Speed: ", my_weapon.get_speed())

    # print out the range of the weapon using the appropriate method of the object
    print("Range: ", my_weapon.get_range())

    # print out the number of bullets of the weapon using the appropriate method of the object
    print("Bullets: ", my_weapon.get_bullets())

    #use an input statement to halt the program and wait for the user - 
    input("Press any key to fire the weapon")

    # use an appropriate loop to keep firing the weapon until all bullets run out
    for i in range(my_weapon.get_bullets()):

        # call the appropriate method to fire a bullet
        my_weapon.fire_bullet()
    
        # print out the bullet count every time the weapon is fired
        
        print("Number of bullets", my_weapon.get_bullets(), end='\r')

    


#using a loop print out the name and number of bullets from the dictionary
for items in weapons_dict:
    print("name of the weapon is", items, "\t Number of bullets: ", weapons_dict[items])
    #print("Number of bullets", weapons_dict[items])

