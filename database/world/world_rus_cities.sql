SELECT `CountryCode`, `Name`, `Population`
	FROM world.city
    WHERE CountryCode = "RUS"
    ORDER BY Population DESC