from flask_cors import CORS, cross_origin

from src.server.instance import server
from src.controllers.accumulated_values import *


cors = CORS(app)

if __name__ == '__main__':
  server.run()