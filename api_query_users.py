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

	print('Retrieving Google Admin User Account Information...')
	results = service.users().list(domain = 'avx.com', maxResults = 500, orderBy = 'email').execute()
	
	#while results.get('nextPageToken'):
	#	users = results.get('users', [])

	users = results.get('users', [])

	try:
		if not users:
			print('Nothing')
		else:
			print('Users:')
			for user in users:
				#if user['creationTime'] >= week_ago:
				print (u'{0}, {1}, {2}, {3}, {4}'.format(user['primaryEmail'],user['name']['givenName'],user['name']['familyName'],user['name']['fullName'],user['orgUnitPath']))
				#else:
				#	continue
	except Exception, e:
		pass
			
	cont = (results.get('nextPageToken'))
	
# TODO Write loop for all pageTokens and then stop when you run out

	results2 = service.users().list(domain = 'avx.com', maxResults = 500, orderBy = 'email', pageToken = cont).execute()
	
	users2 = results2.get('users', [])
	
	if not users2:
		print ('No more')
	else:
		print('Users:')
		try:
			for user in users2:
				#if user['creationTime'] >= week_ago:
				print (u'{0}, {1}, {2}, {3}, {4}'.format(user['primaryEmail'],user['name']['givenName'],user['name']['familyName'],user['name']['fullName'],user['orgUnitPath']))
		except Exception, e:
			pass
		print (len(users2))
				
				#results.get('users', pageToken = users['nextPageToken'])

getUsers()
