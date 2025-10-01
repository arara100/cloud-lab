from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Жанри
class Genre(db.Model):
    __tablename__ = "Genre"
    genre_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

# Лейбли
class Label(db.Model):
    __tablename__ = "Label"
    label_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    country = db.Column(db.String(100))

# Автори
class Author(db.Model):
    __tablename__ = "Author"
    author_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150), nullable=False)
    country = db.Column(db.String(100))
    birth_date = db.Column(db.Date)

# Альбоми
class Album(db.Model):
    __tablename__ = "Album"
    album_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    release_year = db.Column(db.Integer)
    label_id = db.Column(db.Integer, db.ForeignKey("Label.label_id"))

# Пісні
class Song(db.Model):
    __tablename__ = "Song"
    song_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Numeric(6,2), nullable=False, default=0.00)
    downloads_count = db.Column(db.Integer, default=0)
    genre_id = db.Column(db.Integer, db.ForeignKey("Genre.genre_id"))
    album_id = db.Column(db.Integer, db.ForeignKey("Album.album_id"))

# Багато-до-багатьох: Пісні ↔ Автори
SongAuthor = db.Table("SongAuthor",
    db.Column("song_id", db.Integer, db.ForeignKey("Song.song_id"), primary_key=True),
    db.Column("author_id", db.Integer, db.ForeignKey("Author.author_id"), primary_key=True)
)

# Користувачі
class User(db.Model):
    __tablename__ = "User"
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    registration_date = db.Column(db.Date)

# Завантаження користувачами
class UserDownload(db.Model):
    __tablename__ = "UserDownload"
    user_id = db.Column(db.Integer, db.ForeignKey("User.user_id"), primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey("Song.song_id"), primary_key=True)
    download_date = db.Column(db.DateTime)
