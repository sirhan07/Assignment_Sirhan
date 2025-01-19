--1. Retrieve customer details
SELECT * 
FROM SalesLT.Customer;
--2. Retrieve customer name data
SELECT 
    Title,
    FirstName,
    MiddleName,
    LastName,
    Suffix
FROM SalesLT.Customer;
--3. Retrieve customer names and phone numbers

 SELECT Salesperson, ISNULL(Title,'') + ' ' + LastName AS CustomerName, Phone
 FROM SalesLT.Customer;

 --Challenge 2: Retrieve data for transportation reports
-- 1. Retrieve a list of cities
 SELECT DISTINCT City, StateProvince
 FROM SalesLT.Address
 
 --2. Retrieve the heaviest products
 SELECT TOP (10) PERCENT WITH TIES Name
 FROM SalesLT.Product
 ORDER BY Weight DESC;

 --Challenge 3: Retrieve product data
 --1. Retrieve product details for product model 1
 SELECT Name, Color, Size
 FROM SalesLT.Product
 WHERE ProductModelID = 1;

 --2. Filter products by color and size
 SELECT ProductNumber, Name
 FROM SalesLT.Product
 WHERE Color IN ('Black','Red','White') AND Size IN ('S','M');

 --3.Filter products by product number
 SELECT ProductNumber, Name, ListPrice
 FROM SalesLT.Product
 WHERE ProductNumber LIKE 'BK-%';

 --4.Retrieve specific products by product number 
 SELECT ProductNumber, Name, ListPrice
 FROM SalesLT.Product
 WHERE ProductNumber LIKE 'BK-[^R]%-[0-9][0-9]';

--Challenge 4.Generate invoice reports
--1. Retrieve customer orders 
 SELECT c.CompanyName, oh.SalesOrderID, oh.TotalDue
 FROM SalesLT.Customer AS c
 JOIN SalesLT.SalesOrderHeader AS oh
     ON oh.CustomerID = c.CustomerID;
