# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 11:01:30 2021

@author: navya200
"""
from flask import Flask,jsonify
from flask_restful import reqparse, abort, Api, Resource
import pickle
import numpy as np
import pandas as pd
import csv

app = Flask(__name__)
api = Api(app)


clf_path = 'final.pickle'
with open(clf_path, 'rb') as f:
    model = pickle.load(f)

# argument parsing

parser = reqparse.RequestParser()
parser.add_argument('place')
parser.add_argument('date_time')

class PredictSentiment(Resource):
    def get(self):
        #json_data = request.get_json()
        args = parser.parse_args()
        place=args.place
        date_time=args.date_time
        place=' '+place
        
        with open('Japan_cities_rainfall.csv') as infile:
            read = csv.reader(infile)
            for row in read :
                if row[1]==place and row[0]==date_time:
                    ro=row
                    print(ro)
                    ro.remove(ro[0])
                    ro.remove(ro[0])
                    ro.remove(ro[2])
                    ro=np.array(ro,dtype='float64')
                    roy=ro.reshape(1,-1)
                    predict=np.array2string(model.predict(roy))
                    print(predict)
     
        # create JSON object
        output = {'place': place , 'date_time':date_time ,'rainfall': predict }
        return output
# Setup the Api resource routing here
# Route the URL to the resource
api.add_resource(PredictSentiment, '/')


if __name__ == '__main__':
    app.run(debug=True)
