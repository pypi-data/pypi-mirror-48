#!/usr/bin/env python3
# coding: utf-8

from __future__ import division, print_function

import os
from os.path import split, splitext

import flask


def _create_flaskapp(contextmap, **flask_params):
    """
    :param contextmap: a dict-like obj
    :param flask_params: (dict)
    :return: (flask.Flask)
    """
    app = flask.Flask(**flask_params)
    _gl = contextmap.pop('_global', {})

    for ctx in contextmap.values():
        ctx.update({k: v for k, v in _gl.items() if k not in ctx})

    @app.route('/<path:path>')
    def render(path):
        name, ext = splitext(path)
        if ext and ext != '.html':
            return flask.abort(404)
        try:
            context = contextmap[name]
            template_path = context['_prot'] + '.html'
        except KeyError:
            return flask.abort(404)
        return flask.render_template(template_path, **context)

    app.route('/')(lambda: render('index'))
    return app


def create_flaskapp(package, contextmap, static_folder=None):
    flask_params = {
        'root_path': split(package.__file__)[0],
        'import_name': package.__name__,
        'static_url_path': '/static',
    }
    if static_folder:
        flask_params['static_folder'] = static_folder
    return _create_flaskapp(contextmap, **flask_params)


def create_flat_flaskapp(root_path, contextmap):
    if os.path.isfile(root_path):
        root_path = split(root_path)[0]

    flask_params = {
        'root_path': root_path,
        'import_name': __name__,
    }
    return _create_flaskapp(contextmap, **flask_params)
