-- 14-model_city_fetch_by_state.sql

CREATE DATABASE IF NOT EXISTS hbtn_0e_14_usa;
USE hbtn_0e_14_usa;

CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    state_id INT,
    FOREIGN KEY (state_id) REFERENCES states(id)
);

-- Insert sample data
INSERT INTO states (name) VALUES ('California'), ('Nevada'), ('Texas');
INSERT INTO cities (name, state_id) VALUES ('Los Angeles', 1), ('San Francisco', 1), ('Las Vegas', 2), ('Houston', 3);
