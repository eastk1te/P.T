create database book_rental;
use book_rental;


create table book (
book_ID int primary key auto_increment,
title text,
author text,
publisher text,
publishing_year text,
book_type text,
loc text,
registration_date date,
remaining_number int)
engine = InnoDB default char set = utf8;

select * from book;

create table user(
user_ID int primary key auto_increment,
name text,
grade text,
address text,
cellphone text,
email text,
late_fee int)
engine = InnoDB default char set=utf8;
select * from user;

create table rental(
rental_ID int primary key auto_increment,
user_ID int,
book_ID int,
rent_date date,
return_date date,
exten_period int,
foreign key(book_ID) references book(book_ID) on update cascade,
foreign key(user_ID) references user(user_ID) on update cascade)
engine = InnoDB default char set = utf8;
select * from rental;

select * from book;