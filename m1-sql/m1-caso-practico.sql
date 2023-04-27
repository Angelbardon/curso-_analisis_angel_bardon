
DROP schema IF exists`m1_caso_practico`;
create schema `m1_caso_practico`;
use `m1_caso_practico`;

create table clientes(
id_cliente int primary key auto_increment,
nombre varchar(50),
apellido varchar(100),
email varchar(50) unique,
telefono int(9)unique,
direccion varchar(50)
);

create table productos(
id_producto int primary key auto_increment,
nombre varchar(50),
descripcion varchar(100),
precio decimal(9, 2),
stock int(100)
);

create table pedidos(
id_pedido int primary key auto_increment,
id_cliente int,
fecha date,
foreign key (id_cliente) references clientes(id_cliente)
);

create table detalle_pedidos(
id_detalle_pedido int primary key auto_increment,
id_pedido int,
id_cliente int,
id_producto int,
cantidad int,
fecha timestamp default current_timestamp ,
foreign key (id_cliente) references clientes(id_cliente),
foreign key (id_producto) references productos(id_producto)
);


select * from clientes;
select * from productos;
select * from pedidos;
select * from detalle_pedidos;

insert into clientes (nombre, apellido, email, telefono, direccion) values
('Pablo', 'Garcia', 'pablo,@gmail.com', 666555777, 'calle mercurio'),
('Carmen', 'Cuevas', 'c.cuevas@gmail.com', 777444333, 'calle tierra'),
('Rocio', 'Fernandez', 'rociofer@gmail.com', 999876678, 'calle venus'),
('Luis', 'Martinez', 'luis@gmail.com', 111555254, 'calle marte'),
('Alberto', 'Casas', 'alberto@gmail.com', 654456654, 'calle jupiter'),
('Pilar', 'Puentes', 'pilar@hotmail.com', 999999888, 'calle venus')
;


insert into productos (nombre, descripcion, precio, stock) values
('HP', 'ordenador sobremesa', 1200, 5),
('Dell', 'ordenador sobremesa', 1325, 9),
('HP', 'ordenador portalil', 890, 12),
('Lenovo', 'ordenador portatil', 750, 7),
('Dell', 'ordenador portatil', 650.90, 12),
('Samsung', 'pantalla 20"', 200, 15),
('HP', 'pantalla 20"', 170, 20),
('HP', 'teclado inalambrico', 125.50, 25),
('HP', 'raton inalambrico', 90, 35),
('Dell', 'teclado de portatil', 200, 12),
('HP', 'impresora color', 229.50, 7), 
('HP', 'impresora laser', 437, 3)
;


insert into pedidos(id_pedido, id_cliente, fecha) values
(3, 1, '2023-01-10'),
(6, 1, '2023-01-10'),
(2, 5, '2023-01-25'),
(1, 3, '2023-01-26'),
(10, 1, '2023-02-02'),
(5, 2, '2023-02-03'),
(7, 2, '2023-02-03')
;


insert into detalle_pedidos(id_detalle_pedido, id_pedido, id_producto, cantidad, fecha) values
(1, 3, 1, 3, '2023-01-10'),
(2, 3, 6, 1, '2023-01-10'),
(3, 2, 2, 5, '2023-01-25'),
(4, 3, 1, 3, '2023-01-26'),
(5, 1, 10, 1, '2023-02-02'),
(6, 2, 5, 2, '2023-02-03'),
(7, 3, 7, 2, '2023-02-03')
;

select * from clientes;
select * from productos;
select * from pedidos;
select * from detalle_pedidos;

select apellido from clientes order by apellido;

select  nombre, descripcion , stock from productos where stock < 10;


select count(*) from pedidos;
select  count(*)  from pedidos group by id_cliente = 3;

 # mostrar total de ventas (precio * cantidad) por cada pedido

 
























