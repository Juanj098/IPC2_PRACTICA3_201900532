from flask import Flask, request,jsonify
from flask_cors import CORS
from movies import Movies
import json

movies = []

mov =  Movies(1,'Deadpool','Heroes')
movies.append(mov)
movies_Json = []

app = Flask(__name__)

CORS(app)

@app.route('/ping')
def index():
    return jsonify({'Request':'pong'})

@app.route('/api/new-movie', methods = ['POST'])
def Nmovie():
    print(request.json)
    id = request.json['id']
    name = request.json['name']
    genre = request.json['genre']
    newMovie = Movies(id,name,genre)
    movies.append(newMovie)
    return jsonify({'info':'recibido'})

@app.route('/api/all-movies', methods = ['GET'])
def enlist_Movies():
    movies_Json.clear()
    return jsonify({'Movies':[movie.__dict__ for movie in movies]})

@app.route('/api/all-movies-by-genre/<string:genre>', methods = ['GET'])
def byGenre(genre):
        movies_Json.clear()
        for movie in movies:
            if movie.genre == genre:
                  movies_Json.append(movie)
        return jsonify({'movies':[moviej.__dict__ for moviej in movies_Json]})

@app.route('/api/modify-movie/<string:name_movie>', methods = ['POST'])
def modMovie(name_movie):
    found_movie = None
    for movie in movies:
        if movie.name == name_movie:
            found_movie = movie
            break

    if found_movie is not None:
        found_movie.id = request.json['id']
        found_movie.name = request.json['name']
        found_movie.genre = request.json['genre']
        return jsonify({'mensaje':'Actualizado','pelicula':found_movie.__dict__})
    else:
        return jsonify({'info':'Pelicula no encontrada'})
 
if __name__ =='__main__':
    app.run(debug=True,port=4500)
