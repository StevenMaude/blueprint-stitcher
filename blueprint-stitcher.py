#!/usr/bin/env python
# encoding: utf-8
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
import os
import importlib
from flask import Flask

flask_app = Flask('blueprint-stitcher')

blueprint_names = [f for f in os.listdir('blueprint')
                   if os.path.isdir(os.path.join('blueprint', f))]

for blueprint_name in blueprint_names:
    module_name = "blueprint.{0}.app.{0}".format(blueprint_name)
    module = importlib.import_module(module_name)
    blueprint = getattr(module, blueprint_name)
    flask_app.register_blueprint(blueprint, url_prefix='/' + blueprint_name)

flask_app.run()
