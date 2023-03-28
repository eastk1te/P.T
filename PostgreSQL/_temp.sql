
select s.column, count(*)
from column s
where s.column = '' and s.column ::date = '2022-12-12'
group by s.entity_id;


CREATE TABLE (
uuid,
    NUMERIC,
    varchar(500),
    timestamp default now(),
    geometry(POINT, 4326),
		NUMERIC,
				json,
    s	bigserial
);


SELECT * FROM pg_catalog.pg_stat_activity;
select oid, datname from pg_catalog.pg_database;
select * from pg_catalog.pg_stats;

SELECT @@profiling;


---

ALTER TABLE table DROP CONSTRAINT table_pkey;


alter table name add column uuid;
commit



update table set column_date = '2022-08-17 14:08:00+09' where column_date > '2022-08-19'; 
commit


	
select * from table where bssh_nm LIKE '%aa%' and instt_nm = '';


if exists ()


if LCNS_NO is in () then
	참
else
	거짓
end if;


/* */

INSERT INTO table(column)
    SELECT column
    FROM (select * from tablenr where column is null and column is null order by "sequence") as t
    WHERE NOT EXISTS (
   		select column
   		from table nr 
   		where column is null
   		order by "column");
  

SELECT *
  case 
    WHEN LCNS_NO field1>0 THEN field2/field1
    ELSE 0
  END 
  AS field3
FROM 

delete from table where column_date > '2022-08-25';


update tableA AS a 
set column = b.column 
from tableB AS b 
where a.column = b.column


IF (select count(*) from pg_tables where schemaname='public' and tablename='') = 0 then
	select count(*) from pg_tables
END IF;

create table
uuid not null default uuid_generate_v4(),

(select to_char(max(nr2.column), 'YYYY-MM-DD') 
                                    from table nr2 ::timestamp;



WITH UPSERT AS (
    UPDATE table nr
    SET column = (select id from column where id = nr.column) 
    RETURNING *
);

INSERT INTO talbe(column)
	SELECT column
	from 
	on conflict 
	do update set column = id;

/*postgresql ::text type 변환.*/
delete from table r where r.column::text not in (select distinct concat(rt.column, rv.column) from column rt, column rv);


-- 중복 삭제, 원래 중복이 있어야하는데 삭제를 잘못함. 일자별로 업데이트 로그가 찍혀야 정상인데 그걸 삭제해버림.
DELETE  FROM
    talbe a
        USING talbe b
WHERE
    a.column < b.column    AND a.column= b.column;

select nr.column, nr.column, nr.column, if(nr.columnis null, true, false) from table nr



IF EXISTS(SELECT * FROM MyTable WHERE...)
 --value exists perform update
  BEGIN
    UPDATE...
  END
ELSE
  --value doesnt exist perform insert
  BEGIN
    INSERT ...
  end


select st_astext(rs."l")  
select ST_AsText(rs.) as lon, st_y(rs.) as lat