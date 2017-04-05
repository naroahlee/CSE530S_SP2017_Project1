#!/usr/bin/python

import csv
Input1_CSV  = 'CensusMSA.csv'
Input2_CSV  = 'CensusNonMSA.csv'
Output_CSV  = 'MergedCensus.csv'


NewList = []
Header = (
		'StateCode',
		'CountyCode', 
		'TractCode', 
		'MSA', 
		'CensusYear', 
		'Minority_Population',
		'Non_hispanic_other',
		'Non_hispanic_asian',
		'Non_hispanic_white',
		'Non_hispanic_american_indian',
		'Non_hispanic_black',
		'Hispanics',
		'Population',
		'Minority_percentage',
		'Family_count',
		'Household_count',
		'DistressedTractInd',
		'Income_Indicator',
		'Poverty_level_percentage',
		'MSA_MFI_pct',
		'Decennial_Trace_MHI',
		'Decennial_MSA_MFI',
		'HUD_est_MSA_MFI',
		'Est_Income',
		'sDecennial_Tract_MFI',
		'Median_unit_age',
		'Total_housing_units',
		'Num_1_to_4_units',
		'Own_occ_1_to_4_units',
		'Owner_occupied_units',
		'Renter_occupied_units',
		'Units_vacant',
		'Central_City_Flag'
		)
NewList.append(Header)
MyYear='2015'

# Read DonorList provided by Data Vendor
with open(Input1_CSV, 'r') as readFile:
	reader = csv.reader(readFile)
	Donor_List = list(reader)

StateCode_Col                    = 12
CountyCode_Col                   = 15
TractCode_Col                    = 11
MSA_Col                          = 2

# Census
Minority_Population_Col          = 0
Non_hispanic_other_Col           = 4
Non_hispanic_asian_Col           = 7
Non_hispanic_white_Col           = 9
Non_hispanic_american_indian_Col = 16
Non_hispanic_black_Col           = 28
Hispanics_Col                    = 27
Population_Col                   = 13
Minority_percentage_Col	         = 10 
Family_count_Col                 = 22
Household_count_Col              = 8
DistressedTractInd_Col           = 21
# Income
Income_Indicator_Col             = 30
Poverty_level_percentage_Col     = 23
MSA_MFI_pct_Col                  = 14
Decennial_Trace_MHI_Col          = 19
Decennial_MSA_MFI_Col            = 25
HUD_est_MSA_MFI_Col              = 29
Est_Income_Col                   = 32
sDecennial_Tract_MFI_Col         = 33

# Housing
Median_unit_age_Col              = 6
Total_housing_units_Col          = 17
Num_1_to_4_units_Col             = 26
Own_occ_1_to_4_units_Col         = 20
Owner_occupied_units_Col         = 24
Renter_occupied_units_Col        = 31
Units_vacant_Col                 = 34
Central_City_Flag_Col            = 18


isHead = True
for Item in Donor_List:
	if(True == isHead):
		isHead = False
		continue

	NewItem = (
			Item[StateCode_Col], 
			Item[CountyCode_Col], 
			Item[TractCode_Col], 
			Item[MSA_Col], 
			MyYear,
			Item[Minority_Population_Col         ],
			Item[Non_hispanic_other_Col          ],
			Item[Non_hispanic_asian_Col          ],
			Item[Non_hispanic_white_Col          ],
			Item[Non_hispanic_american_indian_Col],
			Item[Non_hispanic_black_Col          ],
			Item[Hispanics_Col                   ],
			Item[Population_Col                  ],
			Item[Minority_percentage_Col	     ], 
			Item[Family_count_Col                ],
			Item[Household_count_Col             ],
			Item[DistressedTractInd_Col          ],
			Item[Income_Indicator_Col            ],
			Item[Poverty_level_percentage_Col    ],
			Item[MSA_MFI_pct_Col                 ],
			Item[Decennial_Trace_MHI_Col         ],
			Item[Decennial_MSA_MFI_Col           ],
			Item[HUD_est_MSA_MFI_Col             ],
			Item[Est_Income_Col                  ],
			Item[sDecennial_Tract_MFI_Col        ],
			Item[Median_unit_age_Col             ],
			Item[Total_housing_units_Col         ],
			Item[Num_1_to_4_units_Col            ],
			Item[Own_occ_1_to_4_units_Col        ],
			Item[Owner_occupied_units_Col        ],
			Item[Renter_occupied_units_Col       ],
			Item[Units_vacant_Col                ],
			Item[Central_City_Flag_Col           ],
				)
			
	
	# print NewItem
	NewList.append(NewItem)


