import csv
import json
from flask import Blueprint
from api import global_info
from apps.core.models import Aroma


oidc = global_info["oidc"]
bp = Blueprint('scents', __name__)


@bp.route("/")
@oidc.accept_token(require_token=True)
def get_catalog():
    scents = []
    with open('database.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            scents.append(Aroma().build_from_csv(row).to_dict())

    response = {
        'scents': scents
    }

    return json.dumps(response)
