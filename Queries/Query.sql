
-- SELECT firstname,lastname,donor.donorid
SELECT COUNT(*) 
FROM donor, package, sendmail
WHERE package.packageid='R15I2' AND sendmail.donorid=donor.donorid AND sendmail.packageid=package.packageid;

SELECT COUNT(*) 
FROM donor, package, sendmail
WHERE package.packageid='R15A1' AND sendmail.donorid=donor.donorid AND sendmail.packageid=package.packageid;

SELECT COUNT(*)
FROM gift
WHERE packageid='R15I2';

SELECT COUNT(*)
FROM donor
WHERE donorid in
(
	(
		SELECT donor.donorid
		FROM donor, package, sendmail
		WHERE package.packageid='R15I2' AND sendmail.donorid=donor.donorid AND sendmail.packageid=package.packageid
	)
	INTERSECT
	(
		SELECT donorid
		FROM gift
		WHERE packageid='R15I2'	
	)
);

