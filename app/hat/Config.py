# Active environment
environment = "qa"

# Sample time in ~seconds
sampleTime = 1800

# Device ID for this PI
deviceID = 0

# Different Primary environment configurations
env_dev1 = {'webApi': 'http://marks-macbookair.local:8080/cloudservices/rest/weather/save',
         	'username': 'CloudWorkshop',
         	'password': 'dGVzdHRlc3Q='}
env_dev2 = {'webApi': 'http://node5.codenvy.io:37551/cloudservices/rest/weather/save',
         	'username': 'CloudWorkshop',
         	'password': 'dGVzdHRlc3Q='}
env_qa = {'webApi': 'http://cloudservices-workshop.1d35.starter-us-east-1.openshiftapps.com/cloudservices/rest/weather/save',
         	'username': 'CloudWorkshop',
         	'password': 'dGVzdHRlc3Q='}
env_prod = {'webApi': 'http://cloudservices-workshop.1d35.starter-us-east-1.openshiftapps.com/cloudservices/rest/weather/save',
         	'username': 'CloudWorkshop',
         	'password': 'dGVzdHRlc3Q='}

# Optional Secondary endpoints to post data
process_sec_endpoints = False
sec_endpoints = [
			['Test 1', 'http://somewhere.com/cloudservices/rest/weather/save', 'CloudWorkshop', 'dGVzdHRlc3Q='],
			['Test 2', 'http://somewhere.com/cloudservices/rest/weather/save', 'CloudWorkshop', 'dGVzdHRlc3Q=']
		]