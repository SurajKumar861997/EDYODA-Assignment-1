# Assignment2.2
# Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values

dict1 = {} #Creating an empty dictionary
# ASCII value of a-z ranges from 97-122

for i in range(97,123): #Defining the range of ASCII value from a to z
    dict1[chr(i)] = i   #Assigning keys and values to the empty dictionary

print(dict1)
