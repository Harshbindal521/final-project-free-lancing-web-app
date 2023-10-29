from django import http
from django.http import request
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from django.contrib.auth.models import User
from Lctl.models import freelancer , order, img
from django.views.decorators.csrf import csrf_exempt
import random
from .imglist import imgli


li=[0,1,2,3,4,5,6,7,8,9,]
# Create your views here.

def main(request):
    if freelancer.objects.filter(username =request.user.username).exists():
        return redirect("/freelancer-dashboard")
    return render(request,"main.html")


def cardhome(request):
    if request.user.is_anonymous:
        return redirect("/login")
    list_free = list(freelancer.objects.all().values())
    dictlist = {"li":list_free , "len" : len(list_free), "range": [0,1,2] }
    return render(request, "cardhome.html" ,dictlist)


def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        

        if user is not None:
            if freelancer.objects.filter(username =username).exists():
                login(request, user)
                return redirect("/freelancer-dashboard")
            
            login(request, user)
            return redirect("/")
        else:
            messages.success(request , "0")
            return render(request, "login.html")
    return render(request, "login.html")


def createuser(request):
    if request.method == 'POST':
        
        username = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpass = request.POST.get('confirmpass')
        skills = request.POST.get('skills')
        # desc = request.POST.get('desc')
        country = request.POST.get('country')
        phn = request.POST.get('contact')
        name = str( request.POST.get('fullname'))
        firstname = name.split(' ')[0]
        lastname = name.split(' ')[-1]
        
        if User.objects.filter(username =username).exists():
            messages.success(request, "0")
            return render(request, "register.html")


        if password== confirmpass:
            user = User.objects.create_user(email = email , password=password, username = username, first_name = firstname, last_name= lastname)
            user.save()
            temp = freelancer(name = name, username = username, skills = skills, country = country, phn = phn)
            temp.save()
            login(request, user)
            return redirect("/freelancer-dashboard")

        else:
            return render(request, "register.html")
          
        
    return render(request, "register.html")


