from tortoise.models import Model
from tortoise import fields

class Movie(Model):
    uuid = fields.UUIDField(pk=True)
    imdbID = fields.CharField(max_length=255, unique=True)
    Title = fields.CharField(max_length=255)
    Year = fields.CharField(max_length=255)
    Type =  fields.CharField(max_length=255)
    Poster = fields.CharField(max_length=255)
    created_at = fields.CharField(max_length=255)
    posts: fields.ReverseRelation["Post"]

    def __str__(self):
        return f'\tIMDB: {self.imdbID}\n\tTitle={self.Title!r}\n\tYear={self.Year}\n\tType={self.Type}\n'