
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from pprint import pprint

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'cafe'
#app.config['MONGO_URI'] = 'mongodb://username:password@hostname:port/databasename'
app.config['MONGO_URI'] = 'mongodb://sajiri:sajiri@ds033196.mlab.com:33196/cafe'
mongo = PyMongo(app)

#---------------------------------------------------------------------------------------------------------------------
@app.route('/add', methods=['GET'])
def add():
    cafe = mongo.db.cafe
    cafe.insert([
    { "number" : "1", "item": "Espresso", "price": "2.49$", "cal": 205, "size": "Small" },
    { "number" : "2", "item": "Espresso", "price": "3.99$", "cal": 299, "size": "Medium"},
    { "number" : "3", "item": "Espresso", "price": "5.99$", "cal": 319, "size": "Large"},
    { "number" : "4", "item": "Cappuccino", "price": "2.99$", "cal": 215, "size": "Small" },
    { "number" : "5", "item": "Cappuccino", "price": "4.49$", "cal": 335, "size": "Medium"},
    { "number" : "6", "item": "Cappuccino", "price": "5.49$", "cal": 465, "size": "Large"},
    { "number" : "7", "item": "Latte", "price": "2.49$", "cal": 205, "size": "Small" },
    { "number" : "8", "item": "Latte", "price": "3.99$", "cal": 275, "size": "Medium"},
    { "number" : "9", "item": "Latte", "price": "4.99$", "cal": 378, "size": "Large"},
    { "number" : "10", "item": "Americano", "price": "2.69$", "cal": 302, "size": "Small" },
    { "number" : "11", "item": "Americano", "price": "3.99$", "cal": 403, "size": "Medium"},
    { "number" : "12", "item": "Americano", "price": "4.49$", "cal": 515, "size": "Large"},
    { "number" : "13", "item": "Hot Chocolate", "price": "3$", "cal": 317, "size": "Small" },
    { "number" : "14", "item": "Hot Chocolate", "price": "4$", "cal": 418, "size": "Medium"},
    { "number" : "15", "item": "Hot Chocolate", "price": "5$", "cal": 521, "size": "Large"},
    { "number" : "16", "item": "Tea", "price": "1.69$", "cal": 105, "size": "Small" },
    { "number" : "17", "item": "Tea", "price": "2.49$", "cal": 195, "size": "Medium"},
    { "number" : "18", "item": "Tea", "price": "3.19$", "cal": 245, "size": "Large"},
    { "number" : "19", "item": "Black Tea", "price": "3.49$", "cal": 245, "size": "Small" },
    { "number" : "20", "item": "Black Tea", "price": "4.69$", "cal": 345, "size": "Medium"},
    { "number" : "21", "item": "Black Tea", "price": "5.15$", "cal": 395, "size": "Large"},
    { "number" : "22", "item": "Iced Tea", "price": "4.49$", "cal": 445, "size": "Medium" },
    { "number" : "23", "item": "Soda", "price": "2.99$", "cal": 317, "size": "Medium"},
    { "number" : "24", "item": "Coke", "price": "2.99$", "cal": 415, "size": "Large"}
    ])

    return "Value added"

#---------------------------------------------------------------------------------------------------------------------
#To read all the records in the database perform "Enquire" operation
@app.route('/enquire', methods=['GET'])
def get_all_records():
    cafe = mongo.db.cafe

    output = []

    for q in cafe.find():
        output.append({'item' : q['item'], 'price' : q['price'], 'cal' : q['cal'], 'size' : q['size'], 'number' : q['number']})

    return jsonify({'result' : output})
    ouput = '\n Required fields for operations: 1. Insert: all fields 2. Fetch single record: item,size 3. Delete: item,size '
#---------------------------------------------------------------------------------------------------------------------
#To read only single record from database
@app.route('/enquire/<number>', methods=['GET'])
def get_one_record(number):
    cafe = mongo.db.cafe

    q = cafe.find_one({'number' : number})

    if q:
        output = {'item' : q['item'], 'price' : q['price'], 'cal' : q['cal'], 'size' : q['size'], 'number' : q['number']}
    else:
        output = 'No results found'

    return jsonify({'result' : output})

#---------------------------------------------------------------------------------------------------------------------
#To "Insert" a new record in the database
@app.route('/insert', methods=['POST'])
def insert_record():
    cafe = mongo.db.cafe 

    item = request.json['item']
    price = request.json['price']
    cal = request.json['cal']
    size = request.json['size']
    number = request.json['number']

    cafe_id = cafe.insert({'item' : item, 'price' : price, 'cal' : cal, 'size' : size, 'number' : number})
    new_cafe = cafe.find_one({'_id' : cafe_id})

    output = {'item' : new_cafe['item'], 'price' : new_cafe['price'], 'cal' : new_cafe['cal'], 'size' : new_cafe['size'], 'number' : new_cafe['number']}

    return "New Record Inserted"

#---------------------------------------------------------------------------------------------------------------------
#To "Remove" a record from the database using "number"
@app.route('/remove', methods=['POST'])
def remove_record():
    cafe = mongo.db.cafe

    number = request.json['number']

    q = cafe.find_one({'number' : number})
    
    if q:
        result = cafe.remove(q)
    else:
        return "No Record Found"

    return "Record Deleted"

#---------------------------------------------------------------------------------------------------------------------
#To "Update" a record in the database
@app.route('/update', methods=['POST'])
def update_record():
    cafe = mongo.db.cafe
    item = request.json['item']
    price = request.json['price']
    cal = request.json['cal']
    size = request.json['size']
    number = request.json['number']

    q = cafe.find_one({'number' : number})
    
    if q:
        result = cafe.update_one({'number' : number}, {"$set" : {'item' : item, 'price' : price, 'cal' : cal, 'size' : size}})
    else:
        return "No Record Found"

    return "Record Updated"
    return jsonify ({'result' : result})

#---------------------------------------------------------------------------------------------------------------------

#To "Remove" all the records from the database
@app.route('/removeall', methods=['POST'])
def remove_all_records():
    cafe = mongo.db.cafe
    
    result = cafe.remove()

    return "All the Records are Deleted"

#-----------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)
