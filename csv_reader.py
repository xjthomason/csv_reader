# TODO automate Google Audit Report for User Creation (once a week)
# Establish output location (should never change)
# Setup place for this script to run and output location
# Run extracted emails through Google query to grab FirstName, LastName, and OU (for location)

# GLOBAL
#csvfile = location of Report output
#columnName = 'Event Description'

import csv, datetime, os, locations
#from progressbar import Percentage,ProgressBar,Bar,ETA
#import pandas as pd

today = datetime.date.today()

def createCSV(list):
	global today
	
	#N = len(list)
	#pbar = ProgressBar(widgets=[Bar('>', '[', ']'), '', Percentage(), '', ETA()],
	#					maxval=N).start()
	with open('Google_list_%s.csv' % today, 'wb') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames = ['Email', 'First Name', 'Last Name', 'Phone Number', 
														'Extension', 'Group', 'Location', 'Division', 'Manager Name', 
														'Manager Email', 'Employee Number', 'Job Title', 'Password', 'Mobile'])
		writer.writeheader()
		for i in list:
			email = i.split(',')[0]
			firstName = i.split(',')[1]
			lastName = i.split(',')[2]
			OU = i.split(',')[3]
			group = locations.location_group(OU)
			
			writer.writerow({'Email': email, 
							 'First Name': firstName.encode('utf-8'), 
							 'Last Name': lastName.encode('utf-8'), 
							 'Group': group})
			#pbar.update(e+1)
			#print location.split('/')
	
	os.system('cp Google_list_%s.csv output/ -f' % today)
	os.system('rm Google_list_%s.csv' % today)

# def parseColumnExtractEmails(csvFile, columnName):
	
	# file = pd.read_csv(csvFile)
	# results = file[columnName]
	# for r in results:
		# print r.split(' ')[0]
	