with open(Input2_CSV, 'r') as readFile:
	reader = csv.reader(readFile)
	Donor_List = list(reader)

StateCode_Col                    = 14
CountyCode_Col                   = 17
TractCode_Col                    = 13
MSA_Col                          = 4

# Census
Minority_Population_Col          = 2
Non_hispanic_other_Col           = 6 
Non_hispanic_asian_Col           = 9
Non_hispanic_white_Col           = 11
Non_hispanic_american_indian_Col = 18
Non_hispanic_black_Col           = 31
Hispanics_Col                    = 30
Population_Col                   = 15
Minority_percentage_Col	         = 12
Family_count_Col                 = 25
Household_count_Col              = 10
DistressedTractInd_Col           = 21
# Income
Income_Indicator_Col             = 34
Poverty_level_percentage_Col     = 26
MSA_MFI_pct_Col                  = 17
Decennial_Trace_MHI_Col          = 22
Decennial_MSA_MFI_Col            = 28
HUD_est_MSA_MFI_Col              = 32
Est_Income_Col                   = 36
sDecennial_Tract_MFI_Col         = 37

# Housing
Median_unit_age_Col              = 8
Total_housing_units_Col          = 19
Num_1_to_4_units_Col             = 29
Own_occ_1_to_4_units_Col         = 23
Owner_occupied_units_Col         = 27
Renter_occupied_units_Col        = 35
Units_vacant_Col                 = 38
Central_City_Flag_Col            = 24

isHead = True
for Item in Donor_List:
	if(True == isHead):
		isHead = False
		continue

	NewItem = (
			Item[StateCode_Col], 
			Item[CountyCode_Col], 
			Item[TractCode_Col], 
			Item[MSA_Col], 
			MyYear,
			Item[Minority_Population_Col         ],
			Item[Non_hispanic_other_Col          ],
			Item[Non_hispanic_asian_Col          ],
			Item[Non_hispanic_white_Col          ],
			Item[Non_hispanic_american_indian_Col],
			Item[Non_hispanic_black_Col          ],
			Item[Hispanics_Col                   ],
			Item[Population_Col                  ],
			Item[Minority_percentage_Col	     ], 
			Item[Family_count_Col                ],
			Item[Household_count_Col             ],
			Item[DistressedTractInd_Col          ],
			Item[Income_Indicator_Col            ],
			Item[Poverty_level_percentage_Col    ],
			Item[MSA_MFI_pct_Col                 ],
			Item[Decennial_Trace_MHI_Col         ],
			Item[Decennial_MSA_MFI_Col           ],
			Item[HUD_est_MSA_MFI_Col             ],
			Item[Est_Income_Col                  ],
			Item[sDecennial_Tract_MFI_Col        ],
			Item[Median_unit_age_Col             ],
			Item[Total_housing_units_Col         ],
			Item[Num_1_to_4_units_Col            ],
			Item[Own_occ_1_to_4_units_Col        ],
			Item[Owner_occupied_units_Col        ],
			Item[Renter_occupied_units_Col       ],
			Item[Units_vacant_Col                ],
			Item[Central_City_Flag_Col           ],
				)
	
	# print NewItem
	NewList.append(NewItem)


# Dump CSV File
with open(Output_CSV, 'w') as resFile:
	writer = csv.writer(resFile, dialect = 'excel')
	writer.writerows(NewList)
