import json
import logging
import requests


defaultHeaders = {
    "Accept": "*/*",
    "Content-Type": "application/json"
}

class Apex(object):
    def __init__(
        self, username, password, deviceip
    ):

        self.username = username
        self.password = password
        self.deviceip = deviceip
        self.sid = ""



    def auth(self):
        print("Logging In")
        headers = {
            **defaultHeaders
        }
        data = {
            "login" : self.username, 
            "password": self.password, 
            "remember_me" : False
        }


        r = requests.post(
            "http://" + self.deviceip + "/rest/login",
            headers = headers,
            json = data
        )

        print(r.text)
        print(r.request.body)
        print(r.status_code)

        if r.status_code == 200:
            result = r.json()
            self.sid = result["connect.sid"]
        else:
            print("Status code failure")

    def status(self):
        headers = {
            **defaultHeaders,
            "Cookie" : "connect.sid=" + self.sid
        }

        r = requests.get(
            "http://" + self.deviceip + "/rest/status",
            headers = headers
        )

        if r.status_code == 200:
            result = r.json()
            return result
        else:
            print("Error occured")


