-- Comprehensive seed data for restaurant database

-- Insert 30 sample customers
INSERT INTO customers (full_name, phone, email) VALUES
('John Smith', '555-0101', 'john.smith@email.com'),
('Sarah Johnson', '555-0102', 'sarah.j@email.com'),
('Michael Brown', '555-0103', 'mbrown@email.com'),
('Emily Davis', '555-0104', 'emily.davis@email.com'),
('David Wilson', '555-0105', 'dwilson@email.com'),
('Lisa Martinez', '555-0106', 'lisa.m@email.com'),
('James Anderson', '555-0107', 'janderson@email.com'),
('Maria Garcia', '555-0108', 'maria.g@email.com'),
('Robert Taylor', '555-0109', 'rtaylor@email.com'),
('Jennifer Thomas', '555-0110', 'jthomas@email.com'),
('William Moore', '555-0111', 'wmoore@email.com'),
('Linda Jackson', '555-0112', 'ljackson@email.com'),
('Richard White', '555-0113', 'rwhite@email.com'),
('Patricia Harris', '555-0114', 'pharris@email.com'),
('Christopher Martin', '555-0115', 'cmartin@email.com'),
('Barbara Thompson', '555-0116', 'bthompson@email.com'),
('Daniel Garcia', '555-0117', 'dgarcia@email.com'),
('Susan Martinez', '555-0118', 'smartinez@email.com'),
('Matthew Robinson', '555-0119', 'mrobinson@email.com'),
('Jessica Clark', '555-0120', 'jclark@email.com'),
('Anthony Rodriguez', '555-0121', 'arodriguez@email.com'),
('Ashley Lewis', '555-0122', 'alewis@email.com'),
('Mark Lee', '555-0123', 'mlee@email.com'),
('Michelle Walker', '555-0124', 'mwalker@email.com'),
('Paul Hall', '555-0125', 'phall@email.com'),
('Amanda Allen', '555-0126', 'aallen@email.com'),
('Steven Young', '555-0127', 'syoung@email.com'),
('Melissa King', '555-0128', 'mking@email.com'),
('Kevin Wright', '555-0129', 'kwright@email.com'),
('Laura Lopez', '555-0130', 'llopez@email.com');

-- Insert 50+ menu items across multiple categories
INSERT INTO menu_items (name, description, category, price, is_available) VALUES
-- Appetizers (15 items)
('Spring Rolls', 'Crispy vegetable spring rolls with sweet chili sauce', 'Appetizer', 8.99, 1),
('Bruschetta', 'Toasted bread with tomatoes, basil, and garlic', 'Appetizer', 9.99, 1),
('Calamari', 'Lightly fried squid with marinara sauce', 'Appetizer', 12.99, 1),
('Chicken Wings', 'Spicy buffalo wings with ranch dressing', 'Appetizer', 11.99, 1),
('Mozzarella Sticks', 'Breaded mozzarella with marinara sauce', 'Appetizer', 8.99, 1),
('Stuffed Mushrooms', 'Mushroom caps filled with herbs and cheese', 'Appetizer', 10.99, 1),
('Shrimp Cocktail', 'Chilled shrimp with cocktail sauce', 'Appetizer', 13.99, 1),
('Nachos Supreme', 'Tortilla chips with cheese, jalapeños, and guacamole', 'Appetizer', 11.99, 1),
('Garlic Bread', 'Toasted bread with garlic butter and parmesan', 'Appetizer', 6.99, 1),
('Onion Rings', 'Crispy battered onion rings', 'Appetizer', 7.99, 1),
('Spinach Artichoke Dip', 'Creamy dip served with tortilla chips', 'Appetizer', 10.99, 1),
('Deviled Eggs', 'Classic deviled eggs with paprika', 'Appetizer', 7.99, 1),
('Potato Skins', 'Loaded with bacon, cheese, and sour cream', 'Appetizer', 9.99, 1),
('Edamame', 'Steamed soybeans with sea salt', 'Appetizer', 6.99, 1),
('Crab Cakes', 'Pan-seared crab cakes with remoulade', 'Appetizer', 14.99, 1),

