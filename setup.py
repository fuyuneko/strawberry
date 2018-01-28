from setuptools import setup

setup(
    name='strawberry',
    version='0.0.1',
    description='Theme for Sphinx',

    packages=['strawberry'],
    package_data={'strawberry': [
        'theme.conf',
        '*.html',
        'static/css/*.css'
    ]},
    include_package_data=True,

    entry_points = {
        'sphinx.html_themes': [
            'strawberry = strawberry'
        ]
    }
)
