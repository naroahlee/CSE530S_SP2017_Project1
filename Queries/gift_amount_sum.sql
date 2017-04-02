SELECT SUM(giftamount)
FROM gift
WHERE packageid in
(
	SELECT package.packageid
	FROM campaign, package
	WHERE package.projectid=campaign.projectid AND campaignid='R15'
);