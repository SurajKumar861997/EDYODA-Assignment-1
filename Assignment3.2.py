# Assignment 3.2
# String inside the function
# Write a Python program to reverse a string.

#Funtion to reverse a string
def rev():
    str2 = str1[::-1] #Slicing operator to reverse
    return str2

str1 = input("Enter any word to reverse: ") #User input string

result = rev() #Callig the function
print("The reversed word is: ",result)


