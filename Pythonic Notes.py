# Notes of the book "Learn Python the Hard Way" by Zed Shaw

#                         code is not executed - Useful for comments

floating point            number = number with decimals (e.g. 4.0)

=                          assign value to a variable

==                       tests whether two things have the same value

;                          concatenate different lines in one

round()               round a floating point number

,                           keep code on the same line

"""                       print all the text between the two """ (unlimited)


                        FORMAT CHARACTERS %

Format
Description	Example
%d	Decimal integers (not floating point).	"%d" % 45 == '45'
%i	Same as %d.	"%i" % 45 == '45'
%o	Octal number.	"%o" % 1000 == '1750'
%u	Unsigned decimal.	"%u" % -1000 == '-1000'
%x	Hexadecimal lowercase.	"%x" % 1000 == '3e8'
%X	Hexadecimal uppercase.	"%X" % 1000 == '3E8'
%e	Exponential notation, lowercase 'e'.	"%e" % 1000 == '1.000000e+03'
%E	Exponential notation, uppercase 'E'.	"%E" % 1000 == '1.000000E+03'
%f	Floating point real number.	"%f" % 10.34 == '10.340000'
%F	Same as %f.	"%F" % 10.34 == '10.340000'
%g	Either %f or %e, whichever is shorter.	"%g" % 10.34 == '10.34'
%G	Same as %g but uppercase.	"%G" % 10.34 == '10.34'
%c
Character format (e.g. 35 = "#")
"%c" % 34 == '"'
%r	Repr format (debugging format).	"%r" % int == "<type 'int'>"
%s	String format.	"%s there" % 'hi' == 'hi there'
%%	A percent sign.	"%g%%" % 10.34 == '10.34%'


                             ESCAPE SEQUENCES

