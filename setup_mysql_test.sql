-- Create the test database if it does not already exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create the test user if it does not already exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost'
IDENTIFIED BY 'hbnb_test_pwd';

-- Give hbnb_test all privileges on hbnb_test_db only
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Give hbnb_test SELECT privilege on performance_schema only
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';