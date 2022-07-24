# Assignment2.1
# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples

lst = [(10,3),(2,5),(25,4),(23,1),(16,6),(51,8),(56,2),(20,7),(11,10),(30,9)]  #Taking some random non-empty tuple in a list
number = lst # Assigning the values of the list to another variable

for i in range(len(number)):   #Defining the range of i in number
    for j in range(i, len(number)):   #Defining the range of j
        if number[j][1] < number[i][1]:  #Comparing the last element of each tuple inside the list
            number[i], number[j] = number[j], number[i]  #Swaping the values

print(number)
