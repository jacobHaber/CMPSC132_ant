# -*- coding: utf-8 -*-
"""CMPSC132 - Homework 1.ipynb
I have included that code snippets for the <a href= 
"https://runestone.academy/runestone/books/published/pythonds3/Introduction/
ObjectOrientedProgramminginPythonDefiningClasses.html">PSADS book below</a>. You 
need to extend the code in order to meet the criteria listed at the end of the 
chapter.
"""

def gcd(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n

class Fraction:
    def __init__(self, top, bottom):
        cmmn = gcd(top, bottom)
        self.num = top // cmmn 
        self.den = bottom // cmmn
        
    def __str__(self):
        return "{:d}/{:d}".format(self.num, self.den)
    
    def get_num(self):
        return self.num
    
    def get_den(self):
        return self.num

    def __eq__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = other_fraction.num * self.den
        return first_num == second_num
    
    def __add__(self, other_fraction):
        if isinstance(other_fraction,int):
            other_fraction = Fraction(other_fraction,1)

        new_num = self.num * other_fraction.den \
        + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)

    def __sub__(self,other_fraction):
        new_num = self.num* other_fraction.den / + self.den * other_fraction.num
        new_den = self.den * other_fraction.num
        return Fraction(new_num,new_den)
    

    def show(self):
        print("{:d}/{:d}".format(self.num, self.den))

    def __myl__(s, o):
        """
        s = a/b , o = c/d
        s*o = ac/db
        """
        new_num = s.num * o.den
        new_den = s.den * o.den 
        
        return Fraction(new_num, new_den)

    def __truediv__(s, o):
        """
        s = a/b , o = c/d
        s*o = ac/db
        """
        new_num = s.num * o.den
        new_den = s.den * o.den 
        
        return Fraction(new_num, new_den)

    def __ge__(self,other_fraction):
        first_num = self.num * other_fraction.den
        second_num = other_fraction.num * self.den
        return first_num >= second_num

    def __lt__(self,other_fraction):
        first_num = self.num * other_fraction.den
        second_num = other_fraction.num * self.den
        return first_num < second_num    


x = Fraction(1, 2)
x.show()
y = Fraction(2, 3)
print(y)
assert y == Fraction(2,3) #not moving forward till passes test (eq check)
print(x + y)
assert x + y == Fraction(7,6)
print(x == y)

"""# COMPLETE THE FRACTION CLASS
<a href= 
"https://runestone.academy/runestone/books/published/pythonds3/Introduction/
Exercises.html"> You can also find these questions in the book. </a><br>
1. Implement the simple methods get\_num and get\_den that will return the 
numerator and denominator of a fraction.

2. In many ways it would be better if all fractions were maintained in lowest terms
right from the start. Modify the constructor for the Fraction class so that GCD is 
used to reduce fractions immediately. Notice that this means the \_\_add\_\_ 
function no longer needs to reduce. Make the necessary modifications.

3. Implement the remaining simple arithmetic operators (\_\_sub\_\_, \_\_mul\_\_, 
and \_\_truediv\_\_).

4. Implement the remaining relational operators (\_\_gt\_\_, \_\_ge\_\_, \_\_lt\_\
_, \_\_le\_\_, and \_\_ne\_\_).

5. Modify the constructor for the fraction class so that it checks to make sure 
that the numerator and denominator are both integers. If either is not an integer, 
the constructor should raise an exception.

6. In the definition of fractions we assumed that negative fractions have a 
negative numerator and a positive denominator. Using a negative denominator would 
cause some of the relational operators to give incorrect results. In general, this 
is an unnecessary constraint. Modify the constructor to allow the user to pass a 
negative denominator so that all of the operators continue to work properly.

7. Research the \_\_radd\_\_ method. How does it differ from \_\_add\_\_? When is 
it used? Implement \_\_radd\_\_.

8. Repeat the last question but this time consider the \_\_iadd\_\_ method.

9. Research the \_\_repr\_\_ method. How does it differ from \_\_str\_\_? When is 
it used? Implement \_\_repr\_\_.
"""
#Test 1
x.get_num()
assert x.get_num() == 1
y.get_den()
print(y.get_den())
assert y.get_den() == 3
# Test 2
z = Fraction(3,6)
print(z)  #should be 1/2
assert z == Fraction(1,2)
# Test 3
# __sub__
z = x-y
print(z)
assert z == Fraction(-1,6)
# __mul__
z = x*y
print(z)
assert z == Fraction(1,3)
# __truediv__
# from __future__ import division  #this might need to be imported
z = x/y
print(z)
assert z == Fraction(3,4)
# Test 4
# __gt__
assert (x>y) == False
# __ge__
assert (x>=y) == False
# __lt__
assert (x<y) == True
# __le__
assert (x<=y) == True
# __ne__
assert (x!=y) == True
#Test 5
try:
    alpha = Fraction(1.2,2.2)
