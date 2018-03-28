from __future__ import print_function

from creds import api_credentials as creds

import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

def getReport():
	
	credentials = creds.get_credentials_report()
	http = credentials.authorize(httplib2.Http())
	service = discovery.build('admin', 'reports_v1', http=http)

	print('Getting the last 10 login events')
	results = service.activities().list(userKey='all', applicationName='login', maxResults=10).execute()
	activities = results.get('items', [])
	
	if not activities:
		print('No logins found.')
	else:
		print('Logins:')
		for activity in activities:
			print('{0}: {1} ({2})'.format(activity['id']['time'], activity['actor']['email'], activity['events'][0]['name']))

getReport()
