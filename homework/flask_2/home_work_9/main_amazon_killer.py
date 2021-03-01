from flask import Flask
from amazon_killer import amazon_killer


main_amazon_killer = Flask(__name__)

main_amazon_killer.register_blueprint(amazon_killer)