-- Soups & Salads (8 items)
('French Onion Soup', 'Classic soup with caramelized onions and gruyere', 'Soup', 8.99, 1),
('Tomato Basil Soup', 'Creamy tomato soup with fresh basil', 'Soup', 7.99, 1),
('Clam Chowder', 'New England style creamy clam chowder', 'Soup', 9.99, 1),
('Caesar Salad', 'Romaine lettuce with caesar dressing and croutons', 'Salad', 10.99, 1),
('Greek Salad', 'Mixed greens with feta, olives, and vinaigrette', 'Salad', 11.99, 1),
('Cobb Salad', 'Chicken, bacon, egg, avocado, and blue cheese', 'Salad', 13.99, 1),
('Caprese Salad', 'Fresh mozzarella, tomatoes, and basil', 'Salad', 12.99, 1),
('Garden Salad', 'Mixed greens with vegetables and choice of dressing', 'Salad', 8.99, 1),

-- Main Courses (20 items)
('Grilled Salmon', 'Atlantic salmon with lemon butter sauce and vegetables', 'Main Course', 24.99, 1),
('Ribeye Steak', '12oz ribeye with garlic mashed potatoes', 'Main Course', 32.99, 1),
('Filet Mignon', '8oz filet with asparagus and red wine reduction', 'Main Course', 38.99, 1),
('Chicken Parmesan', 'Breaded chicken breast with marinara and mozzarella', 'Main Course', 18.99, 1),
('Grilled Chicken', 'Herb-marinated chicken breast with roasted vegetables', 'Main Course', 17.99, 1),
('BBQ Ribs', 'Full rack of baby back ribs with coleslaw', 'Main Course', 26.99, 1),
('Vegetable Pasta', 'Penne pasta with seasonal vegetables in olive oil', 'Main Course', 16.99, 1),
('Fettuccine Alfredo', 'Creamy parmesan sauce with fettuccine', 'Main Course', 17.99, 1),
('Spaghetti Bolognese', 'Traditional meat sauce with spaghetti', 'Main Course', 18.99, 1),
('Shrimp Scampi', 'Garlic butter shrimp over linguine', 'Main Course', 22.99, 1),
('Beef Burger', 'Angus beef burger with lettuce, tomato, and fries', 'Main Course', 15.99, 1),
('Turkey Club Sandwich', 'Triple-decker with turkey, bacon, and fries', 'Main Course', 14.99, 1),
('Fish and Chips', 'Beer-battered cod with french fries', 'Main Course', 17.99, 1),
('Chicken Tikka Masala', 'Curry chicken with basmati rice', 'Main Course', 19.99, 1),
('Beef Tacos', 'Three soft tacos with beef, cheese, and salsa', 'Main Course', 14.99, 1),
('Pulled Pork Sandwich', 'Slow-cooked pork with BBQ sauce and coleslaw', 'Main Course', 15.99, 1),
('Lobster Tail', '8oz lobster tail with drawn butter', 'Main Course', 42.99, 1),
('Pork Chops', 'Grilled pork chops with apple compote', 'Main Course', 21.99, 1),
('Lamb Chops', 'Herb-crusted lamb chops with mint sauce', 'Main Course', 34.99, 1),
('Vegetarian Lasagna', 'Layered pasta with vegetables and ricotta', 'Main Course', 16.99, 1),

