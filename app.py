import os
from flask import Flask, request, abort, jsonify,Response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import exc
import json
from auth import AuthError, requires_auth
from models import *
from datetime import *

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

  '''
  @TODO: Use the after_request decorator to set Access-Control-Allow
  '''
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,PATCH,POST,DELETE,OPTIONS')
    return response




  @app.route('/actros')
  @requires_auth('get:actros')
  def actor_details(jwt_token):
    actros = Actor.query.all()

    try:
      return jsonify({"success": True, "actros_info": [actor.format() for actor in actros]})
    except:
      print(sys.exc_info())
      abort(404)

      




  @app.route('/movie')
  @requires_auth('get:movie')
  def movie_details(jwt_token):
    movies = Movie.query.all()
    try:
      return jsonify({"success": True, "movies_info": [movie.format() for movie in movies]})
    except:
      print(sys.exc_info())
      abort(404)




  @app.route('/actros/<id>' ,methods=['DELETE'])
  @requires_auth('delete:actros')
  def remvoe_actro(jwt_token,id):
    actor = Actor.query.get(id)
    if actor is None:
      abort(404)
    try:
      actor.delete()
      return jsonify({"success": True, "delete": id})
    except:
      print(sys.exc_info())
      abort(422)




  @app.route('/movie/<id>' ,methods=['DELETE'])
  @requires_auth('delete:movie')
  def remvoe_movie(jwt_token,id):
    movie = Movie.query.get(id)
    if movie is None:
      abort(404)
    try:
      movie.delete()
      return jsonify({"success": True, "delete": id})
    except:
      print(sys.exc_info())
      abort(422)




  @app.route("/actros", methods=['POST'])
  @requires_auth('post:actros')
  def new_actro(jwt_token):
    body = request.get_json()
    new_name = body.get('name')
    new_age = body.get('age')
    new_gender = body.get('gender')

    try:
      new_actros = Actor(name = new_name , age = new_age , gender = new_gender)
      new_actros.insert()

      return jsonify({"success": True, "actros_info": [new_actros.format()]})

    except:
      print(sys.exc_info())
      abort(422)




  @app.route("/movie", methods=['POST'])
  @requires_auth('post:movie')
  def new_movie(jwt_token):
    body = request.get_json()
    new_title = body.get('title')
    new_date = body.get('release_date')

    try:
      new_movie = Movie(title = new_title , release_date=new_date)
      new_movie.insert()

      return jsonify({"success": True, "movies_info": [new_movie.format()]})

    except:
      print(sys.exc_info())
      abort(422)




  @app.route('/actros/<id>', methods=['PATCH'])
  @requires_auth('patch:actros')
  def edit_actros(jwt_token,id):
    actro = Actor.query.get(id)
    if actro is None:
      abort(404)
    else:
      try:
        body = request.get_json()
        edit_name = body.get('name')

        if edit_name:
          actro.name =  edit_name

        edit_age = body.get('age')

        if edit_age:
          actro.age = edit_age

        edit_gender = body.get('gender')

        if edit_gender:
          actro.gender = edit_gender

        actro.update()

        return jsonify({"success": True, "Actor_info": [actro.format()]})

      except:
        abort(422)




  @app.route('/movie/<id>', methods=['PATCH'])
  @requires_auth('patch:movie')
  def edit_movie(jwt_token,id):
    movie = Movie.query.get(id)
    if movie is None:
      abort(404)
    else:
      try:
        body = request.get_json()
        edit_title = body.get('title')

        if edit_title:
          movie.title =  edit_title

        edit_date = body.get('release_date')

        if edit_date:
          movie.release_date = edit_date

        movie.update()

        return jsonify({"success": True, "movie_info": [movie.format()]})

      except:
        abort(422)




  @app.errorhandler(404)
  def not_found(error):
      return jsonify({
          "success": False, 
          "error": 404,
          "message": "resource not found"
          }), 404




  @app.errorhandler(400)
  def bad_request(error):
      return jsonify({
          "success": False, 
          "error": 400,
          "message": "bad request"
          }), 400




  @app.errorhandler(AuthError)
  def auth_error_handler(e):
      return jsonify({
          "success": False, 
          "error": e.status_code,
          "message": e.error
          }), e.status_code




  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      "success": False, 
      "error": 422,
      "message": "unprocessable"
      }), 422



  return app

app = create_app()

if __name__ == '__main__':
  app.run()