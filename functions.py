#functions are used to simplify the coding process to reduce the amount of repeated codes used

#syntax
def FUNCTION_NAME():
    CONTENT

#example of a basic function
def function():
  print("Hello from a function")

#calling a function
function()

#functions with one arguement in the parenthesis
def my_function(x):
  print("My Name is " + x)

my_function("Tom")
my_function("Jake")
my_function("Frank")

#functions with two arguement in the parenthesis
def my_function(x, y):
  print("My name is " + x + " and his name is " + y)

my_function("Tom", "Jake")

#Arbitrary Arguments
def find_sum(*numbers):
    result = 0
    
    for num in numbers:
        result = result + num
    
    print("Sum = ", result)

# function call with 3 arguments
find_sum(1, 2, 3)

# function call with 2 arguments
find_sum(4, 9)

#returning values from functions
def my_function(x):
  return 5 * x

print(my_function(3)) #3*5
print(my_function(5)) #5*5
print(my_function(9)) #9*5

#Recursion in functions
#there are 2 main types of functions in python, iterative and recursive

#sample question
#find the factorial of x using functions

#iterative method
def find_fact(x):
    if (x == 1):
        result = 1
        return result
    else:
        result = 1
        for i in range(1, x + 1):  # Start the loop from 1
            result = i * result
        return result

result = find_fact(int(input()))  # Assign the result to a variable here
print(result)  # Now you can print the result in the global scope

#recursive method
def find_fact(x):
    if (x == 1):
        result = 1
        return result
    else:
        result = 1
        result = x * find_fact(x-1)
        return result
result = find_fact(int(input()))  # Assign the result to a variable here
print(result)  # Now you can print the result in the global scope
