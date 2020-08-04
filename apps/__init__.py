# -*- coding: utf-8 -*-
from flask import Flask
from flask_oidc import OpenIDConnect
from config import config
from api import configure_api


def create_app(config_name: str) -> Flask:
    app = Flask('api-aroma-wiki')
    app.config.from_object(config[config_name])
    oidc = OpenIDConnect()
    configure_api(app, oidc)
    oidc.init_app(app)

    return app
