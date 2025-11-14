-- join_report.sql
-- 
-- This SQL query generates a detailed e-commerce purchase report by joining
-- four related tables: customers, orders, order_items, and products.
--
-- It returns the following:
--   - customer_name : Name of the customer
--   - order_id      : Unique ID of the order
--   - order_date    : Date when the order was placed
--   - product_name  : Name of the purchased product
--   - quantity      : Number of units bought
--   - subtotal      : Price * Quantity for the product in the order
--   - city          : Customer's city
--
-- The results are sorted by order_date in descending (latest first) order.
--
-- This report helps in understanding customer purchases, product demand,
-- and overall sales activity.


SELECT 
    c.name AS customer_name,
    o.order_id,
    o.order_date,
    p.product_name,
    oi.quantity,
    oi.subtotal,
    c.city
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
ORDER BY o.order_date DESC;

