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

import sys
import redfish
import lenovo_utils as utils

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

