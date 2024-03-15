import mysql.connector

from flask import Flask, render_template, request, redirect, url_for, session, jsonify, json
from sql_connection import get_sql_connection
import mysql.connector
import json


import productDao
import orderDao
import unitDao
from loginDao import validate_user
from registerDao import register_user
from devLoginDao import validate_dev_user
from model import recommend_food

app = Flask(__name__)

connection = get_sql_connection()



@app.route('/getUnit', methods=['GET'])
def get_unit():
    response = unitDao.get_unit(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getProducts', methods=['GET'])
def get_products():
    response =productDao.get_all_products(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertProduct', methods=['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])
    product_id = productDao.insert_new_product(connection, request_payload)
    response = jsonify({
        'product_id': product_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    response = orderDao.get_all_orders(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertOrder', methods=['POST'])
def insert_order():
    request_payload = json.loads(request.form['data'])
    order_id = orderDao.insert_order(connection, request_payload)
    response = jsonify({
        'order_id': order_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    return_id = productDao.delete_product(connection, request.form['product_id'])
    response = jsonify({
        'product_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/devlogin', methods=['POST'])
def logindev():
    username = request.form['username']
    password = request.form['password']

    if validate_dev_user(connection, username, password):
        response = jsonify({'status': 'success', 'message': 'Login successful'})
    else:
        response = jsonify({'status': 'failed', 'message': 'Invalid credentials'})

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# Login API endpoint
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if validate_user(connection, username, password):
        response = jsonify({'status': 'success', 'message': 'Login successful'})
    else:
        response = jsonify({'status': 'failed', 'message': 'Invalid credentials'})

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# Register API endpoint
@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']

    if register_user(connection, username, password):
        response = jsonify({'status': 'success', 'message': 'Registration successful'})
    else:
        response = jsonify({'status': 'failed', 'message': 'Username already taken'})

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
#recommendation
@app.route('/predict', methods=['POST'])
def predict():
    ingredients_input = request.form['ingredients']
    
    recommendations = recommend_food(ingredients_input)
    
    response = jsonify(recommendations)
    
    response.headers['Access-Control-Allow-Origin'] = '*'
    
    return response



if __name__ == "__main__":
    print("Starting Python Flask Server For Binod Grocery Store Management System")
    app.run(port=5000)
