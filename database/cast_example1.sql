select 
	Name, 
    concat(IndepYear, "-01-01"),
    cast(concat(IndepYear, "-01-01") as datetime)
  from country