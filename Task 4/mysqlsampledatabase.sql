USE classicmodels;

SELECT productName, buyPrice
FROM products
WHERE buyPrice > 100
ORDER BY buyPrice DESC;

SELECT productLine, 
       COUNT(*) AS product_count, 
       AVG(buyPrice) AS average_price
FROM products
GROUP BY productLine
ORDER BY average_price DESC;

SELECT c.customerName, 
       COUNT(o.orderNumber) AS total_orders
FROM customers c
JOIN orders o ON c.customerNumber = o.customerNumber
GROUP BY c.customerName
ORDER BY total_orders DESC;


SELECT customerName
FROM customers
WHERE customerNumber IN (
    SELECT customerNumber
    FROM orders
    GROUP BY customerNumber
    HAVING COUNT(*) > 5
);


SELECT c.customerName, 
       SUM(od.quantityOrdered * od.priceEach) AS total_spent
FROM customers c
JOIN orders o ON c.customerNumber = o.customerNumber
JOIN orderdetails od ON o.orderNumber = od.orderNumber
GROUP BY c.customerName
ORDER BY total_spent DESC
LIMIT 10;


CREATE OR REPLACE VIEW customer_order_summary AS
SELECT c.customerName,
       COUNT(DISTINCT o.orderNumber) AS total_orders,
       SUM(od.quantityOrdered * od.priceEach) AS total_spent
FROM customers c
JOIN orders o ON c.customerNumber = o.customerNumber
JOIN orderdetails od ON o.orderNumber = od.orderNumber
GROUP BY c.customerName;


SELECT * FROM customer_order_summary
ORDER BY total_spent DESC
LIMIT 5;


CREATE INDEX idx_orderdetails_orderNumber
ON orderdetails(orderNumber);


