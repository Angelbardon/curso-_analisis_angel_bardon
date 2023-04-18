
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
    precio decimal (12, 2),
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
    recargo decimal(12, 2) default 0.0,
    foreign key (id_libro) references libros(id_libro),
    foreign key (id_usuario) references usuarios(id_usuario)
); 

select * from autores;
select * from libros;
select * from usuarios;
select * from prestamos;

INSERT INTO `m1_caso_practico`.`autores` (`nombre`, `apellidos`, `fecha_nacimiento`) VALUES ('francisco', 'mora', '1952-07-28');
INSERT INTO `m1_caso_practico`.`autores` (`nombre`, `apellidos`, `fecha_nacimiento`) VALUES ('angel', 'limon', '1942-09-12');
INSERT INTO `m1_caso_practico`.`autores` (`nombre`, `apellidos`, `fecha_nacimiento`) VALUES ('pablo', 'garcia', '1969-05-15');
INSERT INTO `m1_caso_practico`.`autores` (`nombre`, `apellidos`, `fecha_nacimiento`) VALUES ('maria', 'olmo', '1999-07-01');
INSERT INTO `m1_caso_practico`.`autores` (`nombre`, `apellidos`, `fecha_nacimiento`) VALUES ('dolores', 'casas', '2000-12-12');

INSERT INTO `m1_caso_practico`.`libros` (`titulo`, `editorial`, `category`, `precio`, `id_autor`) VALUES ('pesadilla', 'planeta', 'novela', '19.20', '2');
INSERT INTO `m1_caso_practico`.`libros` (`titulo`, `editorial`, `category`, `precio`, `id_autor`) VALUES ('paraiso', 'everest', 'novela', '18.00', '1');
INSERT INTO `m1_caso_practico`.`libros` (`titulo`, `editorial`, `category`, `precio`, `id_autor`) VALUES ('ingles facil', 'planeta', 'texto', '9.00', '5');
INSERT INTO `m1_caso_practico`.`libros` (`titulo`, `editorial`, `category`, `precio`, `id_autor`) VALUES ('el futuro es hoy', 'santillana', 'teatro', '25.75', '2');

INSERT INTO `m1_caso_practico`.`usuarios` (`nif`, `email`, `fecha_alta`, `codigo_postal`) VALUES ('78276421s', 'maria@gmail.com', '202-05-14', '28000');
INSERT INTO `m1_caso_practico`.`usuarios` (`nif`, `email`, `fecha_alta`, `codigo_postal`) VALUES ('55667665a', 'felipe@hot.com', '2023-01-02', '28002');
INSERT INTO `m1_caso_practico`.`usuarios` (`nif`, `email`, `fecha_alta`, `codigo_postal`) VALUES ('76887231c', 'teresa@gmail.com', '2019-05-02', '28002');
INSERT INTO `m1_caso_practico`.`usuarios` (`nif`, `email`, `fecha_alta`, `codigo_postal`) VALUES ('36227889h', 'sofia@gmail.com', '2020-02-02', '28002');

INSERT INTO `m1_caso_practico`.`prestamos` (`id_libro`, `id_usuario`, `fecha_inicio`, `fecha_fin`, `recargo`) VALUES ('3', '1', '2023-03-10', '2023-04-15', '2.50');
INSERT INTO `m1_caso_practico`.`prestamos` (`id_libro`, `id_usuario`, `fecha_inicio`, `fecha_fin`, `recargo`) VALUES ('2', '3', '2023-04-01', '2023-04-10', '0.00');
INSERT INTO `m1_caso_practico`.`prestamos` (`id_libro`, `id_usuario`, `fecha_inicio`, `fecha_fin`, `recargo`) VALUES ('2', '4', '2023-04-07', '2023-04-17', '0.00');
