# TODO automate Google Audit Report for User Creation (once a week)
# Establish output location (should never change)
# Setup place for this script to run and output location
# Run extracted emails through Google query to grab FirstName, LastName, and OU (for location)

# GLOBAL
#csvfile = location of Report output
columnName = 'Event Description'

import argparse
import pandas as pd

def parseColumnExtractEmails(csvFile, columnName):
	
	file = pd.read_csv(csvFile)
	results = file[columnName]
	for r in results:
		print r.split(' ')[0]
	
def main():
#	global csvfile
	global columnName
	
	parser = argparse.ArgumentParser('usage%prog ' '-f <csvfile> -c <columnName>')
	parser.add_argument('-f', '--csvfile', help='Please enter the path to the csv file')
	args = parser.parse_args()
	csvfile = args.csvfile
	
	# csvfile = raw_input("Enter file path: ")
	# columnName = raw_input("Enter column name: ")
	
	parseColumnExtractEmails(csvfile, columnName)

main()
