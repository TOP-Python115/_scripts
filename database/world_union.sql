	select `Name`
	  from country
	 where `Name` like 'C%'
union all
	select `Name`
	  from country
	 where IndepYear < 1700
order by `Name`
limit 15
