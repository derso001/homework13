from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Quote, Tag, Author
from .forms import QuoteForm, AuthorForm, TagForm

def main(request):
    quotes =  Quote.objects.all()
    context = {"quotes":quotes}

    return render(request, 'quoteapp/index.html', context)

def quotes_by_tag(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    quotes = Quote.objects.filter(tags=tag)
    context = {"quotes": quotes, "tag": tag}
    
    return render(request, 'quoteapp/index.html', context)

def detail_author(request, author):
    author_inf = get_object_or_404(Author, fullname=author)
    return render(request, 'quoteapp/authorinfo.html', {"author": author_inf})

@login_required
def quote(request):
    tags = Tag.objects.all()
    authors = Author.objects.all()

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save(commit=False)
            # new_quote.user = request.user
            new_quote.save()

            choice_author = Author.objects.filter(fullname__in=request.POST.getlist('author'))
            for author in choice_author.iterator():
                new_quote.author = author

            choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'))
            for tag in choice_tags.iterator():
                new_quote.tags.add(tag)

            new_quote.save()


            return redirect(to='quoteapp:main')
        else:
            return render(request, 'quoteapp/quote.html', {"tags": tags,"authors":authors, 'form': form})

    return render(request, 'quoteapp/quote.html', {"tags": tags, "authors":authors, 'form': QuoteForm()})

@login_required
def tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quoteapp:main')
        else:
            return render(request, 'quoteapp/tag.html', {'form': form})

    return render(request, 'quoteapp/tag.html', {'form': TagForm()})

@login_required
def author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            if not Author.objects.filter(fullname=form.cleaned_data['fullname']).exists():
                form.save()
                return redirect(to='quoteapp:main')
            else:
                return render(request, 'quoteapp/author.html', {'form': form})

    return render(request, 'quoteapp/author.html', {'form': AuthorForm()})
