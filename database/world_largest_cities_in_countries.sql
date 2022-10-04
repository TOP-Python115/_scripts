select
	cn.`Name` as `Country`,
	c.`Name` as `City`,
    subq.max_city as `Population`,
    if(cn.`Capital` = c.`ID`, 'True', 'False') 
		as `Is capital`
  from city as c
  join (select 
			`CountryCode`,
			max(`Population`) as max_city
		  from city
		 group by `CountryCode`) as subq
	on c.`Population` = subq.max_city 
    and c.`CountryCode` = subq.`CountryCode`
  join country as cn
    on cn.`Code` = c.`CountryCode`