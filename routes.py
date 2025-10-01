from flask import Blueprint, request, jsonify
from models import db, Song, Author, Album, Genre, Label, User, UserDownload, SongAuthor
from datetime import datetime

api = Blueprint("api", __name__)

# ----------------- SONG -----------------
@api.route("/songs", methods=["GET"])
def get_songs():
    songs = Song.query.all()
    return jsonify([{
        "id": s.song_id,
        "title": s.title,
        "price": float(s.price),
        "downloads": s.downloads_count,
        "genre_id": s.genre_id,
        "album_id": s.album_id
    } for s in songs])

@api.route("/songs/<int:song_id>", methods=["GET"])
def get_song(song_id):
    s = Song.query.get_or_404(song_id)
    return jsonify({"id": s.song_id, "title": s.title, "price": float(s.price)})

@api.route("/songs", methods=["POST"])
def add_song():
    data = request.json
    song = Song(title=data["title"], price=data.get("price", 0.0),
                genre_id=data.get("genre_id"), album_id=data.get("album_id"))
    db.session.add(song)
    db.session.commit()
    return jsonify({"message": "Song added", "id": song.song_id})

@api.route("/songs/<int:song_id>", methods=["PUT"])
def update_song(song_id):
    song = Song.query.get_or_404(song_id)
    data = request.json
    song.title = data.get("title", song.title)
    song.price = data.get("price", song.price)
    song.genre_id = data.get("genre_id", song.genre_id)
    song.album_id = data.get("album_id", song.album_id)
    db.session.commit()
    return jsonify({"message": "Song updated"})

@api.route("/songs/<int:song_id>", methods=["DELETE"])
def delete_song(song_id):
    song = Song.query.get_or_404(song_id)
    db.session.delete(song)
    db.session.commit()
    return jsonify({"message": "Song deleted"})


# ----------------- AUTHOR -----------------
@api.route("/authors", methods=["GET"])
def get_authors():
    authors = Author.query.all()
    return jsonify([{"id": a.author_id, "name": a.name, "country": a.country} for a in authors])

@api.route("/authors", methods=["POST"])
def add_author():
    data = request.json
    author = Author(name=data["name"], country=data.get("country"))
    db.session.add(author)
    db.session.commit()
    return jsonify({"message": "Author added", "id": author.author_id})

@api.route("/authors/<int:author_id>", methods=["PUT"])
def update_author(author_id):
    author = Author.query.get_or_404(author_id)
    data = request.json
    author.name = data.get("name", author.name)
    author.country = data.get("country", author.country)
    db.session.commit()
    return jsonify({"message": "Author updated"})

@api.route("/authors/<int:author_id>", methods=["DELETE"])
def delete_author(author_id):
    author = Author.query.get_or_404(author_id)
    db.session.delete(author)
    db.session.commit()
    return jsonify({"message": "Author deleted"})


# ----------------- ALBUM -----------------
@api.route("/albums", methods=["GET"])
def get_albums():
    albums = Album.query.all()
    return jsonify([{"id": a.album_id, "title": a.title, "year": a.release_year} for a in albums])

@api.route("/albums", methods=["POST"])
def add_album():
    data = request.json
    album = Album(title=data["title"], release_year=data.get("release_year"), label_id=data.get("label_id"))
    db.session.add(album)
    db.session.commit()
    return jsonify({"message": "Album added", "id": album.album_id})

@api.route("/albums/<int:album_id>", methods=["PUT"])
def update_album(album_id):
    album = Album.query.get_or_404(album_id)
    data = request.json
    album.title = data.get("title", album.title)
    album.release_year = data.get("release_year", album.release_year)
    album.label_id = data.get("label_id", album.label_id)
    db.session.commit()
    return jsonify({"message": "Album updated"})

@api.route("/albums/<int:album_id>", methods=["DELETE"])
def delete_album(album_id):
    album = Album.query.get_or_404(album_id)
    db.session.delete(album)
    db.session.commit()
    return jsonify({"message": "Album deleted"})


# ----------------- GENRE -----------------
@api.route("/genres", methods=["GET"])
def get_genres():
    genres = Genre.query.all()
    return jsonify([{"id": g.genre_id, "name": g.name} for g in genres])

@api.route("/genres", methods=["POST"])
def add_genre():
    data = request.json
    genre = Genre(name=data["name"])
    db.session.add(genre)
    db.session.commit()
    return jsonify({"message": "Genre added", "id": genre.genre_id})

@api.route("/genres/<int:genre_id>", methods=["PUT"])
def update_genre(genre_id):
    genre = Genre.query.get_or_404(genre_id)
    data = request.json
    genre.name = data.get("name", genre.name)
    db.session.commit()
    return jsonify({"message": "Genre updated"})

@api.route("/genres/<int:genre_id>", methods=["DELETE"])
def delete_genre(genre_id):
    genre = Genre.query.get_or_404(genre_id)
    db.session.delete(genre)
    db.session.commit()
    return jsonify({"message": "Genre deleted"})


# ----------------- LABEL -----------------
@api.route("/labels", methods=["GET"])
def get_labels():
    labels = Label.query.all()
    return jsonify([{"id": l.label_id, "name": l.name, "country": l.country} for l in labels])

@api.route("/labels", methods=["POST"])
def add_label():
    data = request.json
    label = Label(name=data["name"], country=data.get("country"))
    db.session.add(label)
    db.session.commit()
    return jsonify({"message": "Label added", "id": label.label_id})

@api.route("/labels/<int:label_id>", methods=["PUT"])
def update_label(label_id):
    label = Label.query.get_or_404(label_id)
    data = request.json
    label.name = data.get("name", label.name)
    label.country = data.get("country", label.country)
    db.session.commit()
    return jsonify({"message": "Label updated"})

@api.route("/labels/<int:label_id>", methods=["DELETE"])
def delete_label(label_id):
    label = Label.query.get_or_404(label_id)
    db.session.delete(label)
    db.session.commit()
    return jsonify({"message": "Label deleted"})


# ----------------- USER -----------------
@api.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([{"id": u.user_id, "username": u.username, "email": u.email} for u in users])

@api.route("/users", methods=["POST"])
def add_user():
    data = request.json
    user = User(username=data["username"], email=data["email"], registration_date=datetime.now())
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User registered", "id": user.user_id})

@api.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.json
    user.username = data.get("username", user.username)
    user.email = data.get("email", user.email)
    db.session.commit()
    return jsonify({"message": "User updated"})

@api.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted"})


# ----------------- DOWNLOADS -----------------
@api.route("/downloads", methods=["GET"])
def get_downloads():
    downloads = UserDownload.query.all()
    return jsonify([{
        "user_id": d.user_id,
        "song_id": d.song_id,
        "date": d.download_date
    } for d in downloads])

@api.route("/downloads", methods=["POST"])
def add_download():
    data = request.json
    download = UserDownload(user_id=data["user_id"], song_id=data["song_id"], download_date=datetime.now())
    db.session.add(download)

    song = Song.query.get(data["song_id"])
    song.downloads_count += 1

    db.session.commit()
    return jsonify({"message": "Download saved"})
