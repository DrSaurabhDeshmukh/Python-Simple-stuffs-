"""
OOP: Object Oriented programming
Everything in python is an object

The thing/data/function/anything which is present iin the memory
nothing but an object

Physical existance of an element is nothing but an object.

#Example:
a = 100
# here a is a reference to 100 and 100 is an object
# which exist in a memory
# a is referring to the object
------------------------------------------------------
What is a class:
It is a container which contains 2 things
- Properties/attributes==> implemented using variables
- Actions/behaviours ===> implemented methods
-------------------------------------------------
a = [1,2]
print(type(a))
# <class 'list'>
class Laptop:
    #properties/attributes
    RAM= 4
    gen = 2
    processor = 'i7'
    OS = 'Win11'
    HDD = 'SATA'
    size = 1

    #actions/behaviour/methods
    #start
    #restart
    #shutdown
    #sleep
    #hibernet
    #open
    #close
    #Exit
list()
input()
---------------------------
When a function declared inside a class is a method
and when its outside a class termed as a function

method is same as that of function except it contains self reference variable
#############################
how to create a Class
Example:
class className:
    pass
======================
# class name should be in CamelCase
class SampleInfo:
    pass
"""
# lets implement a sample class

x = 100
y = 200
class Sample:
    #x = 10
    #y = 'python'
    print('This is a class')
    def display(self):
        print(x,y)

# Write ones and call multiple times
# call the class
# 1st way:
#Sample().display()

# 2nd way
s = Sample()
s.display()

# Constructor and object
# s = Sample()
# s is an object
# Sample() is a constructor