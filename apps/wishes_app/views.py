from django.shortcuts import render, redirect, reverse
# from .models import Travel
from django.contrib import messages
from .models import Wish
from ..loginreg_app.models import User

# Create your views here.

def flash_errors(errors, request):
    for error in errors:
        messages.error(request, error)

def wishes(request):
    user = User.objects.current_user(request)

    wishes = user.wishes.all()
    other_wishes = Wish.objects.exclude(id__in=wishes)

    context = {
        'user':current_user(request),
        'wishes': wishes,
        'other_wishes':other_wishes


    }
    return render(request, 'wishes_app/wishes.html', context)
    return redirect(reverse('landing'))

def current_user(request):
    return User.objects.get(id = request.session['user_id'])

def add(request):
    if 'user_id' in request.session:
        context = {
            'user':current_user(request)
        }
    #
    print "******************ADD Item *************************"
    return render(request, 'wishes_app/add.html')

def create(request):
    if request.method == "POST":
        #validate
        errors = Wish.objects.validate(request.POST)
        if not errors:
            #get current user
            user = User.objects.current_user(request)
            #create the trip
            item = Wish.objects.create_wish(request.POST, user)
            #redirect to dashboard
            return redirect(reverse('dashboard'))
        #flash errors
        flash_errors(request,errors)
    return redirect(reverse('add_wish'))


def add_wish_item(request, id):
    user = User.objects.current_user(request)

    wish = Wish.objects.filter(id=id).first()

    if wish:
        user.wishes.add(wish)
    return redirect(reverse('dashboard'))

def remove_wish_item(request, id):
    user = User.objects.current_user(request)

    wish = Wish.objects.filter(id=id).first()

    if wish:
        user.items.remove(wish)
        #doesn't work for me... the .remove
    return redirect(reverse('dashboard'))

def delete_wish(request, id):
    user = User.objects.current_user(request)

    wish = Wish.objects.filter(id=id).first()
    if wish and user == user.items:
        wish.delete()
    return redirect(reverse('dashboard'))


def wish_item(request,id):
    context = {
        'wisher' : Wish.objects.get(id=id),
    }
    return render(request, 'wishes_app/wish_item.html', context)
