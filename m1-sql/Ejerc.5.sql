alter table sakila.customer_film_favorites
    add column last_update timestamp default current_timestamp on update current_timestamp;
    
    select * from sakila.customer_film_favorites;