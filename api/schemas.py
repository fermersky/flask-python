from flask_marshmallow import Schema
from marshmallow import fields


class CharacterSchema(Schema):
    class Meta:
        fields = ["id", "name", "movie"]

    id = fields.Integer()
    name = fields.String()
    movie = fields.Nested("MovieSchema", exclude=("characters",))


class MovieSchema(Schema):
    class Meta:
        fields = ["id", "title", "characters"]

    id = fields.Integer()
    title = fields.String()
    characters = fields.List(fields.Nested(CharacterSchema(exclude=("movie",))))
