#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      hp1
#
# Created:     16-07-2022
# Copyright:   (c) hp1 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Write a Python program that accepts a word from the user and reverse it.
str1 = input("Enter a word for reverse : ")
length = len(str1)
str2 = str1
for i in range(len(str1)-1,-1,-1):
    print(str1[i], end = "")