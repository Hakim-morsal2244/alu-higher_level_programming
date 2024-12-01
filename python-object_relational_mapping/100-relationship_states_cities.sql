-- Create the database hbtn_0e_100_usa if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0e_100_usa;
USE hbtn_0e_100_usa;

-- Create the states table
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(128) NOT NULL
);

-- Create the cities table
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(128) NOT NULL,
    state_id INT NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id) ON DELETE CASCADE
);
