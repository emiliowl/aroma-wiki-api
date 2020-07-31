# -*- coding: utf-8 -*-
from os import getenv


class Config:
    SECRET_KEY = getenv('SECRET_KEY') or 'a random string'
    APP_PORT = int(getenv('APP_PORT'))
    DEBUG = eval(getenv('DEBUG').title())
    OIDC_INTROSPECTION_AUTH_METHOD = getenv('OIDC_INTROSPECTION_AUTH_METHOD')
    OIDC_CLIENT_SECRETS = getenv('OIDC_CLIENT_SECRETS')
    OIDC_ID_TOKEN_COOKIE_SECURE = eval(getenv('OIDC_ID_TOKEN_COOKIE_SECURE').title())
    OIDC_SCOPES = eval(getenv('OIDC_SCOPES'))
    OIDC_CALLBACK_ROUTE = getenv('OIDC_CALLBACK_ROUTE')
    OIDC_TOKEN_TYPE_HINT = getenv('OIDC_TOKEN_TYPE_HINT')


class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
