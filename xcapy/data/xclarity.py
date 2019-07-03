# Written by Andrew Clure
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
# 
# These functions are intended to be re-used and imported into other scripts.
# Each function has a brief description of what it does.
#

import requests
from requests.auth import HTTPBasicAuth
import json
import urllib3
import getpass
import argparse
import atexit
import ssl
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

api_url = 'https://192.168.10.43'
api_user = 'pylxca'
#api_pass = getpass.getpass(prompt='Enter your password: ')
api_pass = ''


#r = requests.get(f'{api_url}/aicc', auth=(api_user,api_pass),verify=False)
#print(r.text)
#print(r.status_code)
#print(r.json())


def xca_discovered(username,password,url):
    ''' gets a list of devices that have been discovered '''
    print(f'authenticating to {url} for user: {username}')
    response = requests.get(
                f'{url}/discovery', auth=(username,password),verify=False)
    if response.status_code != 200:
        print(f'ERROR! API responded with: {response.status_code}')
        return
    return response.json()


def xca_storedcred(username,password,url):
    ''' Gets a list of all the stored credentials for managing devices '''
    response = requests.get(
                f'{url}/storedCredentials', auth=(username,password),verify=False)
    if response.status_code != 200:
        print(f'ERROR! API responded with: {response.status_code}')
        return
    return response.json()

def xca_discoverdev(username,password,url,devip):
    ''' discovers devices to be managed '''
    payload = {"ipAddresses": "{devip}"}        
    response = requests.post(
                f'{url}/discoverRequest', 
                auth=(username,password),
                verify=False, 
                data=payload
            )
    if response.status_code != 200:
        print(f'ERROR! API responded with: {response.status_code}')
        return
    return response.headers
    print(payload)
    print(response.headers)


def xca_managedev(username,password,url,devip):
    ''' discovers devices to be managed '''
    payload = [{
                "ipAddresses": [devip],
                "forceManage": True,
                "type": "Rack-Tower Server",
                "securityDescriptor": {
                    "managedAuthEnabled": False,
                    "storedCredentials": {
                        "id" : "16302"
                        }
                    }
                }]
    response = requests.post(
                f'{url}/manageRequest?discovery=false', 
                auth=(username,password),
                data=json.dumps(payload),
                verify=False
            )
    if response.status_code != 200:
        print(f'ERROR! API responded with: {response.status_code}. {response.text}')
        print(payload)
        return
    return response.headers


def xca_newuser(username,password,url,newuser,userpw):
    ''' discovers devices to be managed '''
    payload = {
                "userPw": "Passw0rd",
                "userName": "testUser",
                "description": "New User account created by pyLXCA",
                "groups": ["LXC-ADMIN"],
                "PasswordChangeFirstAccess": True
                }
    response = requests.post(
                f'{url}/userAccounts', 
                auth=(username,password), 
                data=json.dumps(payload),
                verify=False)
    if response.status_code != 201:
        print(f'ERROR! API responded with: {response.status_code}. {response.text}')
        print(payload)
        return response.text
        return
    return response.json()

#xca_newuser(api_user,api_pass,api_url,'testuser','Passw0rd')
#xca_managedev(api_user,api_pass,api_url,'192.168.10.66')
