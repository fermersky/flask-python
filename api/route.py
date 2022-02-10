from flask import Blueprint, jsonify, request
from api.models import Character, Movie
from api.schemas import MovieSchema, CharacterSchema
from app import db


api = Blueprint("api", __name__, url_prefix="/")


@api.route("movies", methods=["GET"])
def movies():
    print(request.method)
    # movie = Movie('Star Wars')
    # character = Character('R2D2', movie)

    # db.session.add(movie)
    # db.session.add(character)
    # db.session.commit()

    movieSchema = MovieSchema(many=True)
    # characterSchema = CharacterSchema(many=True)

    # movies = Movie.query.options(joinedload('characters'))

    # result = db.session.query(Movie, Character).join(Character, Movie.id == Character.movie_id).all()
    # movies = [tup[0] for tup in result]

    # print(Movie.query.all()[0].characters[0].name)

    movies = Movie.query.all()
    # characters = Character.query.all()
    # print(movies.characters[0])

    # return jsonify(movieSchema.dump(movies))
    return jsonify(movieSchema.dump(movies))
