# Active environment
environment = "qa"

# Sample time in ~seconds
sampleTime = 7200

# Device ID for this PI
deviceID = 0

# Different Primary environment configurations
env_dev1 = {'webApi': 'http://marks-macbookair.local:8080/cloudservices/rest/weather/save',
         	'username': 'CloudWorkshop',
         	'password': 'dGVzdHRlc3Q='}
env_dev2 = {'webApi': 'http://node5.codenvy.io:37551/cloudservices/rest/weather/save',
         	'username': 'CloudWorkshop',
         	'password': 'dGVzdHRlc3Q='}
env_qa = {'webApi': 'https://cloudservices3.azurewebsites.net/cloudservices/rest/weather/save',
         	'username': 'CloudWorkshop',
         	'password': 'dGVzdHRlc3Q='}
env_prod = {'webApi': 'https://markwsserve2.azurewebsites.net/cloudservices/rest/weather/save',
         	'username': 'CloudWorkshop',
         	'password': 'dGVzdHRlc3Q='}

# Optional Secondary endpoints to post data
process_sec_endpoints = True
sec_endpoints = [
			['Azure', 'https://cloudservices3.azurewebsites.net/cloudservices/rest/weather/save', 'CloudWorkshop', 'dGVzdHRlc3Q='],
                        ['Google', 'https://cloud-workshop-services.appspot.com/rest/weather/save', 'CloudWorkshop', 'dGVzdHRlc3Q='],
                        ['Heroku', 'https://mark-servicesapp.herokuapp.com/rest/weather/save', 'CloudWorkshop', 'dGVzdHRlc3Q='],
                        ['Amazon', 'http://services-app.us-east-2.elasticbeanstalk.com/rest/weather/save', 'CloudWorkshop', 'dGVzdHRlc3Q='],
                        ['Azure Serverless', 'https://markiotfunctions.azurewebsites.net/api/saveweatherdata', 'CloudWorkshop', 'dGVzdHRlc3Q=']
 		]
