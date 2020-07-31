# -*- coding: utf-8 -*-
from flask_cors import CORS

def configure_api(app):
    print('configuring blueprints...')
    
    app.url_map.strict_slashes = False
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    print(app.url_map)
