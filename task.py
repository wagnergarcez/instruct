#!/usr/bin/env python3

'''
    Author: Wagner Garcez
    Date created: 14/03/2019
    Python Version: 3
'''

import sys
import json

try:
    import requests
except:
	import urllib.request

def parse_json(json, all_websites, count):

    for data in json:

        # add websites in list
        all_websites.append(data['website'])

        # Samanthas's mail
        if data['username'] == 'Samantha':
            mail = data['email']

        # counter of total users in the southern hemisphere
        count += [lambda:0, lambda:1][float(data['address']['geo']['lat']) < 0]()

    return mail, count

def main():

	count = 0
	all_websites = []

	if 'requests' in sys.modules: # use module requests

		res = requests.get('https://jsonplaceholder.typicode.com/users')
		jdata = res.json() 

	else: # use module urlib

		url = urllib.request.urlopen('https://jsonplaceholder.typicode.com/users')
		res = url.read()
		jdata = json.loads(res.decode("utf-8"))

	# call function 
	mail, count = parse_json(jdata, all_websites, count)

    # outputs
	print('\nWebsites de todos os usuarios: {} '.format(', '.join(map(str, all_websites))))
	print('\nEmail da usuaria Samantha: {}'.format(mail))
	print('\nTotal de usuarios no hemisferio sul: {}\n'.format(count))

if __name__ == "__main__":
	main()
