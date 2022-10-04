select 
	Continent,
    Region,
    avg(LifeExpectancy) as `Average Life`
  from country
 group by Continent, Region
 order by Continent