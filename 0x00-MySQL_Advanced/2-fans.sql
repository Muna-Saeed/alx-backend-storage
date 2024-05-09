-- Import the provided table dump file (metal_bands.sql.zip) into your database.
-- This file contains the necessary data for the bands.
-- Rank country origins of bands by number of fans
-- Ordered by the number of (non-unique) fans
-- Column must be origin and nb_fans
-- Script can be executed on any database

SELECT origin, SUM(fans) as nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
