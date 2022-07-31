use company;
set sql_safe_updates = 0;
show tables;

select * from dept_locations;
alter table dept_locations add column phone char(15);
select * from dept_locations;

update dept_locations
set phone = 01011111111
where dnumber = 1 and dlocation = 'Houston';

update dept_locations
set phone = 01022222222
where dnumber = 4 and dlocation = 'Stafford';

update dept_locations
set phone = 01033333333
where dnumber = 5 and dlocation = 'Bellaire';

update dept_locations
set phone = 01044444444
where dnumber = 5 and dlocation = 'Houston';

update dept_locations
set phone = 01055555555
where dnumber = 5 and dlocation = 'Sugarland';

select * from dept_locations;

select * from project;
alter table project add column 금액 int;
select * from project;

update project
set 금액 = 1
where pnumber = 1 and dnum = 5;
update project
set 금액 = 2
where pnumber = 2 and dnum = 5;
update project
set 금액 = 3
where pnumber = 3 and dnum = 5;
update project
set 금액 = 4
where pnumber = 10 and dnum = 4;
update project
set 금액 = 5
where pnumber = 20 and dnum = 1;
update project
set 금액 = 6
where pnumber = 30 and dnum = 4;
select * from project;

insert into department values
('영업부',7,'333445555','1990-01-01');
insert into department values
('비서실',8,'999887777','2010-01-01');
select * from department;


insert into dept_locations values
(7,'Korea',010666666666);
insert into dept_locations values
(7,'Seoul',010777777777);
insert into dept_locations values
(7,'Busan',010888888888);
select * from dept_locations;

select * from employee;
insert into employee values
('Kim' ,'D','Yeon',326159487,'1964-04-01','Korea','M',50000,453453453,7);
insert into employee values
('Yeon' ,'D','Kim',261594873,'1964-04-02','Korea','M',56000,453453453,7);
insert into employee values
('Dong' ,'Y','Kim',159487326,'1964-04-03','Korea','M',57000,453453453,7);
select * from employee;

select * from works_on;
alter table works_on add column 일 int;
alter table works_on add column 이 int1;
alter table works_on add column 삼 int2;
alter table works_on add column 사 int4;
alter table works_on add column 오 int8;
select * from works_on;

select ssn, fname,minit,lname,bdate
from employee
where salary >= 30000;

select fname,minit,lname,ssn,bdate
from employee
where dno = 5;

select ssn,fname,minit,lname,bdate
from  employee e, department d
where d.dname = 'Research' and d.dnumber = e.dno and salary >= 30000;


select ssn, pnumber
from employee e,department d, project p
where d.dname = 'Research' and d.dnumber = e.dno and p.dnum = e.dno;

select fname,minit,lname, pname
from employee e,department d, project p
where d.dname = 'Research' and d.dnumber = e.dno and p.dnum = e.dno;

select dnumber,mgr_ssn
from department
where dname = '영업부';

select dlocation, phone
from dept_locations l, department d
where d.dname = '영업부' and d.dnumber = l.dnumber;

select e.fname,e.lname,s.fname,s.lname
from employee e, employee s
where e.ssn = s.super_ssn;

select e.fname,e.lname,s.fname,s.lname
from employee e, employee s
where e.dno != s.dno;