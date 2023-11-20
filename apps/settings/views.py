from django.shortcuts import render, redirect
from .models import Settings, Slider, History, Restaurant, Days, Special, Special_foods, Menu, Lunch, Dinner, Dessert, Drinks, Reservetion, Command, Commands, Opit, Blog
def index(request):
    settings = Settings.objects.latest('id')
    slider = Slider.objects.all()
    history = History.objects.latest('id')
    restaurant = Restaurant.objects.latest('id')
    days = Days.objects.all()
    special = Special.objects.latest('id')
    special_foods = Special_foods.objects.all()
    menu = Menu.objects.latest('id')
    lunch = Lunch.objects.all()
    dinner = Dinner.objects.all()
    dessert = Dessert.objects.all()
    drinks = Drinks.objects.all()
    reservetion = Reservetion.objects.latest('id')
    command = Command.objects.latest('id')
    commands = Commands.objects.all()
    opit = Opit.objects.all()
    # if request.method == "POST":
    #     name = request.POST.get("name-guest")
    #     date_guest = request.POST.get("date-guest")
    #     time_guest = request.POST.get("time_guest")
    #     pers_guest = request.POST.get("pers_guest")
    #     Reservetion.objects.create(name = name, date_guest = date_guest, time_guest = time_guest, pers_guest = pers_guest)
    #     return redirect('index')
    return render(request, 'index.html', locals())

def blog(request):
    blog = Blog.objects.all()
    return render(request, 'blog.html', locals())