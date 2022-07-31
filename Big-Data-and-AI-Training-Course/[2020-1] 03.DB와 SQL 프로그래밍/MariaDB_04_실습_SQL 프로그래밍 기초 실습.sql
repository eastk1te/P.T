use university;
show tables;

set @a = 500; 
set @b =300; 
set @c = @a - @b;
select @a, @b, @c;

drop procedure if exists minus_proc;
delimiter $$
create procedure minus_proc ( )
begin
    declare x int;  declare y int; declare z int;
    set x = 50; set y = 35; set z = x - y; 
    select x, y, z; 
end $$
delimiter ;

call minus_proc;
call minus_proc;

select @a, @b, @c;
select x, y, z;
select @x, @y, @z;

drop procedure if exists minus_proc2;
delimiter $$
create procedure minus_proc2 (IN s int, IN t int)
begin
    declare u int;  
    set u = s - t;  
    select s, t, u; 
end $$
delimiter ;

call minus_proc2(200, 150);
call minus_proc2(5000, 2550);
call minus_proc2(30, 10);

call minus_proc;
call minus_proc;

###########################################################
drop procedure if exists oper_proc;
delimiter $$
create procedure oper_proc (IN s int, IN op char, IN t int)
begin
      declare u int;  
      case
	when op = '+' then set u = s + t;
	when op = '-' then set u = s - t;
	when op = '*' then set u = s * t;
	when op = '/' then set u = s / t;
	else set u = -10000;
     end case;
     select s, op, t, '=', u;
end $$
delimiter ;

call oper_proc (100, '+', 50);
call oper_proc (250, '-', 120);
call oper_proc (10, '*', 5);
call oper_proc (400, '/', 80);  

call oper_proc (100, '/', 10);
call oper_proc (10, '*', 10);
call oper_proc (10, '*', 10);
call minus_proc2(10, 2);
call minus_proc2(10, 5);




