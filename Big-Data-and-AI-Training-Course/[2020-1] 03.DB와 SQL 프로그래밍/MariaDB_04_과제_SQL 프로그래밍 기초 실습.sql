use university;
set @a = 100;
set @b = 200;
set @c = @a + @b;
set @d = @b - @a;
select @a,@b,@c,@d;

delimiter $$
create procedure add_sum ( )
begin
    declare a int;
    declare b int;
    declare c int;
    set a = 500;
    set b = 300;
    set c = a + b;
    select a, b, c;
end $$
delimiter ; # 공백 필요 기호가 delimiter 라는 것을 지정하기 위해

call add_sum();

delimiter $$
create procedure scroe()
begin
  declare d int;
  set d = 86;
  if d >= 90 then select 'A 입니다.';
  elseif d >= 80 then select 'B 입니다.';
  elseif d >= 70 then select 'C 입니다.';
  else select 'F 입니다.';
  end if;
end $$
delimiter ;

call scroe;

delimiter $$
create procedure rep()
begin
  declare i int;
  declare hap int;
  set i = 0; set hap = 0;
#  myLoop: LOOP
  while ( i <= 100) do
#    if i > 100 then leave myLoop;
#    end if;
    set hap = hap + i;
    set i = i + 1;
    end while;
#  end loop myLoop;
  select hap;
end $$
delimiter ;

call rep;

drop procedure rep;
drop procedure score;
drop procedure add_sum;