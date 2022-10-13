select 
	CountryCode,
    count(*) as `Cities`
  from city
 group by CountryCode