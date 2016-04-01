from flask.ext.assets import Environment, Bundle

from app import app


assets = Environment(app)
assets.url = app.static_url_path

bundles = {
    'scss_compiled': Bundle(
        'scss/left-button.scss',
        'scss/right-button.scss',
        filters='pyscss',
        output='gen/refunite.css'),

    'css_minified': Bundle(
        'css/bootstrap.min.css',
        'css/style.css',
        filters='cssmin',
        output='gen/refunite_global.css'),

    'js_minified': Bundle(
        'js/jquery-1.12.0.min.js',
        'js/bootstrap.min.js',
        'js/right-button.js',
        'js/left-button.js',
        filters='rjsmin',
        output='gen/refunite.min.js'),
}

assets.register(bundles)
