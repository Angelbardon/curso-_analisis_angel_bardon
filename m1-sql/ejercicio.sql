CREATE TABLE `employees` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first name` varchar(100) DEFAULT NULL,
  `nif` varchar(45) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `briht day` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nif_UNIQUE` (`nif`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3

SELECT * FROM curso_analisis.employees;