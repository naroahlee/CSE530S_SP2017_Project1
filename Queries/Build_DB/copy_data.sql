\copy donor			FROM './Input_Data/DonorInDB.csv'			WITH CSV HEADER;
\copy sendmail		FROM './Input_Data/SendmailInDB.csv'		WITH CSV HEADER;
\copy gift			FROM './Input_Data/GiftInDB.csv'			WITH CSV HEADER;
\copy campaign		FROM './Input_Data/CampaignInDB.csv'		WITH CSV HEADER;
\copy package		FROM './Input_Data/PackageInDB.csv'			WITH CSV HEADER;
\copy client		FROM './Input_Data/ClientInDB.csv'			WITH CSV HEADER;
\copy dataanalyst	FROM './Input_Data/DataAnalystInDB.csv'		WITH CSV HEADER;