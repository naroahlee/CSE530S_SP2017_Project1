 SELECT povertylevelpercentage, Est_Income, Median_unit_age
 FROM Tract_Census as T, Donor_Tract as D
 WHERE D.StateCode=T.StateCode AND D.CountyCode=T.CountyCode
 AND D.TractCode=T.TractCode AND D.CensusYear=T.CensusYear
 AND
 (D.Donorid,D.StateCode,D.CountyCode,D.TractCode,D.CensusYear) IN
 (
 	SELECT Donorid, StateCode,CountyCode, TractCode, CensusYear
 	FROM Donor_Tract
 	WHERE donorid in
 	(
  		SELECT donor.donorid
  		FROM donor, gift
  		WHERE donor.donorid=gift.donorid AND packageid IN 
  		(
  			SELECT package.packageid
  			FROM campaign, package
 			WHERE package.projectid=campaign.projectid AND campaignid='R15'
  		)
  	)
  );