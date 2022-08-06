# Assignment 4.1
# Play with Lambda
# Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.


#Function to add any given number with 25
def add(x):
    return lambda num :  x + num  #lambda function

num = int(input("Enter any number to add with 25: ")) #User-input

result = add(25)  #Calling the function
print("Result: ",result(num))