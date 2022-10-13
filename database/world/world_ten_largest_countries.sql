USE world;
SELECT `Code`, `Name`, `SurfaceArea`, `LocalName`
	FROM country
    WHERE `Code` != "ATA"
    ORDER BY `SurfaceArea` DESC
    LIMIT 10;