CREATE DATABASE fdtools;

USE fdtools;

CREATE TABLE logs (
`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
date date not null,
time time not null,
decall varchar(15) not null,
dxcall varchar(15) not null,
band varchar(5) not null,
freq varchar(10) not null,
txrst varchar(10) not null,
rxrst varchar(10) not null,
mode varchar(5) not null,
other varchar(255) null
)ENGINE=InnoDB;

