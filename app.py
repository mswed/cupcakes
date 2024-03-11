"""Flask app for Cupcakes"""
from flask import Flask, render_template, jsonify, request
from models import db, connect_db, Cupcake


def create_app(database='cupcakes'):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql:///{database}'
    app.config['SECRET_KEY'] = 'I am bob the mighty'

    connect_db(app)

    @app.route('/')
    def get_index():
        return render_template('index.html')
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
        cupcake = Cupcake.query.get_or_404(cid)
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

    @app.route('/api/cupcakes/<int:cid>', methods=['PATCH'])
    def update_cupcake(cid):
        data = request.json
        cupcake = Cupcake.query.get_or_404(cid)
        cupcake.flavor = data.get('flavor', cupcake.flavor)
        cupcake.size = data.get('size', cupcake.size)
        cupcake.rating = data.get('rating', cupcake.rating)
        cupcake.image = data.get('image', cupcake.image)

        db.session.commit()

        return jsonify(cupcake=cupcake.to_dict())

    @app.route('/api/cupcakes/<int:cid>', methods=['DELETE'])
    def delete_cupcake(cid):
        cupcake = Cupcake.query.get_or_404(cid)
        db.session.delete(cupcake)
        db.session.commit()

        return jsonify(message='DELETED')

    return app


flask_app = create_app()
