
-- SELECT firstname,lastname,donor.donorid
SELECT packageid 
FROM package, campaign
WHERE package.projectid=campaign.projectid AND campaignid='R15';