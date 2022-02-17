import random
from telnetlib import STATUS
from turtle import speed
from unicodedata import name

'''
Create a Weapon Class definition according to the following specs:
'''
class Weapon:
    def __init__(self, name, speed, weaponrange):
        self.__name = name
        self.__bullets = 0
        self.__speed = speed
        self.__weaponrange = weaponrange
        self.__status = "active"

    def set_name(self, name):
        self.__name = name

    def set_bullets(self):
        self.__bullets = random.randint(10, 100000)
        
    
    def set_speed(self, speed):
        self.__speed = speed

    def set_range(self, weaponrange):
        self.__weaponrange = weaponrange

    
    
    def get_name(self):
        return self.__name

    def get_bullets(self):
        return self.__bullets
    
    def get_speed(self):
        return self.__speed

    def get_range(self):
        return self.__weaponrange


    def fire_bullet(self):
        if self.__bullets != 0:
            self.__bullets = self.__bullets-1
        
        else:
            self.__status = "inactive"
        




'''
Attributes:

name - user supplied
bullets - random number between 10 and 100000
speed - user supplied
range - user supplied
status - 'Active' (this attribute should be changed to 'Inactive' if bullets 
                    run out.)

Methods:

Create accessor methods for each attribute.

Create a method named 'fire_bullet' that will simulate
firing a bullet. This is accomplished by decreasing the number of bullets by 1 
every time the method is called. When the bullet count reaches zero, it should change
the attribute 'status' to 'Inactive'

'''






