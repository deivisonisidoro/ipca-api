from flask_restplus import fields

from src.server.instance import server

accumulated_values = server.api.model("Accumulated Values",
  {
    "date": fields.String(description = "Value Date"),
    "values": fields.Integer()
  }
)