import os
import requests


class Authenticator():
    def get_access_token(self):
        client_id = os.environ["EQUINIX_CLIENT_ID"]
        client_secret = os.environ["EQUINIX_CLIENT_SECRET"]
        api_host = "https://uatapi.equinix.com/oauth2/v1/token"
        headers = {"Content-Type":"application/json", "Accept":"application/json"}
        data = {"client_id":client_id, "client_secret":client_secret, "grant_type":"client_credentials"}
        

        response = requests.post(url=api_host, headers=headers,  json=data)
        if (response.status_code) != 200:
            return "auth failed"
        else: 
            r_json = response.json()
            access_token = r_json["access_token"]
            return access_token