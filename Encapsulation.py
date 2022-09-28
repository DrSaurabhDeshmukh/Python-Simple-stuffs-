"""
Encapsulation means hiding the data
Example: class
----------------------------------------
class Sample:
    x = 70

    def __init__(self):
        self.y = 'python'
        self.z = 44.55
# outside the class members are not "directly" accessible
print(x,y,z)
# they are inside a container, that why not accessible directly
# in order to access them we need help of object/className
------------------------------------------
If we want to implement an encapsulation in programming then we need
to take the help access specifiers:
-public [accessible to all]
-protected
-private
Q: Do we have access specifiers in python?
Ans: No,but we can implement  the same using _ (underscore) convention
=====================================
1. Public: accessible anywhere and to anyone
Example:
x = 'public'
class Sample:
    print(x)
    def m1(self):
        print(x)
s = Sample()
s.m1()
class Test:
    print(x)
------------------------------------------------
class Sample:
    s = 'clas level'
    def m1(self):
        a = 60
        self.name= 'ajit'
        print('m1')
s =  Sample()
# from above, s, self.name, m1 are public members
class Test(Sample):
    def m2(self):
        self.m1()
        # by using inheritance we can access members of Sample here
========================================================
2. Protected:
It(variable,method) will be available within the same class and
to its child class
In order to make variable or method protected
use _ as a prefix
===================================
class Sample:
    _pr = 'protected'
    def _m1(self):
        print('Protected Method')
#s = Sample()
#print(s._pr)
#s._m1()
class Child(Sample):
    print(Sample._pr)
    def m2(self):
        super()._m1()
c =Child()
c.m2()

class Normal(Sample):# without inheritance we are nt able to access protected members
    def m3(self):
        print('Normal:',self._pr)
        self._m1()
n = Normal()
n.m3()
============================================
3. Private:
It is only available within the same class
Outside class we can not access private members
bcz its restricted
in order to implement it: use __ [double underscore]
================================================
class Sample:
    __x = 'private'

    def __m1(self):
        print('Private method')
s = Sample()
#print(s.__x) #private variable
#s.__m1() # private method

# try to access using class Name
print(Sample.__x)
===============================================
class Sample:
    __x = 'private'

    def __m1(self):
        print('Private method')
    # private members are accessible inside a class
    def m2(self):
        print(Sample.__x)
        self.__m1()
s = Sample()
#print(s.__x) #private variable
#s.__m1() # private method

# try to access using class Name
#print(Sample.__x)
s.m2()
=======================================
# Name mangling technique:
It is used to access private members outside the class
==================================
class Sample:
    __x = 'private'
    y = 100
    def __m1(self):
        print('Private method')
s =  Sample()
#print(s.__x) # this is not allowed
# use name mangling
#print(dir())
print(s._Sample__x)
s._Sample__m1()
print(dir(s))
========================================
class Sample:
    x = 100
    _y = 200
    __z = 300

s =Sample()
s.
============================================
"""
class Sample:
    _x = 30
    def m1(self):
        self._x = 300
        print(self._x)
s = Sample()
s.m1()
s._x = 45
print(s._x)
class test:
    def m2(self):
        print(Sample._x)
        Sample._x= 700
t  = test()
t.m2()
print(t._x)


