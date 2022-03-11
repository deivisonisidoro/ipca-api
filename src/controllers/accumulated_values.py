# LIBS
from flask import Flask
from flask_restplus import Api, Resource

# IMPORTS
from src.server.instance import server
from src.models.accumulated_values import accumulated_values

# VARIABLES
app = server.app
api = server.api

accumulatedValuesDB =[
        {
        "date": "11/03/2022",
        "values": 10
        },
        {
        "date": "12/03/2022",
        "values": 11
        },
        {
        "date": "13/03/2022",
        "values": 12
        }
]

@api.route("/values")
class AccumulatedValues(Resource):
    @api.marshal_list_with(accumulated_values)
    def get(self,):
        return accumulatedValuesDB