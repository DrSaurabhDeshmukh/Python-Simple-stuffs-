'''
Abstraction:
Information hiding
- In order to implement abstraction we need Abstract class
-  Normal is not an abstract class
- in order to make a normal class as abstract we need the help of
external library which is abc
==> from abc import ABC
- next step is to inherit this ABC class into a normal class
- till now our class Bank is Partially abstract class
- to complete it, we need to write at least one abstract method
- normal methods written in a abstract class are instance/
  non abstract methods
- in order to create abstract method
  use @asbtarctmethod decorator
- we can add non  abstract methods also

Rule: we must have to write an implementation of an
 abstract method into a child class
'''
from abc import ABC,abstractmethod
class Bank(ABC):

    @abstractmethod
    def credit(self): # abstract method
        pass

    def info(self): # non abstract method
        print('Bank Name:','SBI')
        print('IFSC','SBI987700')



