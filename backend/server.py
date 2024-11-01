from flask import Flask, request, jsonify

import products_dao
from sql_connection import get_sql_connection

app = Flask(__name__)

connection = get_sql_connection()

@app.route('/getProducts', methods=['GET'])
def get_Products():
    products = products_dao.get_all_product(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__=="__main__":
    print("Starting Python Flask Srver For Grocery Store Management System")
    app.run(port=5000)