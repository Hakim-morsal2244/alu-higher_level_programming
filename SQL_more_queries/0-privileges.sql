-- Task: List all privileges for user_0d_1 and user_0d_2 on localhost

-- Create the users if they don't exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';

-- Grant necessary privileges
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
GRANT SELECT, INSERT ON *.* TO 'user_0d_2'@'localhost';

-- Display privileges
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
