CREATE DATABASE sales_and_customers;	# Creating the Database.

USE sales_and_customers;	# To use the Database for creating tables.

# Creating table1-SalesPeopl with columns.
CREATE TABLE SalesPeople (
    Snum INT PRIMARY KEY,
    Sname VARCHAR(20) UNIQUE,
    City VARCHAR(20),
    Comm INT
);
# Inserting values to the columns.
INSERT INTO SalesPeople(Snum, Sname, City, Comm) VALUES(1001, "Peel", "London", 12);
INSERT INTO SalesPeople(Snum, Sname, City, Comm) VALUES(1002, "Serres", "Sanjose", 13);
INSERT INTO SalesPeople(Snum, Sname, City, Comm) VALUES(1004, "Motika", "London", 11);
INSERT INTO SalesPeople(Snum, Sname, City, Comm) VALUES(1007, "Rifkin", "Barcelona", 15);
INSERT INTO SalesPeople(Snum, Sname, City, Comm) VALUES(1003, "Axelrod", "Newyork", 10);
SELECT * FROM SalesPeople;	 # To view the table.


# Creating table2-Customers with columns.
CREATE TABLE Customers (
    Cnum INT PRIMARY KEY,
    Cname VARCHAR(20),
    City VARCHAR(20) NOT NULL,
    Snum INT,
    FOREIGN KEY (Snum)
        REFERENCES SalesPeople (Snum)
);
# Inserting values to the columns.
INSERT INTO Customers(Cnum,Cname, City, Snum) VALUES(2001, "Hoffman", "London", 1001);
INSERT INTO Customers(Cnum,Cname, City, Snum) VALUES(2002, "Giovanni", "Rome", 1003);
INSERT INTO Customers(Cnum,Cname, City, Snum) VALUES(2003, "Liu", "Sanjose", 1002);
INSERT INTO Customers(Cnum,Cname, City, Snum) VALUES(2004, "Grass", "Berlin", 1002);
INSERT INTO Customers(Cnum,Cname, City, Snum) VALUES(2006, "Clemens", "London", 1001);
INSERT INTO Customers(Cnum,Cname, City, Snum) VALUES(2008, "Cisneros", "Sanjose", 1007);
INSERT INTO Customers(Cnum,Cname, City, Snum) VALUES(2007, "Pereira", "Rome", 1004);
SELECT * FROM Customers;	# To view the table.


# Creating table-Orders with columns.
CREATE TABLE Orders (
    Onum INT PRIMARY KEY,
    Amt FLOAT,
    Odate VARCHAR(50),
    Cnum INT,
    Snum INT,
    FOREIGN KEY (Cnum)
        REFERENCES Customers (Cnum),
    FOREIGN KEY (Snum)
        REFERENCES SalesPeople (Snum)
);

# Inserting values to the columns.
INSERT INTO Orders(Onum, Amt, Odate, Cnum, Snum) VALUES(3001, 18.69, "3-10-1990", 2008, 1007);
INSERT INTO Orders(Onum, Amt, Odate, Cnum, Snum) VALUES(3003, 767.19, "3-10-1990", 2001, 1001);
INSERT INTO Orders(Onum, Amt, Odate, Cnum, Snum) VALUES(3002, 1900.10, "3-10-1990", 2007, 1004);
INSERT INTO Orders(Onum, Amt, Odate, Cnum, Snum) VALUES(3005, 5160.45, "3-10-1990", 2003, 1002);
INSERT INTO Orders(Onum, Amt, Odate, Cnum, Snum) VALUES(3006,  1098.16, "3-10-1990", 2008, 1007);
INSERT INTO Orders(Onum, Amt, Odate, Cnum, Snum) VALUES(3009, 1713.23, "4-10-1990", 2002, 1003);
INSERT INTO Orders(Onum, Amt, Odate, Cnum, Snum) VALUES(3007, 75.75, "4-10-1990", 2004, 1002);
INSERT INTO Orders(Onum, Amt, Odate, Cnum, Snum) VALUES(3008, 4273.00, "5-10-1990", 2006, 1001);
INSERT INTO Orders(Onum, Amt, Odate, Cnum, Snum) VALUES(3010, 1309.95, "6-10-1990", 2004, 1002);
INSERT INTO Orders(Onum, Amt, Odate, Cnum, Snum) VALUES(3011, 9891.88, "6-10-1990", 2006, 1001);
select * from Orders;	# To view the table.


# QUESTIONS & ANSWERS:
# Q1. Count the number of Salesperson whose name begin with ‘a’/’A’.
SELECT 
	COUNT(*)
FROM
    SalesPeople
WHERE
    Sname LIKE '%A'OR "a";


# Q2. Display all the Salesperson whose all orders worth is more than Rs. 2000.
SELECT Snum,Onum,Amt FROM orders WHERE Amt > 2000;
# OR for full information
SELECT * FROM orders WHERE Amt > 2000;


# Q3. Count the number of Salesperson belonging to Newyork.
SELECT 
    COUNT(*) AS from_Newyork
FROM
    SalesPeople
WHERE
    City = 'Newyork'
GROUP BY Sname , City;


# Q4. Display the number of Salespeople belonging to London and belonging to Paris.
SELECT 
    Sname, City
FROM
    SalesPeople
WHERE
    City = 'London' OR City = 'Paris'
GROUP BY Sname , City;


# Q5. Display the number of orders taken by each Salesperson and their date of orders.
SELECT 
    Odate, Snum, COUNT(*) AS no_of_orders
FROM
    Orders
GROUP BY Odate , Snum;

  







