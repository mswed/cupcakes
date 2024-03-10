"""Flask app for Cupcakes"""
from flask import Flask, render_template, jsonify
from models import db, connect_db, Cupcake
def create_app(database='cupcakes'):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql:///{database}'
    app.config['SECRET_KEY'] = 'I am bob the mighty'

    connect_db(app)

    return app

flask_app = create_app()