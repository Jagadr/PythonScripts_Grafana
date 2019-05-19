#!/usr/bin/env python
# -- coding: utf-8 --

import pysnow

# Create client object

usr='snc_sys_if_AMS_DGFF'
pwd='CKerUtjUHq9eEeN7'


client = pysnow.Client(host='servicenow-uat.dhl.com', user=usr, password=pwd)
client.parameters.display_value = True
client.parameters.exclude_reference_link  = True


#c = pysnow.Client(instance='myinstance', user='myusername', password='mypassword')

# Define a resource, here we'll use the incident table API
incident = client.resource(api_path='/table/incident')

# Query for incidents with state 1
response = incident.get(query={'state': 1}, stream=True)

# Iterate over the result and print out `sys_id` of the matching records.
for record in response.all():
    print(record['sys_id'])

