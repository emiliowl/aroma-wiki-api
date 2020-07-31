# -*- coding: utf-8 -*-
import csv
import json
from os import getenv
from os.path import dirname, isfile, join
from dotenv import load_dotenv

from flask_oidc import OpenIDConnect

# a partir do arquivo atual adicione ao path o arquivo .env
_ENV_FILE = join(dirname(__file__), '.env')


# existindo o arquivo faça a leitura do arquivo através da função load_dotenv
if isfile(_ENV_FILE):
    print(f'loading dotenv from file {_ENV_FILE}')
    load_dotenv(dotenv_path=_ENV_FILE)
else:
    print(f'file loading dotenv from file {_ENV_FILE}')


from apps import create_app
app = create_app(getenv('FLASK_ENV') or 'default')
oidc = OpenIDConnect(app)


@app.route('/api/healthcheck')
def alive():
    return 'catalog still breathing...'


@app.route("/api/scents")
@oidc.accept_token(require_token=True)
def get_catalog():
    scents = []
    with open('database.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            from apps.core.models import Aroma
            scents.append(Aroma().build_from_csv(row).to_dict())

    response = {
        'scents': scents
    }

    return json.dumps(response)


if __name__ == '__main__':
    ip = '0.0.0.0'
    port = app.config['APP_PORT']
    debug = app.config['DEBUG']

    app.run(host=ip, debug=debug, port=port, use_reloader=debug)
