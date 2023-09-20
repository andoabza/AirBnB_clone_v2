-- create database hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- cretae user hbnb_dev (in localhost) with password hbnb_dev_pwd
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- hbnb_dev has all privileges on only hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- hbnb_dev has SELECT privilege on the database performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
-- If hbnb_dev_db or user hbnb_dev already exists, script does not fail