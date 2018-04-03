# TODO automate Google Audit Report for User Creation (once a week)
# Establish output location (should never change)
# Setup place for this script to run and output location
# Run extracted emails through Google query to grab FirstName, LastName, and OU (for location)

# GLOBAL
#csvfile = location of Report output
columnName = 'Event Description'

import csv, datetime, os
import pandas as pd

today = datetime.date.today()

def createCSV(list):
	global today
	
	with open('Google_list_%s.csv' % today, 'wb') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames = ['Email', 'First Name', 'Last Name', 'Full Name', 'Location'])
		writer.writeheader()
		for i in list:
			email = i.split(',')[0]
			firstName = i.split(',')[1]
			lastName = i.split(',')[2]
			fullName = i.split(',')[3]
			OU = i.split(',')[4]
			if "Asia" in OU:
				location = identifyLang(OU)
			else:
				location = OU.split('/')[1] #TODO split up locations by language
			
			writer.writerow({'Email': email, 
							 'First Name': firstName.encode('utf-8'), 
							 'Last Name': lastName.encode('utf-8'), 
							 'Full Name': fullName.encode('utf-8'), 
							 'Location': location})
			#print location.split('/')
	
	os.system('cp Google_list_%s.csv output/ -f' % today)
	os.system('rm Google_list_%s.csv' % today)
	
def identifyLang(OU):
	
	if "Chi" in OU:
		return "Asia - Chinese"
	elif "Jap" in OU:
		return "Asia - Japanese"
	elif "Mala" or "Pena" in OU:
		return "Asia - Malay"
	elif "Korea" in OU:
		return "Asia - Korean"
	elif "Indi" in OU:
		return "Asia - Hindi"
	else: 
		return "Unsure"

def parseColumnExtractEmails(csvFile, columnName):
	
	file = pd.read_csv(csvFile)
	results = file[columnName]
	for r in results:
		print r.split(' ')[0]
	
