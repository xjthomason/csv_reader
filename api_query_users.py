from __future__ import print_function

from creds import api_credentials as creds

import httplib2, os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

def getUsers(date):
	
	credentials = creds.get_credentials_users()
	http = credentials.authorize(httplib2.Http())
	service = discovery.build('admin', 'directory_v1', http=http)
	cont = '' #this will become nextPageToken
	output = []
	next = True
	#errors = 0
	
	while next:
		
		results = service.users().list(domain = 'avx.com', maxResults = 500, orderBy = 'email', pageToken = cont).execute()
		users = results.get('users', [])

		try:
			
			if not users:
				print('Nothing')
			else:
				for user in users:
					if user['creationTime'] >= date: # pull all users created in the last week
						output.append((u'{0}, {1}, {2}, ({3}), {4}'.format(user['primaryEmail'],user['name']['givenName'],user['name']['familyName'],user['name']['fullName'],user['orgUnitPath'])))
					else:
						continue
			if results.get('nextPageToken') == None: # check to see if there are more users
				#print (errors)
				return output
				next = False # exit the loop
			else:
				cont = (results.get('nextPageToken')) # collect new PageToken to put through next loop
				
		except Exception, e:
			#(errors + 1)
			pass
