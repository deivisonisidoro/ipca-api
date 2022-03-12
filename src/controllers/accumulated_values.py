# LIBS 
from flask import Flask, Response
from flask_restplus import Api, Resource
from openpyxl import load_workbook
import json
from datetime import date, datetime
# IMPORTS
from src.server.instance import server
from src.models.accumulated_values import accumulated_values

# VARIABLES
app = server.app
api = server.api

@api.route("/values")
class AccumulatedValues(Resource):
    # @api.marshal_list_with(accumulated_values)    
    def get(self,):
       
        book = load_workbook("ipca.xlsx")
        sheet = book.active 
        
        rows = sheet.rows
    
        
        headers = [cell.value for cell in next(rows)]

        all_rows = []

        
        for row in rows:
            data = {}
            for title, cell in zip(headers,  row):
                json_datetime= cell.value
                if isinstance(cell.value, (datetime, date)):
                    formatted_datetime = cell.value.isoformat()
                    json_datetime = json.dumps(formatted_datetime)
                data[title] = json_datetime
               
            all_rows.append(data) 
        
        return all_rows
        