\xhh
Character with hex value hh
\ooo
Character with octal value ooo
Escape sequence
Function
\\
Backslash (\)
\'
Single-quote (')
\"
Double-quote (")
\a
ASCII bell (BEL)
\b
ASCII backspace (BS)
\f
ASCII formfeed (FF)
\n
ASCII linefeed (LF)
\N{name}
Characted named {name} in the Unicode database (Unicode only)
\r
Carriage return (CR)
\t
Horizontal Tab (TAB)
\uxxxx
Character with 16-bit hex value xxxx (u'' string only)
\Uxxxxxxxx
Character with 32-bit hex value xxxxxxxx (u" string only)
\v
ASCII vertical tab (VT)


                             COMMANDS FOR FILES

seek(offset,from_what)
In file "f" - offset means how many position you will move; from_what defines point of reference
Command
Function
close
Closes the file
read
Reads the content of the file. Result assignable to a variable
readline
Reads just one line of a text file
truncate
Empties the file
write('stuff')
Writes 'stuff' to the file

modules                 additional functionalities that can be imported for a specific function ("libraries")

return                  return what the function does

PEMDAS                  order of inside-out math operations

int()                   turn string into integer

float()                 turn string into floating point

documentation           def name(arg):
                                   """ documentation """

help                      to read the documentation > help(file.function)


                             COMMANDS FOR LISTS

split               Split according to the specified divider (e.g ' ')
sorted              Sort list
pop                 Removes and returns object from list


                                      TRUTH TABLES

NOT

not False
True
not True
False

OR

True or False
True
True or True
True
False or True
True
False or False
False

AND

True and False
False
True and True
True
False and True
False
False and False
False

NOT OR

not(True or False)
False
not(True or True)
False
not(False or True)
False
not(False or False)
True

NOT AND

not(True and False)
True
not(True and True)
False
not(False and True)
True
not(Falseand False)
True
!=

1 =! 0
True
1 =! 1
False
0 =! 1
True
0 =! 0
False
==

1 == 0
False
1 == 1
True
0 == 1
False
0 == 0
True


                               KEYWORDS

and	            Logical and
True and False == False

as              Part of the with-as statement
Create an alias while importing a module.
with X as Y: pass
import math as my_alias

assert	Assert (ensure) that something is true
assert False, "Error!"

break	Stop this loop right now
while True: break

class	Define a class
class Person(object)

continue	'''Don't process more of the loop, do it again.'''
while True: continue

def	Define a function
def X(): pass

del	Delete from dictionary
del X[Y]

elif	Else if condition

else	Else condition

except	If an exception happens, do this
except ValueError, e: print e

exec	Run a string as Python
exec 'print "hello"'

finally	Exceptions or not, finally do this no matter what
finally: pass

for	Loop over a collection of things
for X in Y: pass

from	Importing specific parts of a module
from x import Y

global	Declare that you want a global variable
global X

if	If condition

import	Import a module into this one to use
import os

in	Part of for-loops. Also a test of X in Y
for X in Y:
    pass also 1 in [1] == True

is	Like == to test equality
1 is 1 == True

lambda	Create a short anonymous function

not	Logical not
not True == False

or	Logical or
True or False == True

pass	This block is empty
def empty(): pass

print	Print this string
print 'this string'

raise	Raise an exception when things go wrong
raise ValueError("No")

return	Exit the function with a return value
def X(): return Y

try	Try this block, and if exception, go to except
try: pass

while	While loop
while X: pass

with	With an expression as a variable do
with X as Y: pass

yield	Pause here and return to caller
def X(): yield Y; X().next()


                                   DATA TYPES

True	True boolean value
True or False == True

False	False boolean value
False and True == False

None	Represents "nothing" or "no value"
x = None

strings	Stores textual information
x = "hello"

numbers	Stores integers
i = 100

floats	Stores decimals
i = 10.389

lists	Stores a list of things
j = [1,2,3,4]

dicts	Stores a key=value mapping of things
e = {'x': 1, 'y': 2}


                                   OPERATORS

+	Addition	2 + 4 == 6
-	Subtraction	2 - 4 == -2
*	Multiplication	2 * 4 == 8
**	Power of	2 ** 4 == 16
/	Division	2 / 4.0 == 0.5
//
Floor division (rounded at min)
2 // 4.0 == 0.0
%	String interpolate or modulus	2 % 4 == 2
<	Less than	4 < 4 == False
>	Greater than	4 > 4 == False
<=	Less than equal	4 <= 4 == True
>=	Greater than equal	4 >= 4 == True
==	Equal	4 == 5 == False
!=	Not equal	4 != 5 == True
<>	Not equal	4 <> 5 == True
( )	Parentheses	len('hi') == 2
[ ]	List brackets	[1,3,4]
{ }	Dict curly braces	{'x': 5, 'y': 10}
@	At (decorators)	@classmethod
,	Comma	range(0, 10)
:	Colon	def X():
.	Dot	self.x = 10
=	Assign equal	x = 10
;   Semi-colon
print "hi"; print "there"
+=	Add and assign	x = 1; x += 2
-=	Subtract and assign	x = 1; x -= 2
*=	Multiply and assign	x = 1; x *= 2
/=	Divide and assign	x = 1; x /= 2
//=	Floor divide and assign	x = 1; x //= 2
%=	Modulus assign	x = 1; x %= 2
**=	Power assign	x = 1; x **= 2


                                  CLASSES and OOP

# Words

class
Tell Python to make a new type of thing.

object
Two meanings: the most basic type of thing, and any instance of some thing.

instance
What you get when you tell Python to create a class.

def
How you define a function inside a class.

self
Inside the functions in a class, self is a variable for the instance/object being accessed.

inheritance
The concept that one class can inherit traits from another class, much like you and your parents.

composition
The concept that a class can be composed of other classes as parts, much like how a car has wheels.

attribute
A property classes have that are from composition and are usually variables.

is-a
A phrase to say that something inherits from another, as in a "salmon" is-a "fish."

has-a
A phrase to say that something is composed of other things or has a trait, as in "a salmon has-a mouth."

# Sentences

1.  class X(Y)
"Make a class named X that is-a Y."

2. class X(object): def __init__(self, J)
"class X has-a __init__ that takes self and J parameters."

3. class X(object): def M(self, J)
"class X has-a function named M that takes self and J parameters."

4. foo = X()
"Set foo to an instance of class X."

5. foo.M(J)
"From foo get the M function, and call it with parameters self, J."

6. foo.K = Q
"From foo get the K attribute and set it to Q."

                    BASIC OBJECT-ORIENTED ANALYSIS AND DESIGN

1. Write or draw about the problem
2. Extract key concept from 1 and research them
3. Create a class hierarchy and object map for the concepts
4. Code the classes and a test to run them
5. Repeat and refine

1. Write it down
Write down - draw diagrams - notes - whatever it takes to express the key concepts in words

2. Key concepts
List nouns and verbs and how they are related - useful for future classes, objects and functions naming

3. Create class hierarchy
Nouns > Create a simple outline/tree of the concepts and how they are related as classes
Verbs > Functions for the classes found above

4. Skeleton code
Only classes and functions, nothing more. Write a test with this code and run it.

5. Repeat and refine
Add more functionalities and refine existing code


                         INHERITANCE

"One class will get most or all of its features from a parent class."

# Types of interaction

Actions on the parent imply an action on the child.

        "Putting functions in a base class (i.e., Parent) will automatically get all subclasses (i.e., Child) those features."

Actions on the child override the action on the parent.

         "To override the function in the Child class you must define a function with the same name."

Actions on the child alter the action on the parent.

         A. before
         B. using "super" - after

# Multiple inheritance

Need to use super (class1, class2)


                    NEW PROJECT using the skeleton

1. Make a copy of skeleton directory > Rename it after project name
2. Rename the NAME directory with the project name
3. Edit setup.py with the information of the project
4. Rename test/NAME_test.py with the module name
5. Double check that everything is working with nosetests

CODE!
