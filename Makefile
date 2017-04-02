# Makefile for WUSTL CSE530S SP17 Project 1
# Fund_Raising Database
# Author lihaoran@email.wustl.edu
#

DB_NAME=Fund_Raising
USER_NAME=lihaoran
QUERIES_DIR=./Queries
BUILD_DB_DIR=./Queries/Build_DB
PYTHON_SRC_DIR=./python_src
DST_DIR=./Output_Data
ORIGINAL_DATA_DIR=./Original_Data
INPUT_DATA_DIR=./Input_Data

.PHONY: all install input_data clean database_all database_clean

ALL  = Joined_Parsed.csv
ALL += GiftAmountInCSV.csv

Input_Data  = DonorInDB.csv
Input_Data += GiftInDB.csv
Input_Data += PackageInDB.csv
Input_Data += SendmailInDB.csv 
Input_Data += ClientInDB.csv
Input_Data += DataAnalystInDB.csv 
Input_Data += CampaignInDB.csv 

all: ${ALL}

install:
	cp ${ALL} ${DST_DIR}

clean:
	rm -rf ./*.csv

DonorInDB.csv: 
	${PYTHON_SRC_DIR}/CropDonor.py ${ORIGINAL_DATA_DIR}/UL040J.csv $@

GiftInDB.csv: 
	${PYTHON_SRC_DIR}/CropGift.py ${ORIGINAL_DATA_DIR}/GiftList.csv $@

PackageInDB.csv: 
	${PYTHON_SRC_DIR}/CropPackage.py ${ORIGINAL_DATA_DIR}/SrcMat.csv $@

SendmailInDB.csv: 
	${PYTHON_SRC_DIR}/CropSendmail.py ${ORIGINAL_DATA_DIR}/UL040J.csv $@

ClientInDB.csv:
	${PYTHON_SRC_DIR}/CreateClient.py $@

DataAnalystInDB.csv:
	${PYTHON_SRC_DIR}/CreateDataAnalyst.py $@

CampaignInDB.csv:
	${PYTHON_SRC_DIR}/CreateCampaign.py $@

input_data: ${Input_Data}
	rm -rf Input_Data/*
	cp ${Input_Data} ${INPUT_DATA_DIR}
	

database_all: Create_DB Create_Table Import_Data

database_clean: Drop_Table Drop_DB

Joined_Parsed.csv: Get_Package_Snd_Rcv.csv
	${PYTHON_SRC_DIR}/ParsePackageID.py $< $@

Get_Package_Snd_Rcv.csv:
	${PYTHON_SRC_DIR}/Convert_Query2csv.py ${DB_NAME} ${USER_NAME} ${QUERIES_DIR}/Get_Package_Snd_Rcv.sql $@

GiftAmountInCSV.csv:
	${PYTHON_SRC_DIR}/Convert_Query2csv.py ${DB_NAME} ${USER_NAME} ${QUERIES_DIR}/GetGiftAmountofCampaign.sql $@

	

Create_DB:
	createdb ${DB_NAME}

Drop_DB:
	dropdb ${DB_NAME}

Create_Table:
	psql -d ${DB_NAME} -f ${BUILD_DB_DIR}/create_table.sql

Drop_Table:
	psql -d ${DB_NAME} -f ${BUILD_DB_DIR}/drop_table.sql

Import_Data:
	psql -d ${DB_NAME} -f ${BUILD_DB_DIR}/copy_data.sql