-- Desserts (8 items)
('Chocolate Cake', 'Rich chocolate layer cake with ganache', 'Dessert', 7.99, 1),
('Tiramisu', 'Classic Italian coffee-flavored dessert', 'Dessert', 8.99, 1),
('Cheesecake', 'New York style cheesecake with berry compote', 'Dessert', 8.99, 1),
('Ice Cream Sundae', 'Three scoops with toppings and whipped cream', 'Dessert', 6.99, 1),
('Apple Pie', 'Warm apple pie with vanilla ice cream', 'Dessert', 7.99, 1),
('Crème Brûlée', 'Vanilla custard with caramelized sugar', 'Dessert', 9.99, 1),
('Brownie Sundae', 'Warm brownie with ice cream and chocolate sauce', 'Dessert', 8.99, 1),
('Fruit Tart', 'Fresh seasonal fruit on pastry cream', 'Dessert', 8.99, 1),

-- Beverages (12 items)
('Coca Cola', 'Classic soft drink', 'Beverage', 2.99, 1),
('Diet Coke', 'Zero calorie cola', 'Beverage', 2.99, 1),
('Sprite', 'Lemon-lime soda', 'Beverage', 2.99, 1),
('Iced Tea', 'Freshly brewed sweet or unsweet', 'Beverage', 2.99, 1),
('Lemonade', 'Fresh squeezed lemonade', 'Beverage', 3.49, 1),
('Coffee', 'Hot brewed coffee', 'Beverage', 2.49, 1),
('Espresso', 'Double shot espresso', 'Beverage', 3.99, 1),
('Cappuccino', 'Espresso with steamed milk and foam', 'Beverage', 4.49, 1),
('Hot Chocolate', 'Rich chocolate with whipped cream', 'Beverage', 3.99, 1),
('Orange Juice', 'Freshly squeezed', 'Beverage', 3.99, 1),
('Milk', 'Whole, 2%, or skim', 'Beverage', 2.49, 1),
('Bottled Water', 'Spring water', 'Beverage', 1.99, 1);

-- Insert 20 reservations
INSERT INTO reservations (customer_id, reservation_time, num_guests) VALUES
(1, datetime('now', '+1 day', '18:00'), 4),
(2, datetime('now', '+1 day', '19:30'), 2),
(3, datetime('now', '+2 days', '20:00'), 6),
(4, datetime('now', '+2 days', '19:00'), 3),
(5, datetime('now', '+3 days', '18:30'), 2),
(6, datetime('now', '+3 days', '20:30'), 5),
(7, datetime('now', '+4 days', '19:00'), 4),
(8, datetime('now', '+4 days', '18:00'), 2),
(9, datetime('now', '+5 days', '19:30'), 8),
(10, datetime('now', '+5 days', '20:00'), 3),
(11, datetime('now', '+6 days', '18:30'), 4),
(12, datetime('now', '+6 days', '19:00'), 2),
(13, datetime('now', '+7 days', '20:00'), 6),
(14, datetime('now', '+7 days', '18:00'), 5),
(15, datetime('now', '+8 days', '19:30'), 2),
(16, datetime('now', '+8 days', '20:30'), 4),
(17, datetime('now', '+9 days', '18:00'), 3),
(18, datetime('now', '+9 days', '19:00'), 7),
(19, datetime('now', '+10 days', '20:00'), 2),
(20, datetime('now', '+10 days', '18:30'), 4);

