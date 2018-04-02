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
	
	number = 0
	with open('Google_list_%s.csv' % today, 'wb') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames = ['Email', 'First Name', 'Last Name', 'Full Name', 'Location'])
		writer.writeheader()
		for i in list:
			number += 1
			email = i.split(',')[0]
			firstName = i.split(',')[1]
			lastName = i.split(',')[2]
			fullName = i.split(',')[3]
			OU = i.split(',')[4]
			try:
				location = OU.split('/')[1] + ' - ' + OU.split('/')[3]
			except:
				location = OU.split('/')[1]			
				continue
			
			print str(number) + ' ' + fullName	
			writer.writerow({'Email': email, 
							 'First Name': firstName, 
							 'Last Name': lastName, 
							 'Full Name': fullName, 
							 'Location': str(location)})
			#print location.split('/')
	
	os.system('cp Google_list_%s.csv output/ -f' % today)
	os.system('rm Google_list_%s.csv' % today)

def parseColumnExtractEmails(csvFile, columnName):
	
	file = pd.read_csv(csvFile)
	results = file[columnName]
	for r in results:
		print r.split(' ')[0]
	
