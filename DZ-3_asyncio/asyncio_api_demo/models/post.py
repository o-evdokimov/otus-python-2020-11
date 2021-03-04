from tortoise.models import Model
from tortoise import fields

class Post(Model):
    id = fields.IntField(pk=True)
    #movie_id = fields.ForeignKeyField("models.Movie", related_name="imdbID")
    author = fields.CharField(max_length=255)
    title = fields.CharField(max_length=255)
    text = fields.CharField(max_length=255)
    created_at = fields.CharField(max_length=255)
    movie: fields.ForeignKeyRelation["Movie"] = fields.ForeignKeyField("models.Movie", related_name="posts")

    def __str__(self):
        return f'\tPost: {self.title!r}\n\tAuthor: {self.author}\n\t\t{self.text!r}\n'