#!/usr/bin/env python3

'''
    Author: Wagner Garcez
    Date created: 13/03/2019
    Python Version: 3
'''

try:
    # import module
    import requests

    # variables
    count = 0
    all_websites = []
    
    # get request 
    result = requests.get('https://jsonplaceholder.typicode.com/users')
    
    for data in result.json():

            # add websites in list
            all_websites.append(data['website'])

            # Samanthas's mail
            if data['username'] == 'Samantha':
                mail = data['email']

            # counter of total users in the southern hemisphere
            count += [lambda:0, lambda:1][float(data['address']['geo']['lat']) < 0]()

    # outputs
    print('\nWebsites de todos os usuarios: {} '.format(', '.join(map(str, all_websites))))
    print('\nEmail da usuaria Samantha: {}'.format(mail))
    print('\nTotal de usuarios no hemisferio sul: {}\n'.format(count))

except Exception as e:
    print (str(e))
