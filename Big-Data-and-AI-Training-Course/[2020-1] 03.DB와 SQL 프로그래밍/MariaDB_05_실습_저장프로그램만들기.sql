use company;
show tables;


select * from department;
select * from employee;

drop procedure if exists avgSalary;
delimiter $$
create procedure avgSalary(in dn varchar(15) char set 'utf8' collate 'utf8_bin', out avg_sal int)
begin 
    select avg(salary) into avg_sal from employee e, department d where e.dno = d.dnumber and dn = d.dname;
end $$
delimiter ;

call avgSalary('Research', @ds);
select @ds as 'avgSalary';
call avgSalary('영업부', @dz);
select @dz as 'avgSalary';
call avgSalary('Headquarters', @de);
select @de as 'avgSalary';

drop function if exists avgSalary;
delimiter $$
create function avgSalary(dn varchar(15))
	returns varchar(15) char set 'utf8' collate 'utf8_bin'
begin 
	declare rn int;
    select avg(salary) into rn from employee e, department d where e.dno = d.dnumber and dn = d.dname;
    return rn;
end $$
delimiter ;

select avgSalary('Research') as avg_Salary;
select avgSalary('영업부') as avg_Salary;
select avgSalary('Headquarters') as avg_Salary;
