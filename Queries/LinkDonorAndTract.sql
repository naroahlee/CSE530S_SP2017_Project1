SELECT COUNT(*)
FROM
	(
	SELECT D.firstname, D.lastname, D.donorid, T.tractcode
	FROM donor AS D, donor_tract AS T
	WHERE D.donorid = T.donorid
	) AS TAB1
