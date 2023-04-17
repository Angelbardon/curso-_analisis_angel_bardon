 -- inserrtar actor
     -- Insertar un nuevo actor en la tabla "actor"
     
     select * from sakila.film;
     select * from sakila.language;
     INSERT INTO sakila.film (`title`, `release_year`, `language_id`) 
     VALUES ('pelicula inventada', 2010, 4);