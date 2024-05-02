from flask import Flask, request, jsonify
from ultralytics import YOLO
import cv2
import numpy as np
import json

app = Flask(__name__)

with open('DB.json', "r") as file:
    panes = json.load(file)

@app.route('/panes', methods=['GET'])
def get_panes():
    try:
        return jsonify(panes)
    except Exception as e:
        return str(e)
    
@app.route('/panes', methods=['POST'])
def post_panes():
    try:
        data = request.json
        panes.append(data)
        with open('DB.json', "w") as file:
            json.dump(panes, file)
        return jsonify(panes)
    except Exception as e:
        return str(e)
    
@app.route('/panes', methods=['DELETE'])
def delete_panes():
    try:
        panes.clear()
        with open('DB.json', "w") as file:
            json.dump(panes, file)
        return jsonify(panes)
    except Exception as e:
        return str(e)

@app.route('/panes/<int:id>', methods=['GET'])
def get_pane(id):
    try:
        return jsonify(panes[id])
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run(debug=True, port=5000)