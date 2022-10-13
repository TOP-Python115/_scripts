SELECT c.Name, cl.Language, cl.Percentage
	FROM country as c 
	JOIN countrylanguage as cl 
	  ON c.Code = cl.CountryCode
	WHERE cl.Percentage < 10
    ORDER BY cl.Percentage DESC