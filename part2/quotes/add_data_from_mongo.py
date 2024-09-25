import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quotes.settings')

django.setup()

import mongoengine
from mongoengine import connect
from quoteapp.models import Author as SQLAuthor, Quote as SQLQuote, Tag as SQLTag
from mongo_models import Author as MongoAuthor, Quote as MongoQuote

uri = "mongodb+srv://boris:test123@cluster0.1lmlx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
connect(host=uri, ssl=True)

for mongo_author in MongoAuthor.objects:
    
    sql_author, created = SQLAuthor.objects.get_or_create(
        fullname=mongo_author.fullname,
        defaults={
            'born_date': mongo_author.born_date,
            'born_location': mongo_author.born_location,
            'description': mongo_author.description,
        }
    )
    print(f"add {mongo_author.fullname}")

for mongo_quote in MongoQuote.objects:
    sql_author = SQLAuthor.objects.get(fullname=mongo_quote.author.fullname)
    if not SQLQuote.objects.filter(quote=mongo_quote.quote, author=sql_author).exists():
        sql_quote = SQLQuote.objects.create(
            quote=mongo_quote.quote,
            author=sql_author,
        )
        for tag_name in mongo_quote.tags:
            tag, created = SQLTag.objects.get_or_create(name=tag_name)
            sql_quote.tags.add(tag)
            print(1)
    

