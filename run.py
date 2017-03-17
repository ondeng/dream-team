# run.py

import os
from flask import Flask

from app import create_app

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)

#app = Flask(__name__)



if __name__ == '__main__':
    app.run()