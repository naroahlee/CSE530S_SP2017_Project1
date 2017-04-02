SELECT firstname,lastname,donorid
FROM donor
WHERE donorid in
(
	SELECT donorid
	FROM gift
	WHERE giftamount>500
);