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
