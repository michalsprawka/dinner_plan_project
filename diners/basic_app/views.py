from django.shortcuts import render
from basic_app.models import Dinners, DinnersDate
from . import forms
from datetime import date,timedelta

from django.contrib import messages
from django.http import JsonResponse

# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required




def index(request):
    return render(request,'basic_app/index.html')

def addDinnersShow(request):
    #messages.error(request, 'Three credits remain in your account.')
    dinners = Dinners.objects.all()
    if request.user.is_authenticated:
        print(request.user.pk)
        print(request.user.username)
        print(request.user.email)
    else:
        print("nie ma usera")
    return render(request,'basic_app/addDinnersShow.html',{'dinns':dinners})

def DinnerDateShow(request):
    dinners = DinnersDate.objects.filter(date__gte=date.today()).order_by('date')
    #print(request.session['test'])
    return render(request,'basic_app/dinnersDateShow.html',{'dinns':dinners})
def DinnerChoice(request):
    form = forms.formDaysChoice()
    if request.method == "POST":
        form = forms.formDaysChoice(request.POST)
        if form.is_valid():
            d= form.cleaned_data['days']
            print(d)
            return HttpResponseRedirect(reverse("index"))
    return render(request,'basic_app/dayschoice.html',{'form':form})

def DinnersDelete(request,number):
    obj=DinnersDate.objects.get(pk=number)
    obj.delete()
    return HttpResponseRedirect(reverse('basic_app:dds'))

#FOR Ajax
def validate_dinner(request):
    is_taken=False
    #dinner = request.GET.get('dinner', None)
    date = request.GET.get('date', None)
    #d=DinnersDate.objects.filter(date=date)
    #if d:
    #    print(d[0].din.dinners)
    #    print(dinner)
    #    if d[0].din.dinners==dinner:
    #        is_taken=True

    data = {
        'is_taken': DinnersDate.objects.filter(date=date).exists()
    }
    return JsonResponse(data)


@login_required
def addDinner(request):

    form = forms.formAddDinner()

    if request.method == 'POST':
        form = forms.formAddDinner(request.POST)
        if form.is_valid():
            NAME = form.cleaned_data['name']
            print(NAME)
            obj = Dinners()
            obj.dinners=NAME
            obj.save()

    return render(request,'basic_app/addDinner.html',{'form':form})

def addDinnerDate(request):
    DINS= Dinners.objects.all()
    #CH =[(i+1,DINS[i].dinners) for i in range(len(DINS))]
    CH=[(0,'-------------'),]
    CH +=[(i.pk,i.dinners) for i in DINS]
    day = date.today()
    DATE_TAB=[(0,'---------------'),]
    monday=False
    for i in range(5):
        if day.weekday() == 0:
            monday=True

            break
        if day.weekday()== 2:
            monday=False

            break
        day+=timedelta(1)

    while i<20:
        if monday:
            k=(day,str(day)+" "+"Monday")
            DATE_TAB.append(k)
            day+=timedelta(2)
            monday=False
            continue
        else:
            k=(day,str(day)+" "+"Wednasday")
            DATE_TAB.append(k)
            day+=timedelta(5)
            monday=True

        i+=1

    #delta = timedelta(1)
    #DATE_TAB = [(today+(timedelta(i)),str(today+(timedelta(i)))) for i in range(20)]

    form = forms.formAddDinnerDate(CH,DATE_TAB)
    if request.method == 'POST':
        form = forms.formAddDinnerDate(CH,DATE_TAB,request.POST)
        if form.is_valid():
            print(form.cleaned_data['din'])
            print(form.cleaned_data['date'])
            DIN=form.cleaned_data['din']
            DATE=form.cleaned_data['date']
            d=request.POST.get('bday')
            print(d)
            dat=[i.date for i in DinnersDate.objects.all()]
            #dat2 = DinnersDate.objects.filter(date=DATE)
            #if dat2:
            #    print("jest w tablicy")
            #else:
            #    print("nie ma w tablicy")
            #print("dat2",dat2)
            #if request.POST.get('submit1'):
            #    print("jest submit 1")
            #elif request.POST.get('submit2'):
            #    print("nie ma submit 1")
            #print("Submit :",request.POST.get('submit1'))
            obj = DinnersDate()
            obj.din=Dinners.objects.get(pk=DIN)
            obj.date = DATE
            obj.save()
            #request.session['test'] = 'new'
            #for i in dat:
            #    print(i)
            #messages.error(request, 'testowy')
            #if dat2:
            #    print("JESSST")
            #    messages.error(request, 'Dodałeś kolejny obiad do tego dnia')

    return render(request,'basic_app/addDinnerDate.html',{'form':form})
@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))

def register(request):
    #inject ='injection'
    #user_form = forms.UserForm()
    registered = False

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = forms.UserForm(data=request.POST)
        #profile_form = UserProfileInfoForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid():

            # Save User Form to Database
            user = user_form.save()

            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()

            # Now we deal with the extra info!

            # Can't commit yet because we still need to manipulate
            #profile = profile_form.save(commit=False)

            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            #profile.user = user

            # Check if they provided a profile picture
            #if 'profile_pic' in request.FILES:
            #    print('found it')
                # If yes, then grab it from the POST form reply
            #    profile.profile_pic = request.FILES['profile_pic']

            # Now save model
            #profile.save()

            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = forms.UserForm()
        #profile_form = UserProfileInfoForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'basic_app/registration.html',{'user_form':user_form,'registered':registered })

def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('index'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'basic_app/login.html', {})
