# Assignment 5
# Create Your own built-in class method
# Write a Python class to implement pow(x, n)

class Power:     #class created

    def pow(self,x,n):    #Method
        if x==0 or x==1 or n==1:   #Conditions
            return x
        if x==-1:
            if n%2 ==0:
                return 1
            else:
                return -1
        if n==0:
            return 0
        else:
            return x**n

obj = Power()  #Object creatde

# Taking user input
x = int(input("Enter x value: "))
n = int(input("Enter n value: "))

res = obj.pow(x,n)  #Storing output in a variable
print("pow(", x, ",", n,") =" ,res)