except:
    print('that doesn\'t work!')
#Test 6
beta = Fraction(3, -5)
print(beta)
print(beta.get_num())
print(beta.get_den())
assert beta == Fraction(-3, 5)
#Test 7 radd
print(x + 1)
print(1 + x)
assert (x + 1) == Fraction(3,2)
assert (1 + x) == Fraction(3,2)
#Test 8 iadd
for i in range(y.get_den()):
    x += i
    print(x)
assert x ==  Fraction(7,2)
#Test 9
"""
Research the __repr__ method. How does it differ from __str__? When is it used? 
Implement __repr__.
WRITE A STATEMENT HERE!
"""
class LogicGate:
    def __init__(self, lbl):
        self.name = lbl
        self.output = None
    def get_label(self):
        return self.name
    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output
class BinaryGate(LogicGate):
    def __init__(self, lbl):
        super(BinaryGate, self).__init__(lbl)
        self.pin_a = None
        self.pin_b = None
    def get_pin_a(self):
        if self.pin_a == None:
            return int(input("Enter pin A input for gate " + self.get_label() + ": "))
        else:
            return self.pin_a.get_from().get_output()
    def get_pin_b(self):
        if self.pin_b == None:
            return int(input("Enter pin B input for gate " + self.get_label() + ": "))
        else:
            return self.pin_b.get_from().get_output()
    def set_next_pin(self, source):
        if self.pin_a == None:
            self.pin_a = source
        else:
            if self.pin_b == None:
                self.pin_b = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")
class AndGate(BinaryGate):
    def __init__(self, lbl):
        BinaryGate.__init__(self, lbl)
    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 and b == 1:
            return 1
        else:
            return 0
class OrGate(BinaryGate):
    def __init__(self, lbl):
        BinaryGate.__init__(self, lbl)
    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 or b == 1:
            return 1
        else:
            return 0
class UnaryGate(LogicGate):
    def __init__(self, lbl):
        LogicGate.__init__(self, lbl)
        self.pin = None
    def get_pin(self):
        if self.pin == None:
            return int(input("Enter pin input for gate " + self.get_label() + ": "))
        else:
            return self.pin.get_from().get_output()
    def set_next_pin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")
class NotGate(UnaryGate):
    def __init__(self, lbl):
        UnaryGate.__init__(self, lbl)
    def perform_gate_logic(self):
        if self.get_pin():
            return 0
        else:
            return 1
class Connector:
    def __init__(self, fgate, tgate):
        self.from_gate = fgate
        self.to_gate = tgate
        tgate.set_next_pin(self)
    def get_from(self):
        return self.from_gate
    def get_to(self):
        return self.to_gate
g1 = AndGate("G1")
g2 = AndGate("G2")
g3 = OrGate("G3")
g4 = NotGate("G4")
c1 = Connector(g1, g3)
c2 = Connector(g2, g3)
c3 = Connector(g3, g4)
print(g4.get_output())
"""# LOGIC GATE PROBLEM
Research other types of gates that exist (such as NAND, NOR, and XOR). Add them to 
the circuit hierarchy. How much additional coding did you need to do?
The most simple arithmetic circuit is known as the half adder. Research the simple 
half-adder circuit. Implement this circuit.
Bonus: 10 Points - Extend that circuit and implement an 8-bit full adder.
"""