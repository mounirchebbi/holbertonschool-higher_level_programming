-- create db
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- switch to db
USE hbtn_0d_usa;

-- Create table
CREATE TABLE IF NOT EXISTS cities (
    id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
