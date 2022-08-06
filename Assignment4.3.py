# Assignment 4.3
# Write a Python program to square the elements of a list using map() function.


#Taking user-input for a list
num = int(input("Enter the total number of elements in the list: "))
lst = []
for i in range(num):
    ele = int(input("Enter element: "))
    lst.append(ele)
print("OG List: ",lst)

#Function to square the elements of the list
def square(lst):
    return lst**2

result = list(map(square,lst)) #Calling the function inside map and converting data to List
print("New List after squaring elements: ",result)