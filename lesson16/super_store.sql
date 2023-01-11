

--1
select * from superstore_data;
--2
select count(*) from superstore_data;
--3
select * from superstore_data limit 10;
--4
select * from superstore_data limit 25 offset 20 ;
--5
select id,year_birth ,marital_status  from superstore_data limit 20 offset 1;
--6
select id from superstore_data
where mntwines>1000;
--7
select year_birth ,marital_status  from superstore_data
where mntfishproducts <500 and mntmeatproducts >500;
--8
select count( response)  from superstore_data
where response =1;
--9
select education  from superstore_data
order by education ;
--10
select * from superstore_data
where year_birth =
(select  min(year_birth)  from superstore_data );
--11
select  id,year_birth ,marital_status  from superstore_data
where dt_customer =
(select min(dt_customer) from superstore_data );
--12
select avg(income) from superstore_data
where complain =1;
--13
select sum (kidhome+teenhome) as total_value from superstore_data;
--14
select id ,income , year_birth, marital_status  from superstore_data sd
where numwebpurchases >numstorepurchases ;
--15
select sum (kidhome+teenhome) as total_value from superstore_data
where recency <31;
--16
select count(id)  from superstore_data sd
where mntfishproducts =0 or mntmeatproducts =0;
--17
select * from superstore_data sd
where mntgoldprods =
(select max(mntgoldprods) from superstore_data);
--18
select id ,year_birth  from superstore_data
where year_birth <2003 and year_birth >1983
order by year_birth ;
--19
select distinct(year_birth) from superstore_data;
--20
select * from superstore_data
order BYmntsweetproducts desc
limit 10;
--21
select marital_status ,count(marital_status) as sum_status
from superstore_data
group by marital_status;
--22
select education
,sum(mntwines) as sum_wine_and_sweet
,sum(mntsweetproducts) as sum_swet,
 sum(mntsweetproducts + mntwines ) as total
from superstore_data
group by education;
--23
select education , marital_status ,
 min(date_part ('year',(select current_timestamp))-year_birth) as min_age
,max(date_part ('year',(select current_timestamp))-year_birth) as max_age
from superstore_data sd
group by education ,marital_status
order by education ,
min(date_part('year', (SELECT current_timestamp)) - year_birth);
--24
select response, complain ,
date_part('year', (SELECT current_timestamp)) - year_birth as age
from superstore_data sd
where response =1 and complain =0;
--25
select distinct on (education) education , id ,
min(date_part ('year',(select current_timestamp))-year_birth) as min_age
from superstore_data sd
group by education ,id
order by education ,
min(date_part ('year',(select current_timestamp))-year_birth);
--26
select avg(mntmeatproducts) as avg_meats
      ,avg( mntsweetproducts) as avg_sweets
      ,avg(mntwines) as avg_wines
      ,avg(mntfishproducts) as avg_fishs
      ,avg(mntgoldprods) as avg_golds
      ,kidhome+teenhome as sum_kides
from superstore_data
group by
      kidhome+teenhome;
--27
select distinct on (teenhome) teenhome id ,year_birth
from superstore_data sd
group by id ,year_birth ,teenhome
order by teenhome ,min(date_part ('year',(select current_timestamp))-year_birth);
--28
select
	count(sd.response) filter (where  response = 1) as accepted,
	count(sd.response) filter  (where  response = 0) as not_accepted
from
	superstore_data sd;
--29
select marital_status,
avg(kidhome) as kids_avg,
avg(teenhome) as teens_avg_
from superstore_data sd
group by marital_status ;
--30
select education ,
 max(income) as income_max,
 avg(income) as income_avg,
 min(income) as income_min
 from superstore_data sd
 group by education
