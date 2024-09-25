import mongoengine
from mongoengine import ReferenceField, Document
from mongoengine.fields import ListField, StringField
from mongoengine import connect
from quoteapp.models import Author as SQLAuthor, Quote as SQLQuote, Tag as SQLTag


uri = "mongodb+srv://boris:test123@cluster0.1lmlx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
connect(host=uri, ssl=True)
print(1)
class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField()
    born_location = StringField()
    description= StringField()

class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author, reverse_delete_rule=2)  
    quote = StringField(required=True)