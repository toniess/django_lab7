from .models import Article
from django.http import Http404
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login


def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})


def create_post(request):
    if not request.user.is_anonymous:
        if request.method == "POST":
            form = {
                'text': request.POST["text"], 'title': request.POST["title"]
            }
            if form["text"] and form["title"]:
                try:
                    if Article.objects.get(title=form["title"]):
                        form['errors'] = u"Такой заголовок уже сущестует"
                        return render(request, 'create_post.html', {'form': form})
                except Article.DoesNotExist:
                    Article.objects.create(text=form["text"], title=form["title"], author=request.user)
                    return redirect('/', article_id='article.id')
                    # return redirect('get_article', article_id='article.id')
            else:
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'create_post.html', {'form': form})
        else:
            return render(request, 'create_post.html', {})
    else:
        raise Http404


def registration(request):
    if request.method == 'POST':
        form = {
            'username': request.POST["username"],
            'password': request.POST["password"],
            'email': request.POST["email"]
        }
        if len(form["username"]) >= 4 and len(form["password"]) >= 6:
            try:
                if User.objects.get(username=form["username"]) or User.objects.get(email=form["email"]):
                    form['errors'] = u"Такой логин или почта уже существует"
                    return render(request, 'registration.html', {'form': form})
            except User.DoesNotExist:
                User.objects.create_user(form["username"], form["email"], form["password"])
                return redirect('/')
        else:
            form['errors'] = u"Логин должен содержать более 3 символов, а пароль более 5"
            return render(request, 'registration.html', {'form': form})
    else:
        return render(request, 'registration.html', {})


def authorisation(request):
    if request.method == 'POST':
        form = {
            'username': request.POST["username"],
            'password': request.POST["password"],
        }
        user = authenticate(username=form['username'], password=form['password'])

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            form['errors'] = u"Неверный логин или пароль"
            return render(request, 'authorisation.html', {'form': form})
    else:
        return render(request, 'authorisation.html', {})


def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404

