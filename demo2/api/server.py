from flask import Flask, request, make_response
from flask_cors import CORS
import requests
import re



app = Flask(__name__)
CORS(app)

def check_customer_data(value, regex):
    regex = re.compile(regex)
    if regex.match(value):
        return True
    else:
        return False

@app.route("/health", methods=['GET'])
def health():
  return {"state":"Up and running"}

@app.route("/api/v1/orders/generate_document", methods=['POST'])
def generate_order():
    
    json_data = request.get_json()

    if (('order_id' in json_data ) and ('company' in json_data) and ('price' in json_data) and ('comment' in json_data)):
        order_id = str(json_data['order_id'])
        if not check_customer_data(order_id, "^[0-9]+$"):
            return ''
            
        company = json_data['company']
        if not check_customer_data(company, "^[a-zA-Z0-9]+$"):
            return ''

        price = str(json_data['price'])
        if not check_customer_data(price, "^[0-9]+$"):
            return ''
        
        comment = json_data['comment']
        # not sure how to validate this - business wants to be free text field
        # to be discussed
        
        order_file = ''
        with open('template.html', 'r') as html_template:
            order_file = html_template.read()
            order_file = order_file.replace("order_id",order_id)
            order_file = order_file.replace("company", company)
            order_file = order_file.replace("price", price)
            order_file = order_file.replace("comment", comment)

        with open('index.html', 'w') as file:
            file.write(order_file)

        files = {'file':open('index.html', 'rb')}
        req = requests.post('http://document-generation-service:3000/convert/html',files=files)
        response = make_response(req.content)
        response.headers.set('Content-Type', 'application/pdf')
        print(req.status_code)
        
        return response
        
    else:
        return {"result":"ok"}