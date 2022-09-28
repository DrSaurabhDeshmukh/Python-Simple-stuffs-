"""
Types of Inheritance:
3. Multiple inheritance:
in this type, we may have more than one parent
Example:
    Father            Mother
             child
Hierarchy will be followed from left to right
Means from above ccase we can say,
child will access Father first and then will approach to mother
================================================
class Mother:
    def money(self):
        print('Money from Mother')
class Father:
    #def money(self):
     #   print('Money from Father')
     def car(self):
         print('Car of father')
class Child(Father,Mother):
    # inheritance with more than one parent
    pass
c  = Child()
c.money()
c.car()
===================================================
MRO: Method resolution order
In case of multiple inheritance
we can inherit many Parents hence in order to check the hierarchy of
how methods are searched in parent classes
---------------------------------------

class A:
    pass
class B:
    pass
class C():
    pass
class D(B,C,A):
    pass
# className.mro()
print(D.mro())
print(D.__mro__)
================================
class x:
    pass
class y:
    pass
class z(x,y):
    pass
class a(z,x,y):
    pass
print(a.mro())
==============================================
class a:
    def m1(self):
        print('a')
    class b:
        def m2(self):
            print('b')
class c(a):
    pass
c1 = c()
c1.m1()

c2 = c1.b()
c2.m2()
"""
#outer ka object
ob = a()
ob.m1()
#inner ka object
ob2 = ob.b()
ob2.m2()
"""
"""




