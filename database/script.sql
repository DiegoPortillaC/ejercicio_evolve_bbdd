-- Script de creacion de la bbdd a utilizar, creando las tablas necesarias 
-- con sus correspondientes insert


PRAGMA foreign_keys = ON;


CREATE TABLE usuario (
    usuario_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL CHECK (length(nombre) <= 30),
    apellidos TEXT NOT NULL CHECK (length(apellidos) <= 40),
    email TEXT NOT NULL UNIQUE CHECK (length(email) <= 50),
    telefono TEXT NOT NULL CHECK (length(telefono) <= 12),
    direccion TEXT NOT NULL CHECK (length(direccion) <= 50),
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE factura (
    numero_factura INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER NOT NULL,
    fecha_emision DATETIME DEFAULT CURRENT_TIMESTAMP,
    descripcion TEXT CHECK (length(descripcion) <= 200),
    monto_total REAL NOT NULL,
    estado TEXT NOT NULL CHECK (estado IN ('Pendiente', 'Pagada', 'Cancelada')) DEFAULT 'Pendiente',
    FOREIGN KEY (usuario_id) REFERENCES usuario(usuario_id) ON DELETE CASCADE
);


INSERT INTO usuario (nombre, apellidos, email, telefono, direccion) VALUES
('Ana', 'González Pérez', 'ana.gonzalez@example.com', '612345678', 'Calle Sol 12, Madrid'),
('Luis', 'Martínez Ruiz', 'luis.martinez@example.com', '622334455', 'Av. Libertad 45, Barcelona'),
('María', 'López Gómez', 'maria.lopez@example.com', '611000111', 'Calle Olivo 9, Valencia'),
('Carlos', 'Sánchez Díaz', 'carlos.sanchez@example.com', '699112233', 'Calle Mayor 3, Valencia'),
('Laura', 'Ramírez Torres', 'laura.ramirez@example.com', '633445566', 'Calle Luna 7, Sevilla'),
('David', 'Fernández Soto', 'david.fernandez@example.com', '611223344', 'Calle Norte 21, Madrid'),
('Sara', 'Jiménez Navarro', 'sara.jimenez@example.com', '633556677', 'Calle del Río 8, Málaga'),
('Jorge', 'Moreno Vargas', 'jorge.moreno@example.com', '644332211', 'Calle Sur 14, Murcia'),
('Lucía', 'Castillo Romero', 'lucia.castillo@example.com', '644778899', 'Camino Real 22, Zaragoza'),
('Andrés', 'Ortega Paredes', 'andres.ortega@example.com', '655667788', 'Paseo del Prado 1, Bilbao');


INSERT INTO factura (usuario_id, descripcion, monto_total, estado) VALUES
(1, 'Servicio de consultoría mensual', 300.00, 'Pagada'),
(2, 'Venta de producto X', 120.50, 'Pendiente'),
(3, 'Mantenimiento técnico anual', 450.00, 'Pagada'),
(4, 'Servicio de suscripción premium', 89.99, 'Pendiente'),
(5, 'Venta de paquete promocional', 199.90, 'Cancelada'),
(6, 'Diseño de sitio web', 750.00, 'Pagada'),
(7, 'Actualización de software', 320.00, 'Pagada'),
(8, 'Servicio de soporte 24/7', 150.00, 'Pendiente'),
(9, 'Auditoría de seguridad', 500.00, 'Cancelada'),
(10, 'Formación en línea', 100.00, 'Pagada');