-- Insert 25 sample orders with various statuses
INSERT INTO orders (customer_id, order_time, status, total_amount) VALUES
-- Recent completed orders
(1, datetime('now', '-3 days', '18:30'), 'completed', 0),
(2, datetime('now', '-3 days', '19:15'), 'completed', 0),
(3, datetime('now', '-2 days', '12:45'), 'completed', 0),
(4, datetime('now', '-2 days', '19:00'), 'completed', 0),
(5, datetime('now', '-1 day', '18:20'), 'completed', 0),
(6, datetime('now', '-1 day', '20:00'), 'completed', 0),
(7, datetime('now', '-12 hours'), 'completed', 0),
(8, datetime('now', '-10 hours'), 'completed', 0),
(9, datetime('now', '-8 hours'), 'completed', 0),
(10, datetime('now', '-6 hours'), 'completed', 0),
(11, datetime('now', '-5 hours'), 'completed', 0),
(12, datetime('now', '-4 hours'), 'completed', 0),
(13, datetime('now', '-3 hours'), 'completed', 0),
(14, datetime('now', '-2 hours'), 'completed', 0),
(15, datetime('now', '-90 minutes'), 'completed', 0),
-- Current orders in progress
(16, datetime('now', '-60 minutes'), 'preparing', 0),
(17, datetime('now', '-45 minutes'), 'preparing', 0),
(18, datetime('now', '-30 minutes'), 'preparing', 0),
(19, datetime('now', '-20 minutes'), 'preparing', 0),
(20, datetime('now', '-15 minutes'), 'pending', 0),
(21, datetime('now', '-10 minutes'), 'pending', 0),
(22, datetime('now', '-8 minutes'), 'pending', 0),
(23, datetime('now', '-5 minutes'), 'pending', 0),
(24, datetime('now', '-3 minutes'), 'pending', 0),
(25, datetime('now', '-1 minute'), 'pending', 0);

-- Order 1: Family dinner
INSERT INTO order_items (order_id, menu_item_id, quantity, unit_price) VALUES
(1, 4, 2, 11.99),   -- 2x Chicken Wings
(1, 25, 2, 24.99),  -- 2x Grilled Salmon
(1, 26, 1, 32.99),  -- 1x Ribeye Steak
(1, 29, 1, 17.99),  -- 1x Grilled Chicken
(1, 53, 4, 2.99);   -- 4x Iced Tea

-- Order 2: Date night
INSERT INTO order_items (order_id, menu_item_id, quantity, unit_price) VALUES
(2, 2, 1, 9.99),    -- Bruschetta
(2, 27, 1, 38.99),  -- Filet Mignon
(2, 25, 1, 24.99),  -- Grilled Salmon
(2, 45, 2, 8.99),   -- 2x Cheesecake
(2, 59, 2, 4.49);   -- 2x Cappuccino

-- Order 3: Lunch for two
INSERT INTO order_items (order_id, menu_item_id, quantity, unit_price) VALUES
(3, 19, 2, 10.99),  -- 2x Caesar Salad
(3, 36, 2, 15.99),  -- 2x Beef Burger
(3, 51, 2, 2.99);   -- 2x Coca Cola

-- Order 4: Italian night
INSERT INTO order_items (order_id, menu_item_id, quantity, unit_price) VALUES
(4, 9, 1, 6.99),    -- Garlic Bread
(4, 32, 1, 17.99),  -- Fettuccine Alfredo
(4, 33, 1, 18.99),  -- Spaghetti Bolognese
(4, 42, 1, 8.99),   -- Tiramisu
(4, 59, 2, 4.49);   -- 2x Cappuccino

-- Order 5: Quick bite
INSERT INTO order_items (order_id, menu_item_id, quantity, unit_price) VALUES
(5, 37, 1, 14.99),  -- Turkey Club
(5, 46, 1, 6.99),   -- Ice Cream Sundae
(5, 54, 1, 3.49);   -- Lemonade

-- Order 6: Seafood feast
INSERT INTO order_items (order_id, menu_item_id, quantity, unit_price) VALUES
(6, 7, 1, 13.99),   -- Shrimp Cocktail
(6, 15, 1, 14.99),  -- Crab Cakes
(6, 25, 1, 24.99),  -- Grilled Salmon
(6, 41, 1, 42.99),  -- Lobster Tail
(6, 53, 2, 2.99);   -- 2x Iced Tea

-- Order 7: Casual dinner
INSERT INTO order_items (order_id, menu_item_id, quantity, unit_price) VALUES
(7, 1, 1, 8.99),    -- Spring Rolls
(7, 38, 1, 17.99),  -- Fish and Chips
(7, 41, 1, 7.99),   -- Chocolate Cake
(7, 51, 1, 2.99);   -- Coca Cola

