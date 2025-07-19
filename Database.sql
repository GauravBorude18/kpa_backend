##This code is for how to create a Mysql code
CREATE DATABASE kpa_backend;
USE kpa_backend;

CREATE TABLE form_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    phone VARCHAR(20)
);