def see(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpass = request.POST.get('confirmpass')
        if User.objects.filter(username =username).exists():
            messages.success(request, "0")
            return render(request, "register2.html")
        if password== confirmpass:
            user = User.objects.create_user(email = email , password=password, username = username, first_name = firstname, last_name= lastname)
            user.save()
            login(request, user)
            return redirect("/")
        else:
            return render(request, "register2.html") 
            
    return render(request, "register2.html")      

    


def search(request):
    searchitem= request.GET.get("search")
    list_free = list(freelancer.objects.all().filter(skills__icontains = searchitem) or freelancer.objects.all().filter(name = searchitem))
    dictlist = {"li":list_free}
    return render(request, "cardhome.html" ,dictlist)

def searchfor(request , searchfor):
    searchitem= searchfor
    list_free = list(freelancer.objects.all().filter(skills__icontains = searchitem) or freelancer.objects.all().filter(name = searchitem))
    print(list_free)
    dictlist = {"li":list_free}
    return render(request, "cardhome.html" ,dictlist)


def userlogout(request):
    logout(request)
    return redirect("/")


def freelancer_profile(request, id):
    if request.user.is_anonymous:
        return redirect("/login")
    templi = list(freelancer.objects.all().filter(username = id))
    temp = templi[0]
    dictsend={
        "username":temp.username,
        "name": temp.name,
        "skill": temp.skills,
        "country": temp.country,
        "dp": temp.freelancer_photo,
        "desc" : temp.desc,
        "about": temp.aboutdesc,
        "img1": random.choice(imgli),
        "img2": random.choice(imgli),
        "img3": random.choice(imgli),
        "img4": random.choice(imgli),
        "img5": random.choice(imgli),
        "img6": random.choice(imgli),
    }
    return render(request, "freelancerportfolio.html" , dictsend)


def freelancer_dashboard(request):
    if request.user.is_anonymous:
        return redirect("/login")
    templi = list(freelancer.objects.all().filter(username = request.user.username))
    temp = templi[0]
    print(temp.freelancer_photo)
    dictsend={
        "name": temp.name,
        "skill": temp.skills,
        "country": temp.country,
        "dp": temp.freelancer_photo,
        "desc" : temp.desc,
        "about": temp.aboutdesc,
        "img1": random.choice(imgli),
        "img2": random.choice(imgli),
        "img3": random.choice(imgli),
        "img4": random.choice(imgli),
        "img5": random.choice(imgli),
        "img6": random.choice(imgli),
    }
    return render(request, "userdashboard.html", dictsend)


def edit_freelancer_dashboard(request):
    if request.user.is_anonymous:
        return redirect("/login")

    if request.method=='POST':
        tempuser = freelancer.objects.get(username = request.user.username)
        tempuser.skills = request.POST.get('skills')
        tempuser.name = request.POST.get('name')
        tempuser.country = request.POST.get('country')
        tempuser.aboutdesc = request.POST.get('about')
        freelancer_photo = request.POST.get('photo')
        tempimg = img(photo = freelancer_photo)
        tempimg.save()
        tempuser.freelancer_photo = tempimg.photo
        tempuser.save()

    templi = list(freelancer.objects.all().filter(username = request.user.username))
    temp = templi[0]
    print(temp.freelancer_photo)
    dictsend={
        "name": temp.name,
        "skill": temp.skills,
        "country": temp.country,
        "dp": temp.freelancer_photo,
        "desc" : temp.desc,
        "about": temp.aboutdesc,
        "img1": random.choice(imgli),
        "img2": random.choice(imgli),
        "img3": random.choice(imgli),
        "img4": random.choice(imgli),
        "img5": random.choice(imgli),
        "img6": random.choice(imgli),
    }
    return render(request, "edituserdash.html", dictsend)

def freelancer_work(request):
    
    temp= list(order.objects.all().filter(freelancer_username = request.user.username).filter(order_status=True))
    return render(request, "userworks.html" , {"dictsend": temp} )

# gatewayintegration:


def checkout(request , id):
    if request.user.is_anonymous:
        return redirect("/login")
    
    if request.method=='POST':
        total = request.POST.get('htotal')
        desc = request.POST.get('desc')
        email = request.user.email
        temp = order(client_username = request.user.username , freelancer_username= id, work_desc= desc, order_amount= total , client_email = email )
        temp.save()
        return redirect("/")

#         param_dict ={
#             'MID': 'HuJUxo01540244190631',
#             'ORDER_ID': str(temp.id),
#             'TXN_AMOUNT': str(total),
#             'CUST_ID': request.user.username,
#             'INDUSTRY_TYPE_ID':'Retail',
#             'WEBSITE': 'WEBSTAGING',
#             'CHANNEL_ID':'WEB',
#             'CALLBACK_URL':'http://127.0.0.1:8000/payment',

#         }
#         checksumhash = PaytmChecksum.generateSignature(param_dict, "RDWY_v0gR%U#1SDn")
#         param_dict['CHECKSUMHASH']= checksumhash
#         return render(request, "paytm.html" , {'param_dict':param_dict})

    
    templi = list(freelancer.objects.all().filter(username = id))
    temp = templi[0]
    if request.method == 'GET':
        cpn = request.GET.get('cpn')
        if cpn == "flat90":
            messages.success(request , f"{cpn}")
            print(f"coupon{cpn}")
            dictsend={ 
                "pph": temp.payperhr,
                "discount": 9* (int( temp.payperhr ))/10,
                "total": int(temp.payperhr) - 9*(int( temp.payperhr ))/10,
                "name": temp.name,
                "userid":id,
            }
            return render(request, "checkout.html" , dictsend)
    dictsend={ 
        "pph": temp.payperhr,
        "discount": 0,
        "total": temp.payperhr,
        "name": temp.name,
        "userid":id
        }
    return render(request, "checkout.html" , dictsend)





# @csrf_exempt
# def handelrqst(request):
#     form = request.POST
#     response_dict = {}
#     for i in form.keys():
#         response_dict[i] = form[i]
#         if i == 'CHECKSUMHASH':
#             checksum = form[i]

#     verify = PaytmChecksum.verifySignature(response_dict, "RDWY_v0gR%U#1SDn" , checksum)
#     if verify:
#         if response_dict['RESPCODE'] == '01':
#             temp = order.objects.all().get(id = form['ORDERID'])
#             temp.order_status = True
#             temp.save()
            
#         else:
#             print('order was not successful because' + response_dict['RESPMSG'])

#     return redirect("/")
    