-- Order 8: Vegetarian meal
INSERT INTO order_items (order_id, menu_item_id, quantity, unit_price) VALUES
(8, 14, 1, 6.99),   -- Edamame
(8, 31, 1, 16.99),  -- Vegetable Pasta
(8, 44, 1, 16.99),  -- Vegetarian Lasagna
(8, 24, 1, 8.99);   -- Garden Salad

-- Order 9: Steak lovers
INSERT INTO order_items (order_id, menu_item_id, quantity, unit_price) VALUES
(9, 10, 1, 7.99),   -- Onion Rings
(9, 26, 2, 32.99),  -- 2x Ribeye Steak
(9, 43, 1, 34.99),  -- Lamb Chops
(9, 51, 3, 2.99);   -- 3x Coca Cola

-- Order 10: Kids meal
INSERT INTO order_items (order_id, menu_item_id, quantity, unit_price) VALUES
(10, 36, 2, 15.99), -- 2x Beef Burger
(10, 46, 2, 6.99),  -- 2x Ice Cream Sundae
(10, 51, 2, 2.99);  -- 2x Coca Cola

-- Order 11: Soup and salad
INSERT INTO order_items (order_id, menu_item_id, quantity, unit_price) VALUES
(11, 16, 1, 8.99),  -- French Onion Soup
(11, 18, 1, 9.99),  -- Clam Chowder
(11, 20, 1, 11.99), -- Greek Salad
(11, 55, 2, 2.49);  -- 2x Coffee

-- Order 12: BBQ night
INSERT INTO order_items (order_id, menu_item_id, quantity, unit_price) VALUES
(12, 8, 1, 11.99),  -- Nachos Supreme
(12, 30, 1, 26.99), -- BBQ Ribs
(12, 40, 1, 15.99), -- Pulled Pork Sandwich
(12, 53, 2, 2.99);  -- 2x Iced Tea

-- Order 13: Pasta lovers
INSERT INTO order_items (order_id, menu_item_id, quantity, unit_price) VALUES
(13, 5, 1, 8.99),   -- Mozzarella Sticks
(13, 32, 1, 17.99), -- Fettuccine Alfredo
(13, 34, 1, 22.99), -- Shrimp Scampi
(13, 48, 1, 8.99);  -- Brownie Sundae

-- Order 14: Light lunch
INSERT INTO order_items (order_id, menu_item_id, quantity, unit_price) VALUES
(14, 17, 1, 7.99),  -- Tomato Basil Soup
(14, 21, 1, 12.99), -- Caprese Salad
(14, 55, 1, 2.49);  -- Coffee

-- Order 15: Brunch
INSERT INTO order_items (order_id, menu_item_id, quantity, unit_price) VALUES
(15, 12, 1, 7.99),  -- Deviled Eggs
(15, 22, 1, 13.99), -- Cobb Salad
(15, 47, 1, 7.99),  -- Apple Pie
(15, 61, 2, 3.99);  -- 2x Orange Juice

-- Order 16: Currently preparing - Large party
INSERT INTO order_items (order_id, menu_item_id, quantity, unit_price) VALUES
(16, 4, 3, 11.99),  -- 3x Chicken Wings
(16, 28, 2, 18.99), -- 2x Chicken Parmesan
(16, 36, 2, 15.99), -- 2x Beef Burger
(16, 44, 1, 16.99), -- Vegetarian Lasagna
(16, 51, 5, 2.99);  -- 5x Coca Cola

-- Order 17: Currently preparing
INSERT INTO order_items (order_id, menu_item_id, quantity, unit_price) VALUES
(17, 3, 1, 12.99),  -- Calamari
(17, 33, 1, 18.99), -- Spaghetti Bolognese
(17, 42, 1, 8.99),  -- Tiramisu
(17, 53, 1, 2.99);  -- Iced Tea

