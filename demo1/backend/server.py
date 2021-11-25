from flask import Flask, request
from flask_cors import CORS
import requests
import json
from urllib.parse import urlparse
from Authenticator import Authenticator


app = Flask(__name__)
CORS(app)
auth = Authenticator()


@app.route("/health", methods=['GET'])
def health():
  return {"state":"Up and running"}

@app.route("/router", methods=['POST', 'OPTIONS'])
def get_ibx_regions():
    if request.method == 'OPTIONS':
        return ''
    access_token = auth.get_access_token()
    json_data = request.get_json()

    if (('url' in json_data) and ('method' in json_data) and ('metro_code' in json_data)):
        url = json_data["url"]
        method = json_data["method"]
        metro_code = json_data["metro_code"]


        if urlparse(url).hostname.__contains__("uatapi.equinix.com"):
            headers = {
                "Authorization" : "Bearer " + access_token
            }
            result = requests.get(url, headers=headers)
            j_data = json.loads(result.text)

            output = {}
            output['code'] = j_data['code']
            output['region'] = j_data['region']
            output['connectedMetros'] = []
            for metro in j_data['connectedMetros']:
                t = {}
                t['avgLatency'] = metro['avgLatency']
                t['code'] = metro['code']
                output['connectedMetros'].append(t) 
            

            return output
        else:
            return {"result":"ok"}        
    else:
        return {"result":"ok"}