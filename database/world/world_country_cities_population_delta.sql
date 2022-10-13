select 
	cn.`Name`,
    format(cn.`Population`, 0) as `Total population`,
    format(sum(c.`Population`), 0) as `Population in cities`,
    cn.`Population` - sum(c.`Population`) as `delta`
  from country as cn
  join city as c
    on c.`CountryCode` = cn.`Code`
 where cn.`Population` > 1000000
 group by cn.`Name`, cn.`Population`
having cn.`Population` - sum(c.`Population`) > 0
 order by `delta`