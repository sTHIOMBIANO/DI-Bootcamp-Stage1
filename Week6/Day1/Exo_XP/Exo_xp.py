#exercice1


CREATE DATABASE "Public"
with 
OWNER=postgres 
ENCODING='utf-8' 
LC_COLLATE='French_Burkina Faso.1252' 
LC_CTYPE='French_Burkina Faso.1252' 
TABLESPACE=pg_default 
CONNECTION LIMIT=-1 


CREATE TABLE items(
     id serial primary key,
    name varchar(100),
    prix numeric
)


CREATE TABLE customers(
    id serial prymary key,
    last_name varchar(100),
   first_name varchar(100)
)


insert into items(name,prix) values
('Petit bureau',100),
('Grand bureau',300),
('Ventilateur',80);

insert into customers(last_name,first_name) values
('Greg','Jones'),
('Sandra' ,'Jones'),
('Scott','Scott'),
('Trevor','Green'),
('Melanie','Johnson');


select * from items;

select * from items where prix>80;

select * from items where prix<300;


select * from customers where last_name='Smith';
"aucun resultat car ce nom n'a pas été enregistré"

select * from customers where first_name='Jones';

select * from customers where last_name!='Scott';




