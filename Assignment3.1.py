# Assignment 3.1
# Game of Functions
# Write a Python function to sum all the numbers in a list.

#Function to addup the elements in a list
def sum_list():
    sum = 0
    length = len(lst)
    for i in range(length):
        sum += lst[i]
    return sum

#List from user
lst = []
num = int(input("Enter the number of elements in the list: "))
for i in range(num):
    ele = int(input("Eneter element: ")) #Input the elements
    lst.append(ele)  #Add the elemnets to the empty list
print("List: ", lst)

result = sum_list() #Calling the function
print("Sum of the element in the list: ", result)

