use company;
show tables;

select * from employee;
select fname, lname, bdate from employee where address like '%Houston%';

select fname, lname, bdate
from employee
where bdate like '19__-01-__';

select distinct salary
from employee;

select fname, lname, bdate
from employee
where dno in ( select dnumber
			   from department
               where dname = 'Research');

select fname, lname, bdate
from employee as e
where exists ( select dnumber
			   from department as d
			   where e.dno = d.dnumber and dname = 'Research');


select fname, lname, bdate
from employee
where ssn not in (select essn from dependent);

select fname, lname, bdate
from employee as e
where not exists (select * from dependent as d where e.ssn = d.essn);

select e.fname, e.lname, d.dependent_name
from employee as e inner join dependent as d on e.ssn = d.essn;

select e.fname, e.lname, d.dependent_name
from employee as e left outer join dependent as d on e.ssn = d.essn;

select dno, count(*), avg(salary)
from employee
group by dno;

select dno, count(*), avg(salary)
from employee
group by dno
having count(*) >= 2;

create view works_info1 
as (select fname, lname, pname, dname, hours 
    from employee, department, project, works_on where ssn=essn and dnumber=dnum
    and pnumber=pno);

select fname, lname, pname, hours from works_info1;

select pname, count(*), sum(hours)
from works_info1
group by pname;

select * from dependent;
select * from employee;
select * from department;
select * from works_on;