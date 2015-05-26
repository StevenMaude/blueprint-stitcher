#!/usr/bin/env python
# encoding: utf-8
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
import os
import importlib
from app import flask_app

blueprint_names = [f for f in os.listdir('app/blueprint')
                   if os.path.isdir(os.path.join('app/blueprint', f))]

for blueprint_name in blueprint_names:
    module_name = "app.blueprint.{0}.{0}".format(blueprint_name)
    module = importlib.import_module(module_name)
    blueprint = getattr(module, blueprint_name)
    flask_app.register_blueprint(blueprint, url_prefix='/' + blueprint_name)

flask_app.run()
