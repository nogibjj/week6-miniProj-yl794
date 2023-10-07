WITH USA_Tracks_Sold AS 
(
    SELECT il.* FROM InvoiceLine il
    JOIN Invoice i on il.InvoiceId = i.InvoiceId
    JOIN Customer c on i.CustomerId = c.CustomerId
    WHERE c.Country = 'USA'
)

SELECT
    g.Name as Genre,
    COUNT(uts.InvoiceLineId) as Tracks_Sold
FROM USA_Tracks_Sold uts
JOIN Track t on uts.TrackId = t.TrackId
JOIN Genre g on t.GenreId = g.GenreId
GROUP BY 1
ORDER BY 2 DESC
LIMIT 3;