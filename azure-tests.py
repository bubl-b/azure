#!/usr/bin/python
from azure import *
from azure.servicemanagement import *

subscription_id = 'e225e7e0-8788-44dc-8586-481ee5cbad17'
certificate_path = '../mycert.pem'

#sms = ServiceManagementService(subscription_id, certificate_path)