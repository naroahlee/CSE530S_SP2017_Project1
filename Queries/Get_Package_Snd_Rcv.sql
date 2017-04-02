SELECT TAB1.packageid, TAB1.SndMailAmt, TAB2.RcvGiftAmt
FROM
	(
		SELECT S3.packageid, COUNT(donorid) AS SndMailAmt
		FROM sendmail AS S3
		WHERE S3.packageid IN
		(
			SELECT packageid
			FROM campaign AS C, package as P
			WHERE (C.campaignid = 'R15')
			  AND (C.projectid  = P.projectid)
		)
		GROUP BY S3.packageid 
		ORDER BY S3.packageid
	) AS TAB1,
	(
		SELECT S2.packageid, COUNT(donorid) AS RcvGiftAmt
		FROM sendmail AS S2
		WHERE S2.donorid IN
			(
				(
					SELECT S.donorid
					FROM sendmail AS S
					WHERE S.packageid IN
					(
						SELECT packageid
						FROM campaign AS C, package as P
						WHERE (C.campaignid = 'R15')
						  AND (C.projectid  = P.projectid)
					)
				)
				INTERSECT
				(
					SELECT G.donorid
					FROM gift AS G
					WHERE G.packageid IN
					(
						SELECT packageid
						FROM campaign AS C2, package as P2
						WHERE (C2.campaignid = 'R15')
						  AND (C2.projectid  = P2.projectid)
					)
				)
			)
		GROUP BY S2.packageid
	) AS TAB2
WHERE TAB1.packageid = TAB2.packageid
ORDER BY TAB1.packageid
