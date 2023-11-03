#!/usr/bin/python3
"""returns api status code"""

from api.v1.views import app_views
from flask import Flask
from models import storage
from os import getenv
import api/v1/views/index.py

app = Flask(__name__)
app.register_blueprint(app_views, url_prefix="/api/v1")


@app.teardown_appcontext
def close_session(session):
    """close a session"""
    storage.close()


if __name__ == '__main__':
    host = getenv('HBNB_API_HOST') if getenv('HBNB_API_HOST') else '0.0.0.0'
    port = getenv('HBNB_API_PORT') if getenv('HBNB_API_PORT') else 5000
    app.run(port=port, host=host, threaded=True)
