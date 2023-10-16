##Creating variables

#some definitions...
"""
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
"""
# for eg "a" and "A" are 2 diff veriables

#legal inputs
"""
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
"""

#illegal inputs
"""
2myvar = "John"
my-var = "John"
my var = "John"
"""

# format of declaring : variable name = value

## long variable names (easier for understanding and debugging)

#Camal Case (used most widely in programming languages)
#Each word, except the first, starts with a capital letter
#for example "myVariableName" 
#looks like the hump of a camal

#Pencil Case (not usually used)
#Each word starts with a capital letter
#for example "MyVariableName" 

#Snake Case (most used by Python)
#Each word is separated by an underscore character:
#for example "my_variable_name" 
#looks like a long snake

#Directly creating - fast & convenient
x = 5 # x is of type int
y = "Name" # x is now of type str 
z = 'Name' #same as above

# for strings can use either double quotations "" or single quotations ''

##Casting - think of it as a case

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#>>  str()     converts to string
#>>  int()     converts to string
#>>  float()   converts to string

#example

a = "3" # a is currently a string > cannot add/subtract
b = int(a) # converts a into a string
print(b+1) # outputs 4 (3+1)

##Variable types
x = 5
y = "John"
print(type(x))
print(type(y))

# type() function
# commonly used as breakpoints when debugging to ensure that you are dealing with the right data type
# outputs as <class 'var_type'>
# eg: <class 'int'> <class 'str'> <class 'float'>

##Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x) #outputs "Orange"
print(y) #outputs "Banana"
print(z) #outputs "Cherry"
#by order

##One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

##Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
#same as x, y, z = "apple", "banana", "cherry"
print(x)
print(y)
print(z)

##Output variables
#in simplier terms use "," for variables of different types and "+" for variables of the same type

##Standard output - one variable at once
x = "Python is awesome"
print(x)

##Output many varibables together
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#alt method (same data type)
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

##!carful of usage of "," and "+" when dealing with float & int varibales
x = float(5.55)
y = float(3.23)
print(x+y) #outputs (8.78)
print(x,y) #outputs (5.55 3.23)

#wrong example
x = 5
y = "John"
print(x + y)
#cannot use "+" between vaiables not of the same data type

##global variables

x = "awesome" #defined outside a scope of function >> global to that function (provided there isnt a bigger function surrounding)

def myfunc():
  global x #redefined using the "global" keyword >> keywords always have the highest priority
  x = "fantastic" #redifinition

myfunc()

print("Python is " + x) #outputs x as "fantastic" when accessed outside a scope



