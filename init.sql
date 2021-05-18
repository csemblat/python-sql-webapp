CREATE database IF NOT EXISTS projets_immobiliers;
CREATE USER 'testuser'@'localhost' IDENTIFIED BY 'password';
GRANT ALL ON projets_immobiliers.* TO 'testuser'@'localhost';

USE projets_immobiliers;

create table adresse (adresse_id int not null unique auto_increment primary key, numero int, rue varchar(20));

create table parcelle (parcelle_id int not null unique auto_increment primary key, adresse_id int, codepostal int, ville varchar(20), surface float);

create table projet (projet_id int not null unique auto_increment primary key, parcelle_id int, ca float, creation_date datetime, status varchar(20));

insert into adresse values (1,30, 'Rue de Paris');
insert into adresse values (2,28, 'Rue de Paris');
insert into adresse values (3,10, 'Rue de Rosny');

insert into parcelle values (1, 1, 93100, 'Montreuil' , 452);
insert into parcelle values (2, 2, 93100, 'Montreuil' , 100);
insert into parcelle values (3, 3, 93100, 'Montreuil' , 50);

insert into projet values (1, 1, 2000000, '2020-03-04 10:50:10', 'terminé');
insert into projet values (2, 2, 1000000, '2021-12-05 09:10:10', 'terminé');
insert into projet values (3, 3, 400000, '2019-01-10 20:05:00', 'en cours');
insert into projet values (4, 3, 100000, '2021-10-01 23:55:59', 'abandonné');

