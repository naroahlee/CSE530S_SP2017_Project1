CREATE TABLE Donor
(
	FirstName		varchar(50)		NOT NULL, 
	LastName		varchar(50)		NOT NULL,
	CurrentAddress  varchar(50)		NOT NULL,
	City			varchar(50)		NOT NULL,
	State			varchar(50)		NOT NULL,
	Zip				integer			NOT NULL,
	DonorID			varchar(50)		NOT NULL,
	ClientID		integer,
	Primary key (DonorID)
);

CREATE TABLE Gift
(
	GiftDate		date			Not NULL,
	GiftType		varchar(50)		NOT NULL,
	GiftID			integer			NOT NULL,
	GiftState		varchar(50),
	GiftAmount		real			NOT NULL,
	DonorID			varchar(50)		NOT NULL,
	PackageID		varchar(50),
	Primary key (GiftID)
);

CREATE TABLE DataAnalyst
(
	EmployeeID		varchar(50)		NOT NULL,
	FirstName		varchar(50)		NOT NULL,
	LastName		varchar(50)		NOT NULL,
	Gender			varchar(50)		NOT NULL,
	DateofBirth		date			NOT NULL,
	Primary key (EmployeeID)
);


CREATE TABLE Campaign 
(
	ProjectID		integer			NOT NULL,
	CampaignID		varchar(50)		NOT NULL,
	CampaignDate	DATE,
	Type			varchar(20),
	ClientID		integer			NOT NULL,
	Primary key (ProjectID)
);

CREATE TABLE Client 
(
	ClientType		varchar(50)		NOT NULL,
	ClientID		integer			NOT NULL,
	ClientName		varchar(50)		NOT NULL,
	EmployeeID		varchar(50)		NOT NULL,
	Primary key (ClientID)
);

CREATE TABLE Package 
(
	PackageID		varchar(50)		NOT NULL,
	PackageRecency	varchar(50),
	PackageRange	varchar(50),
	PackageMS		varchar(50),
	ProjectID		integer			NOT NULL,
	Primary key (PackageID)
);

CREATE TABLE SendMail
(
	DonorID			varchar(50)		NOT NULL,
	PackageID		varchar(50)		NOT NULL
);

CREATE TABLE Donor_Tract
(
	DonorID			varchar(50) NOT NULL,
	StateCode		varchar(50) NOT NULL,
	CountyCode		varchar(50) NOT NULL,
	TractCode		varchar(50) NOT NULL,
	MSA				varchar(50) NOT NULL,
	CensusYear		integer		NOT NULL,
	Primary key (DonorID,StateCode,CountyCode,TractCode,CensusYear)
);



CREATE TABLE Tract_Census
(
	StateCode					varchar(50) NOT NULL,
	CountyCode					varchar(50) NOT NULL,
	TractCode					varchar(50) NOT NULL,
	MSA							varchar(50) NOT NULL,
	CensusYear					integer NOT NULL,
	MinorityPopulation			integer,
	NonHispanicOther integer,
	NonHispanicAsian integer,
	NonHispanicWhite integer,
	NonHispanicAmericanIndian	integer,
	NonHispanicBlack integer,
	Hispanics integer,
	Population integer,
	MinorityPercentage real,
	FamilyCount integer,
	HouseHoldCount integer,
	DistressedTractInd varchar(50),
	IncomeIndicator varchar(50),
	PovertyLevelPercentage real,
	MSA_MFI_pct real,
	Decennial_Trace_MHI integer,
	Decennial_MSA_MFI integer,
	HUD_est_MSA_MFI integer,
	Est_Income integer,
	Decennial_Tract_MFI integer,
	Median_unit_age integer,
	Total_housing_units integer,
	Num_1_to_4_units integer,
	Own_occ_1_to_4_units integer,
	Owner_occupied_units integer,
	Renter_occupied_units integer,
	Units_vacant integer,
	Central_City_Flag integer,
	Primary key (StateCode,CountyCode,TractCode,CensusYear)
);
