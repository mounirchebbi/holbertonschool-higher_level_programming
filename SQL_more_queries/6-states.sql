-- create db 
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

--create table
CREATE TABLE IF NOT EXISTS states (
    id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256)
    );
