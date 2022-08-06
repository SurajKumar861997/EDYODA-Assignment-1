# Assignment 4.2
# Find the way with Maps
# Write a Python program to triple all numbers of a given list of integers. Use Python map


#Taking user-input for a list
num = int(input("Enter the total number of elements in the list: "))
lst = []
for i in range(num):
    ele = int(input("Enter element: "))
    lst.append(ele)
print("OG List: ",lst)

#Function to triple the elements of the list
def triple(lst):
    return lst*3

result = list(map(triple,lst)) #Calling the function inside map and converting data to List
print("New List after tripling elements: ",result)