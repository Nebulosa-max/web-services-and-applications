show databases;

create database wsaa;

use wsaa;

create table student (
    id int NOT NULL auto_increment,
    firstname varchar(100),
    age int(3),
    PRIMARY KEY (id)
);

insert into student (firstname, age) values ('joe',56);

select * from student;

update student set firstname='mary' where id = 1;

delete from student where id = 1;

create table book (
    id int NOT NULL auto_increment,
    title varchar(200),
    author varchar(100),
    price float,
    PRIMARY KEY (id)
);

insert into book (title, author, price) 
values ('Python Basics', 'John Doe', 29.99);