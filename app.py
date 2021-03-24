import logging
import os

from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'stddata'
app.config['MONGO_URI'] = 'mongodb://' + os.getenv('MONGO_URI', 'localhost') + ':27017/stddata'
mongodb = PyMongo(app)

# Main file

@app.route('/')
def default_route():
    """Default route to return a simple message"""
    return jsonify('Please use /std URI to view content')


@app.route('/std', methods=['GET'])
def get_all_stds():
    std = mongodb.db.stddata
    output = []
    for s in std.find():
        output.append({'name': s['name'], 'ranklevel': s['ranklevel']})
    return jsonify({'result': output})


@app.route('/std/<name>', methods=['GET'])
def get_one_std(name):
    std = mongodb.db.stddata
    s = std.find_one({'name': name})
    if request.method == 'GET':
        if s:
            output = {'name': s['name'], 'ranklevel': s['ranklevel']}
        else:
            output = "No such Student!!!"
    return jsonify({'result': output})


@app.route('/std', methods=['POST'])
def add_std():
    std = mongodb.db.stddata
    name = request.json['name']
    rank_level = request.json['ranklevel']
    std_id = std.insert({'name': name, 'ranklevel': rank_level})
    new_std = std.find_one({'_id': std_id})
    output = {'name': new_std['name'], 'ranklevel': new_std['ranklevel']}
    return jsonify({'result': output})


application = app


if __name__ == '__main__':
    logging.info('starting with MONGO_URL %d', os.getenv('MONGO_URI', 'localhost'))
    app.run(host='0.0.0.0', debug=True)
