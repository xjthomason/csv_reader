import api_query_users as api
import csv_reader
import datetime, pandas, csv

#SET_TIME
today = datetime.date.today()
week_ago = unicode(today - datetime.timedelta(days=7))

users = []

def main():
	global week_ago
	
	print('Retrieving Google Admin User Account Information...')
	
	users = api.getUsers(week_ago)
	csv_reader.createCSV(users)

main()
	
