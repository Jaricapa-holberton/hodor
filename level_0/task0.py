#!/usr/bin/python3
"""
Bot for cheating voting contests
This programs allow do 1024 times the input
of a specific data (as show in payload)
"""
import requests

ses = requests.session()

# the data to input in the web page
payload = {
    'id':'2241',
    'holdthedoor':'Enviar'
}

for i in range(1025):
    #this allow insert the data inside of payload
    response = ses.post(url="http://158.69.76.135/level0.php",data=payload)
    #if prints 200, the conection was succesfull
    print(response.status_code)

#print(response.status_code)
#print("============")
#print(response.content)