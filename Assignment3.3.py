# Assignment 3.3
# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

#Function to count Upper & Lower case characters
def count():
    dict1 = {"upper_count":0,"lower_count":0} #Create empty dictionary

    for i in str1:
        if i.isupper():
            dict1["upper_count"] +=1 #Add upper count to key as value
        elif i.islower():
            dict1["lower_count"] +=1 #Add lower count to key as value

    print("No. of Upper case characters: ", dict1["upper_count"])
    print("No. of Lower case characters: ", dict1["lower_count"])

str1 = input("Enter any string: ") #User input string
count() #Calling the function




