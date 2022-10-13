select
	cn.`Name` as `Country`,
    c.`Name` as `Capital`,
    round(c.`Population` / cn.`Population` * 100, 1) 
		as `Percent of people in capital`
  from country as cn
  join city as c
    on c.`ID` = cn.`Capital`