from django.shortcuts import render, HttpResponse, redirect, reverse
from vamp_shop.models import Product, Contact, Orders, orderupdate
from math import ceil
import json
from django.views.decorators.csrf import csrf_exempt
from Paytm import Checksum
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView,LoginView

MERCHANT_KEY = 'VMLsKh3337413176'


def loginhome(request):
        return render(request, "shop/login.html")




def handlelogin(request):
    if request.method == "POST":
        # getting the inputs for signup from user
        logusername = request.POST['logusername']
        logpassword = request.POST['password']
      
        # Authenticate the user
        user = authenticate(request, username=logusername, password=logpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "Your account has been logged in.")
            return redirect('/shop/home')
        else:
            messages.error(request, "Please verify your credentials.")
            return redirect('/')

    else:
        return HttpResponse("404 - Not found")
    

    
@login_required(login_url='login')
def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')

@login_required(login_url='login')
def searchMatch(query, item):
    '''return true only if query matches the item'''
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False

@login_required(login_url='login')
def search(request):
    query= request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod=[item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod)!= 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'list': allProds, "msg":""}
    if len(allProds)==0 or len(query)<4:
        params={'msg':"Please make sure to enter relevant search query"}
    return render(request, 'shop/search.html', params)


@login_required(login_url='login')
def products(request, myid):
    product = Product.objects.filter(id=myid)
    params = {"products":product[0]}
    return render(request, "shop/products.html", params)


@login_required(login_url='login')
def home(request):
    allprods = []
    catprods = Product.objects.values('category')
    cats = {item['category'] for item in catprods}

    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allprods.append([prod, range(1,nSlides), nSlides])

    params = {'list': allprods}
    return render(request, 'shop/home.html', params)


@login_required(login_url='login')
def about(request):
    return render(request, "shop/about.html")



@login_required(login_url='login')
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        sub=request.POST.get('subject', '')
        msg=request.POST.get('message', '')
        contact = Contact(name = name, email = email ,subject = sub, message= msg)
        contact.save()
    return render(request, "shop/contact.html")


@login_required(login_url='login')
def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = orderupdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps({"status":"success", "updates": updates, "itemsJson": order[0].items_json}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"NoItem"}')
        except Exception as e:
            return HttpResponse('{{"status":"Failure"}}')

    return render(request, 'shop/tracker.html')


@login_required(login_url='login')
def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone, amount=amount)
        order.save()
        update = orderupdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        # return render(request, 'shop/checkout.html', {'thank':thank, 'id': id})
        
        # Request paytm to transfer the amount to your account after payment by user
        param_dict = {

                'MID': 'VMLsKh33374131769871',
                'ORDER_ID': str(order.order_id),
                'TXN_AMOUNT': str(amount),
                'CUST_ID': email,
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'VampEvents',
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL':'http://127.0.0.1:8000/shop/handlerequest/',

        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request, 'shop/paytm.html', {'param_dict': param_dict})

    return render(request, 'shop/checkout.html')

@login_required(login_url='login')
@csrf_exempt
def handlerequest(request):
    # paytm will send post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'shop/paymentstatus.html', {'response': response_dict})


@login_required(login_url='login')
def handlesignup(request):
    try:
        if request.method == "POST":
        # getting the inputs for signup from user
            username = request.POST['username']
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            pass1 = request.POST['pass1']
            pass2 = request.POST['pass2']

        # Check for errors

            if not username.isalnum():
                messages.error(request, "Please enter Username with letters and Numbers only")
                return redirect('/')
            
            if (pass1 != pass2):
                messages.error(request, "Both password should match")
                return redirect('/')

        # save the user    
            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name= fname
            myuser.last_name= lname
            myuser.save()
            messages.success(request, " Your account has been successfully created")
            return redirect('/shop/home')

        else:
            return HttpResponse("<h2> 404 - Not found</h2>")
    except Exception as e:
        return HttpResponse("<h2>404 - Not found : It seems username is already in our Database. Please try a unique Username</h2> error exception as {}".format(e))

