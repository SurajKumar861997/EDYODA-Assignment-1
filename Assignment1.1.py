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


# Write a Python program to get the Fibonacci series between 0 to 50
start = 0
end = 1
while end<50:
    print(end)
    start, end = end, start+end
