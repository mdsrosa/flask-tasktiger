"""
Flask-TaskTiger
--------------

TaskTiger integration for Flask.
"""
from setuptools import setup

version = '0.0.1'

setup(
    name='Flask-TaskTiger',
    version=version,
    url='https://github.com/mdsrosa/flask-tasktiger',
    license='MIT',
    author='Matheus Rosa',
    author_email='matheusdsrosa@gmail.com',
    description='TaskTiger integration for Flask',
    py_modules=['flask_tasktiger'],
    zip_safe=False,
    include_package_data=False,
    platforms='any',
    install_requires=[
        'Flask',
        'tasktiger'
    ],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
