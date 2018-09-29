from django.shortcuts import render, HttpResponse, redirect
from .models import *
import bcrypt
from django.contrib import messages
import re

def logreg(request):
    if "first_name" in request.session:
        request.session['first_name'] = None
    if "id" in request.session:
        request.session['id'] = None
    return render(request, 'belt/logreg.html')

def registration(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value, extra_tags=key)
            return redirect('/')
        else:
            user_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], hash_pw=user_hash)
            curr_user = User.objects.last()
            request.session['id'] = curr_user.id
            request.session['first_name'] = curr_user.first_name
            return redirect('/main')
    return redirect('/')

def login(request):
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value, extra_tags=key)
            return redirect('/')
        else:
            curr_user = User.objects.get(email=request.POST['email'])
            request.session['id'] = curr_user.id
            request.session['first_name'] = curr_user.first_name
            return redirect('/main')
    return redirect('/')

def main(request):
    if request.session['first_name'] == None:
        return redirect('/')
    group = Review.objects.all()
    last = group[:3]
    context = {
        "review": Book.objects.all(),
        "latest": last
    }
    return render(request, 'belt/main.html', context)

def new_book(request):
    return render(request, 'belt/add.html')

def show(request, book_id):
    latest = Book.objects.get(id=book_id)
    print(latest)
    request.session['count'] = 0
    context = {
         "book": Book.objects.last(),
         "reviews": Review.objects.filter(book = Book.objects.last()),
    }
    return render(request, 'belt/book.html', context)

def add_both(request):
    curr_user = User.objects.get(id = request.session['id'])
    curr_book = Book.objects.create(title = request.POST['title'], author = request.POST['author'], user = curr_user)
    curr_review = Review.objects.create(text = request.POST['review'], stars = request.POST['rating'], user = curr_user, book = curr_book)
    book_id = curr_book.id
    return redirect('/show/'+str(book_id))

def add_review(request, book_id):
    curr_user = User.objects.get(id = request.session['id'])
    curr_book = Book.objects.get(id = book_id)
    curr_review = Review.objects.create(text = request.POST['review'], stars = request.POST['rating'], user = curr_user, book = curr_book)
    return redirect('/show/'+str(book_id))

def delete(request, review_id, book_id):
    curr_review = Review.objects.get(id = review_id)
    curr_review.delete()
    return redirect('/show/'+str(book_id))

def user(request, user_id):
    curr_user = User.objects.get(id = user_id)
    total = len(curr_user.user_reviews.all())
    reviews = Review.objects.filter(user_id = user_id)
    obj = {}
    arr = []
    for i in reviews:
        arr.append(i.book_id)
    for i in arr:
        if i not in obj:
            obj[i] = i
    boo={}
    for i in obj:
        boo[i] = Book.objects.get(id = i)
    context = {
        "user": curr_user,
        "count": total,
        "num": boo,
        "books": Book.objects.all()
    }
    return render(request, 'belt/user.html', context)
 
