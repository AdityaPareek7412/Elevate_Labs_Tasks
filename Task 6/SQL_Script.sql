USE classicmodels;

SELECT 
    YEAR(orderDate) AS year,
    MONTH(orderDate) AS month,
    SUM(quantityOrdered * priceEach) AS revenue,
    COUNT(DISTINCT orderNumber) AS order_volume
FROM
    orders
JOIN
    orderdetails USING (orderNumber)
GROUP BY year, month
ORDER BY year, month;



