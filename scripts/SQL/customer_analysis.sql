SELECT s.customer_id AS Customer, c.age AS Age, i.item_name AS Item, SUM(o.quantity) AS Quantity
FROM Orders AS o
LEFT JOIN Sales AS s
ON o.sales_id = s.sales_id
LEFT JOIN Customers AS c 
ON s.customer_id = c.customer_id
LEFT JOIN Items AS i
ON o.item_id = i.item_id
WHERE c.age BETWEEN 18 AND 35 AND o.quantity IS NOT NULL
GROUP BY s.customer_id, c.age, i.item_name
HAVING SUM(o.quantity) > 0;