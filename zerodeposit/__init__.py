# zerodeposit/__init__.py
import os, json

from flask import Flask, render_template
import requests

api_id = '5c751c10f87e432abd3ecffb85ebee19'
def get_current_rates():
    """Query the openexchangerates API to gather the current Euro/Pound and return it"""
    r = requests.get('https://openexchangerates.org/api/latest.json?app_id=%s'%(api_id))
    data = r.json()
    
    usdToEur = data['rates']['EUR']
    usdToGbp = data['rates']['GBP']
    
    gbpToEur = usdToEur/usdToGbp
    
    return gbpToEur


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    
    # Render number of blocks
    @app.route('/')
    def number_of_blocks():
        """ Render the maximum amount of cheese blocks to be included in an order to still make a profit taking into account the current Euro/Pound exchange rate"""
        
        gbpToEur = get_current_rates()
        
        gbpAmount = 19.99 * gbpToEur
        
        numberOfBlock = int(gbpAmount / 3.24)

        return render_template('index.html', numberOfBlock=numberOfBlock)

    return app