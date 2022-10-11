create database if not exists academy;
use academy;

create table if not exists Curators (
	`id` mediumint unsigned not null auto_increment,
    `Name` varchar(30) not null,
    `Surname` varchar(30) not null,
    constraint PK_id primary key(`id`)
);


