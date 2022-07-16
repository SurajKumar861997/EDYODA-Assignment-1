#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      hp1
#
# Created:     16-07-2022
# Copyright:   (c) hp1 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Write a Python program to count the number of even and odd numbers from a series of numbers.
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) #Declaring the numbers
even = 0
odd = 0
for i in numbers:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("Number of even numbers : ", even)
print("Number of even numbers : ", odd)