-- Order 18: Currently preparing
INSERT INTO order_items (order_id, menu_item_id, quantity, unit_price) VALUES
(18, 15, 1, 14.99), -- Crab Cakes
(18, 41, 1, 42.99), -- Lobster Tail
(18, 25, 1, 24.99), -- Grilled Salmon
(18, 56, 1, 3.99);  -- Espresso

-- Order 19: Currently preparing
INSERT INTO order_items (order_id, menu_item_id, quantity, unit_price) VALUES
(19, 39, 1, 19.99), -- Chicken Tikka Masala
(19, 14, 1, 6.99),  -- Edamame
(19, 45, 1, 8.99);  -- Cheesecake

-- Order 20: Just placed - Pending
INSERT INTO order_items (order_id, menu_item_id, quantity, unit_price) VALUES
(20, 13, 1, 9.99),  -- Potato Skins
(20, 30, 1, 26.99), -- BBQ Ribs
(20, 51, 1, 2.99);  -- Coca Cola

-- Order 21: Just placed - Pending
INSERT INTO order_items (order_id, menu_item_id, quantity, unit_price) VALUES
(21, 19, 2, 10.99), -- 2x Caesar Salad
(21, 29, 2, 17.99); -- 2x Grilled Chicken

-- Order 22: Just placed - Pending
INSERT INTO order_items (order_id, menu_item_id, quantity, unit_price) VALUES
(22, 26, 1, 32.99), -- Ribeye Steak
(22, 10, 1, 7.99),  -- Onion Rings
(22, 44, 1, 9.99);  -- Crème Brûlée

-- Order 23: Just placed - Pending
INSERT INTO order_items (order_id, menu_item_id, quantity, unit_price) VALUES
(23, 40, 2, 15.99), -- 2x Tacos
(23, 8, 1, 11.99),  -- Nachos
(23, 54, 2, 3.49);  -- 2x Lemonade

-- Order 24: Just placed - Pending
INSERT INTO order_items (order_id, menu_item_id, quantity, unit_price) VALUES
(24, 38, 1, 17.99), -- Fish and Chips
(24, 47, 1, 7.99),  -- Apple Pie
(24, 53, 1, 2.99);  -- Iced Tea

-- Order 25: Just placed - Pending
INSERT INTO order_items (order_id, menu_item_id, quantity, unit_price) VALUES
(25, 6, 1, 10.99),  -- Stuffed Mushrooms
(25, 42, 1, 21.99), -- Pork Chops
(25, 49, 1, 8.99),  -- Fruit Tart
(25, 59, 1, 4.49);  -- Cappuccino

-- Update all order totals
UPDATE orders SET total_amount = (
    SELECT SUM(total_price)
    FROM order_items
    WHERE order_items.order_id = orders.id
);

-- Display summary statistics
SELECT '=== DATABASE SEED SUMMARY ===' as info;
SELECT 'Customers: ' || COUNT(*) as stat FROM customers
UNION ALL SELECT 'Menu Items: ' || COUNT(*) FROM menu_items
UNION ALL SELECT 'Reservations: ' || COUNT(*) FROM reservations
UNION ALL SELECT 'Orders: ' || COUNT(*) FROM orders
UNION ALL SELECT 'Order Items: ' || COUNT(*) FROM order_items;

SELECT '';
SELECT '=== MENU BREAKDOWN ===' as info;
SELECT category, COUNT(*) as item_count, 
       '$' || ROUND(AVG(price), 2) as avg_price
FROM menu_items 
GROUP BY category 
ORDER BY item_count DESC;

SELECT '';
SELECT '=== ORDER STATUS ===' as info;
SELECT status, COUNT(*) as order_count,
       '$' || ROUND(SUM(total_amount), 2) as total_revenue
FROM orders 
GROUP BY status 
ORDER BY order_count DESC;