
drop schema if exists `m1_caso_practico`;
create schema `m1_caso_practico`;
use `m1_caso_practico`;

create table autores (
	id_autor int primary key auto_increment,
    nombre varchar(50),
    apellidos varchar(100),
    fecha_nacimiento date
    );
    
create table libros (
	id_libro int primary key auto_increment,
	titulo varchar (250),
	editorial varchar (100),
    category varchar (50),
    precio decimal (3, 2),
    id_autor int,
    foreign key (id_autor) references autores (id_autor)
);

create table usuarios (
	id_usuario int primary key auto_increment,
    nif varchar (9),
    email varchar (50) unique,
    fecha_alta date,
    codigo_postal varchar(5),
    unique key `usuarios_nif_unique` (`nif`)
);

create table prestamos (
	id_prestamo int primary key auto_increment,
    id_libro int,
    id_usuario int,
    fecha_inicio date,
    fecha_fin date,
    recargo decimal(2, 2) default 0.0,
    foreign key (id_libro) references libros(id_libro),
    foreign key (id_usuario) references usuarios(id_usuario)
); 

select * from autores;
select * from libros;
select * from usuario;
select * from prestamos;

    







