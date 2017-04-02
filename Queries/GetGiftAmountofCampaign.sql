SELECT G.giftamount
FROM gift as G
WHERE G.packageid IN
(
	SELECT packageid
	FROM campaign AS C, package as P
	WHERE (C.campaignid = 'R15')
	  AND (C.projectid  = P.projectid)
)
