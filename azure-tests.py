#!/usr/bin/python
from azure import *
from azure.servicemanagement import *

subscription_id = 'e225e7e0-8788-44dc-8586-481ee5cbad17'
certificate_path = '../mycert.pem'

sms = ServiceManagementService(subscription_id, certificate_path)

result = sms.list_locations()
for location in result:
    print(location.name)
images = sms.list_vm_images()
for image in images:
    print image.label
    #print image.__dict__