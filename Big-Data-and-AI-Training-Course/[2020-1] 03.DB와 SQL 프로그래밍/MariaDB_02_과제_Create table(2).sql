use company;
show tables;
select bdate, address from employee
where fname = 'Jphn' and minit = 'B' and lname = 'Smith';
select fname, lname, dname from employee, department
where dname = 'Research' and dnumber = dno;

select pnumber, dnum, lname, address, bdate 
from project as p , departmentas d, employee e
where p.plocation = 'Stafford' and p.dnum = d.dnumber and d.mgr_ssn = e.ssn;

select e.fname, e.lname, s.fname, s.lname
from employee e, employee s
where e.super_ssn = s.ssn;

select * from employee, department;