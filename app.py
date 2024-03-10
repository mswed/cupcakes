"""Flask app for Cupcakes"""
from flask import Flask, render_template, jsonify, request
from models import db, connect_db, Cupcake
def create_app(database='cupcakes'):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql:///{database}'
    app.config['SECRET_KEY'] = 'I am bob the mighty'

    connect_db(app)

    @app.route('/api/cupcakes')
    def list_cupcakes():
        """
        Get a json with all the cupcakes in the database
        Returns: json, list of cupcakes
        """

        cupcakes = [cc.to_dict() for cc in Cupcake.query.all()]
        return jsonify(cupcakes=cupcakes)

    @app.route('/api/cupcakes/<int:cid>')
    def get_cupcake(cid):
        cupcake = Cupcake.query.get(cid)
        return jsonify(cupcake=cupcake.to_dict())

    @app.route('/api/cupcakes', methods=['POST'])
    def create_cupcake():
        data = request.json
        new_cupcake = Cupcake(flavor=data.get('flavor'),
                              size=data.get('size'),
                              rating=data.get('rating'),
                              image=data.get('image'))
        db.session.add(new_cupcake)
        db.session.commit()

        return (jsonify(cupcake=new_cupcake.to_dict()), 201)
    return app


flask_app = create_app()
