from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import TweetForms,UserRegistrationForms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def home(request):
    return render(request,'home.html')

def tweet_list(request):
    tweet=Tweet.objects.all()
    if request.GET.get('search'):
        search=request.GET.get('search')
        tweet=tweet.filter(text__icontains=search)
    return render(request,'tweet_list.html',{'tweet':tweet})

    
@login_required(login_url='logedin')
def tweet_create(request):
    if request.method=='POST':
        form=TweetForms(request.POST,request.FILES)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user=request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form=TweetForms()
        return render(request,'tweet_form.html',{'form':form})
@login_required(login_url='logedin')
def tweet_edit(request,id):
    tweet=get_object_or_404(Tweet, pk=id,user=request.user)
    # queryset=Tweet.objects.get(id=id)
    
    if request.method=='POST':
        form=TweetForms(request.POST,request.FILES, instance=tweet)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user=request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form=TweetForms(instance=tweet)
    return render(request,'tweet_form.html',{'form':form})
@login_required(login_url='logedin')
def tweet_delete(request,id):
    # tweet=Tweet.objects.get(id=id)
    tweet=get_object_or_404(Tweet, pk=id,user=request.user)
    if request.method=='POST':
        tweet.delete()
        return redirect('tweet_list')
    else:
        return render(request,'tweet_confirm_delete.html', {'tweet':tweet} )
         
def register(request):
    if request.method=='POST':
        form=UserRegistrationForms(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('tweet_list')
        else:
            return render(request, 'register.html', {'form': form}) 

    else:
        form = UserRegistrationForms()

    return render(request, 'register.html', {'form': form})
    
     

def logedin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)  
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
    else:
        form = AuthenticationForm() 

    return render(request, 'login.html', {'form': form})
    
def logedout(request):
    logout(request)
    return redirect('tweet_list')


            