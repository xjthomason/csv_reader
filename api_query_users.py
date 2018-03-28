from __future__ import print_function

from creds import api_credentials as creds

import httplib2, os, datetime

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

#SET_TIME
today = datetime.date.today()
week_ago = unicode(today - datetime.timedelta(days=7))

def getUsers():
	global week_ago
	
	credentials = creds.get_credentials_users()
	http = credentials.authorize(httplib2.Http())
	service = discovery.build('admin', 'directory_v1', http=http)
	cont = '' #this will become nextPageToken
	#errors = 0


	print('Retrieving Google Admin User Account Information...')
	print('Users:')
	
	while True:
		
		results = service.users().list(domain = 'avx.com', maxResults = 500, orderBy = 'email', pageToken = cont).execute()
		users = results.get('users', [])

		try:
			
			if not users:
				print('Nothing')
			else:
				for user in users:
					#if user['creationTime'] >= week_ago:
					print (u'{0}, {1}, {2}, ({3}), {4}'.format(user['primaryEmail'],user['name']['givenName'],user['name']['familyName'],user['name']['fullName'],user['orgUnitPath']))
					#else:
					#	continue
			if results.get('nextPageToken') == None:
				#print (errors)
				return False
			else:
				cont = (results.get('nextPageToken'))
				
		except Exception, e:
			#(errors + 1)
			pass
	
# TODO Write loop for all pageTokens and then stop when you run out

	# results2 = service.users().list(domain = 'avx.com', maxResults = 500, orderBy = 'email', pageToken = cont).execute()
	
	# users2 = results2.get('users', [])
	
	# if not users2:
		# print ('No more')
	# else:
		# print('Users:')
		# try:
			# for user in users2:
				# #if user['creationTime'] >= week_ago:
				# print (u'{0}, {1}, {2}, {3}, {4}'.format(user['primaryEmail'],user['name']['givenName'],user['name']['familyName'],user['name']['fullName'],user['orgUnitPath']))
		# except Exception, e:
			# pass
		# print (len(users2))
				
				#results.get('users', pageToken = users['nextPageToken'])

getUsers()
