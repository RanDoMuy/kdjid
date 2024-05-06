from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import User, Deposit_History, Withdrawal_History

# Create your views here.

def handler404(request, exception):
    return HttpResponseRedirect('/home/')

def load(request):
    return render(request, "load.html")

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def terms(request):
    return render(request, "terms.html")

def register(request):
    if request.method== "POST":
        fullname= request.POST["fullname"]
        email= request.POST["email"]
        number= request.POST["number"]
        country= request.POST["country"]
        password= request.POST["password"]
        password2= request.POST["password2"]
        country= request.POST["country"]
        try:
            if password2==password:
                user = User.objects.create_user(full_name=fullname, email=email, password=password, passwd= password2, number= number, country=country)
                user.save()
                user = authenticate(request, email=email, password=password)
                login(request, user)
                return redirect("dashboard")   
            else:
                error_message= "Passwords do not match"
                return render(request, "register.html", {"error_message":error_message})
        except:
            redirect("home")
    return render(request, "register.html")

def user_login(request):
    if request.method=="POST":
        email = request.POST['email']
        password = request.POST['password']
        user= authenticate(request, email=email, password=password)
    
        if user is not None:
            login(request, user)
            return redirect("dashboard")
                
        else:
            error_message= "Invalid Username or Password"
            return render(request, "login.html", {"error_message":error_message})
    return render(request, "login.html")

@login_required(login_url='/accounts/login/')
def verify(request):
    user= request.user
    if user.verify== True:
        return redirect("dashboard")
    return render(request, "verify.html")

@login_required(login_url='/accounts/login/')
def dashboard(request):
    user = request.user
    if user.verify== False:
        return redirect("account_verify")
    return render(request, "dashboard.html", {'user': user})

@login_required(login_url='/accounts/login/')
def deposit(request):
    user = request.user
    if user.verify== False:
        return redirect("account_verify")
    deposits = Deposit_History.objects.filter(user=request.user).order_by('-timestamp')
    if request.method == 'POST':
        amount = request.POST['amount']
        deposit = Deposit_History(user=request.user, amount=amount)
        deposit.save()
        return redirect("confirmd", amount=amount)
    return render(request, "deposit.html", {'user': user, 'deposits': deposits})

@login_required(login_url='/accounts/login/')
def confirm_deposit(request, amount):
    user = request.user
    if user.verify== False:
        return redirect("account_verify")
    amount=amount
    return render(request, "confirm_d.html",{'user': user, "amount":amount})

@login_required(login_url='/accounts/login/')
def confirm_withdraw(request):
    user = request.user
    if user.verify== False:
        return redirect("account_verify")
    return render(request, "confirm_w.html",{'user': user})

@login_required(login_url='/accounts/login/')
def invest(request):
    user = request.user
    if user.verify== False:
        return redirect("account_verify")
    return render(request, "invest.html",{'user': user})

@login_required(login_url='/accounts/login/')
def invest_success(request):
    user = request.user
    if user.verify== False:
        return redirect("account_verify")
    return render(request, "invest_success.html",{'user': user})

@login_required(login_url='/accounts/login/')
def invest_failed(request):
    user = request.user
    if user.verify== False:
        return redirect("account_verify")
    return render(request, "invest_fail.html",{'user': user})

@login_required(login_url='/accounts/login/')
def starter(request):
    price= 200
    user= request.user
    if user.verify== False:
        return redirect("account_verify")
    if user.deposit_balance >= price:
        user.deposit_balance= user.deposit_balance - price
        user.trading_plan = "STARTER"
        user.trade_status = "ACTIVE"
        user.save()
        return redirect("invest_success")
    else:
        return redirect("invest_failed")

@login_required(login_url='/accounts/login/')
def bronze(request):
    price= 500
    user= request.user
    if user.verify== False:
        return redirect("account_verify")
    if user.deposit_balance >= price:
        user.deposit_balance= user.deposit_balance - price
        user.trading_plan = "BRONZE"
        user.trade_status = "ACTIVE"
        user.save()
        return redirect("invest_success")
    else:
        return redirect("invest_failed")

@login_required(login_url='/accounts/login/')
def silver(request):
    price= 1000
    user= request.user
    if user.verify== False:
        return redirect("account_verify")
    if user.deposit_balance >= price:
        user.deposit_balance= user.deposit_balance - price
        user.trading_plan = "SILVER"
        user.trade_status = "ACTIVE"
        user.save()
        return redirect("invest_success")
    else:
        return redirect("invest_failed")

@login_required(login_url='/accounts/login/')
def gold(request):
    price= 2000
    user= request.user
    if user.verify== False:
        return redirect("account_verify")
    if user.deposit_balance >= price:
        user.deposit_balance= user.deposit_balance - price
        user.trading_plan = "GOLD"
        user.trade_status= "ACTIVE"
        user.save()
        return redirect("invest_success")
    else:
        return redirect("invest_failed")

@login_required(login_url='/accounts/login/')
def diamond(request):
    price= 5000
    user= request.user
    if user.verify== False:
        return redirect("account_verify")
    if user.deposit_balance >= price:
        user.deposit_balance= user.deposit_balance - price
        user.trading_plan = "DIAMOND"
        user.trade_status= "ACTIVE"
        user.save()
        return redirect("invest_success")
    else:
        return redirect("invest_failed")

@login_required(login_url='/accounts/login/')
def platinum(request):
    price= 10000
    user= request.user
    if user.verify== False:
        return redirect("account_verify")
    if user.deposit_balance >= price:
        user.deposit_balance= user.deposit_balance - price
        user.trading_plan = "PLATINUM"
        user.trade_status= "ACTIVE"
        user.save()
        return redirect("invest_success")
    else:
        return redirect("invest_failed")
 

@login_required(login_url='/accounts/login/')
def withdraw(request):
    user = request.user
    if user.verify== False:
        return redirect("account_verify")
    withdraws = Withdrawal_History.objects.filter(user=request.user).order_by('-timestamp')
    if request.method == 'POST':
        amount = request.POST['amount']
        withdraw = Withdrawal_History(user=request.user, amount=amount)
        withdraw.save()
        return redirect("confirmw")
    return render(request, "withdraw.html", {'user': user, 'withdraws': withdraws})

@login_required(login_url='/accounts/login/')
def faq(request):
    user = request.user
    if user.verify== False:
        return redirect("account_verify")
    return render(request, "faq.html", {'user': user})

@login_required(login_url='/accounts/login/')
def profile(request):
    user = request.user
    if user.verify== False:
        return redirect("account_verify")
    return render(request, "profile.html", {'user': user})

@login_required(login_url='/accounts/login/')
def user_logout(request):
    logout(request)
    return redirect("home")
