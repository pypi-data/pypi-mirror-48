#  Copyright 2018 Ocean Protocol Foundation
#  SPDX-License-Identifier: Apache-2.0

import configparser

from flask import jsonify
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint

from aquarius.app.assets import assets
from aquarius.config import Config
from aquarius.constants import BaseURLs, Metadata
from aquarius.myapp import app

config = Config(filename=app.config['CONFIG_FILE'])
aquarius_url = config.aquarius_url


def get_version():
    conf = configparser.ConfigParser()
    conf.read('.bumpversion.cfg')
    return conf['bumpversion']['current_version']


@app.route("/")
def version():
    info = dict()
    info['software'] = Metadata.TITLE
    info['version'] = get_version()
    return jsonify(info)


@app.route("/spec")
def spec():
    swag = swagger(app)
    swag['info']['version'] = get_version()
    swag['info']['title'] = Metadata.TITLE
    swag['info']['description'] = Metadata.DESCRIPTION + '`' + aquarius_url + '`.'
    # swag['basePath'] = BaseURLs.BASE_AQUARIUS_URL
    return jsonify(swag)


# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    BaseURLs.SWAGGER_URL,
    aquarius_url + '/spec',
    config={  # Swagger UI config overrides
        'app_name': "Test application"
    },
)

# Register blueprint at URL
app.register_blueprint(swaggerui_blueprint, url_prefix=BaseURLs.SWAGGER_URL)
app.register_blueprint(assets, url_prefix=BaseURLs.ASSETS_URL)

if __name__ == '__main__':
    if isinstance(config.aquarius_url.split(':')[-1], int):
        app.run(host=config.aquarius_url.split(':')[1],
                port=config.aquarius_url.split(':')[-1])
    else:
        app.run()
