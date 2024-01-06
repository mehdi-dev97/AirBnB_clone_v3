#!/usr/bin/python3
"""
App views for AirBnB_clone_v3
"""

from flask import jsonify, request
from models import storage
from api.v1.views import app_views


@app_views.route('/status')
def status():
    """ returns status """
    status = {"status": "OK"}
    return jsonify(status)

@app_views.route('/stats', methods=['GET'])
def stats():
    """
    function to return the count of all class objects
    """
    if request.method == 'GET':
        response = {}
        STATS = {
            "amenities": 47, 
            "cities": 36, 
            "places": 154, 
            "reviews": 718, 
            "states": 27, 
            "users": 31
        }
        for key, value in STATS.items():
            response[value] = storage.count(key)
        return jsonify(response)
