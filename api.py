# -*- coding: utf-8 -*-
from flask_cors import CORS
from flask_oidc import OpenIDConnect


global_info = {
    "oidc": None
}


def configure_api(app, oidc: OpenIDConnect):
    print('configuring blueprints...')
    global_info["oidc"] = oidc

    from apps.core.blueprints.scents import bp as scents_bp
    app.register_blueprint(scents_bp, url_prefix='/api/scents')

    app.url_map.strict_slashes = False
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    print(app.url_map)
