from app import db


class Movie(db.Model):
    __tablename__ = "movies"

    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column("title", db.Text)

    def __init__(self, title) -> None:
        """
        Initialize the movie with the title given.
        @param title - the title of the movie
        """
        self.title = title

    def __repr__(self) -> str:
        """
        Return a string representation of the movie and its characters
        @returns the string representation of the movie.
        """
        return f"Movie {self.title} with characters {[c.name for c in self.characters]}"


class Character(db.Model):
    __tablename__ = "characters"

    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.Text)

    movie_id = db.Column(db.Integer, db.ForeignKey("movies.id"))
    movie = db.relationship("Movie", backref="characters", lazy=True)

    def __init__(self, name, movie) -> None:
        """
        Initialize the class with the name and movie title.
        @param name - the name of the movie
        @param movie - the movie itself
        """
        self.name = name
        self.movie = movie

    def __repr__(self) -> str:
        """
        The __repr__ function for the Character class. It returns a string that is the character's name and movie title.
        @returns the string
        """
        """"""
        return f"Character {self.name} of movie {self.movie.title}"
