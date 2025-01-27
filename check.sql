use Demo
go

--sp_help jokes

--truncate table dbo.jokes
select *
from dbo.jokes with(nolock)
where jokeid = 189

select jokeid, count(0)
from jokes
group by jokeid
having count(0) > 1