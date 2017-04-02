SELECT firstname,lastname,donorid
FROM donor
WHERE donorid in
(
	SELECT donorid
	FROM gift
	WHERE giftamount>100 AND packageid IN 
	(
		SELECT package.packageid
		FROM campaign, package
		WHERE package.projectid=campaign.projectid AND campaignid='R15'
	)
);


