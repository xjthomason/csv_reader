# TODO automate Google Audit Report for User Creation (once a week)
# Establish output location (should never change)
# Setup place for this script to run and output location
# Run extracted emails through Google query to grab FirstName, LastName, and OU (for location)

# GLOBAL
#csvfile = location of Report output
columnName = 'Event Description'

import csv, datetime
import pandas as pd

today = datetime.date.today()

def createCSV(list):
	global today
	
	with open('Google_list_%s.csv' % today, 'wb') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames = ['Email', 'First Name', 'Last Name', 'Full Name', 'Location'])
		writer.writeheader()
		for i in list:
			print i.split(',')[0]

def parseColumnExtractEmails(csvFile, columnName):
	
	file = pd.read_csv(csvFile)
	results = file[columnName]
	for r in results:
		print r.split(' ')[0]
	
