CREATE DATABASE IF NOT EXISTS nethbo;

USE nethbo;

CREATE TABLE IF NOT EXISTS clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    correo VARCHAR(100) UNIQUE,
    edad INT
);