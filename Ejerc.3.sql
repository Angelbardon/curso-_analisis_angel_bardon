

CREATE TABLE IF NOT exists sakila.customer_film_favorites(
	film_id smallint unsigned not null,
    customer_id smallint unsigned not null,
    position int not null,
    creation_datetime datetime default current_timestamp,
    primary key (film_id, customer_id),
    constraint `fk_favorite_film` foreign key (`film_id`) references `sakila`.`film` (`film_id`),
    constraint `fk_favorite_customer` foreign key (`customer_id`) references `sakila`.`customer` (`customer_id`)
    );
    
    select * from sakila.customer_film_favorites;
    
    