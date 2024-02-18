SELECT s.customer_id AS Customer, c.age AS Age, s.item_id AS Item, SUM(s.quantity) AS Quantity
FROM Orders AS o
LEFT JOIN Sales AS s
ON o.sales_id = s.sales_id
LEFT JOIN Customer AS c 
ON s.customer_id = c.customer_id
LEFT JOIN Items AS i
ON o.item_id = i.item_id
WHERE c.age BETWEEN 18 AND 35 AND s.quantity IS NOT NULL
GROUP BY s.customer_id, c.age, s.item_id
HAVING SUM(s.quantity) > 0;