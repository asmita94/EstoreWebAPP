from django.shortcuts import redirect, render, HttpResponse,redirect
from django.views import View
from msgqpp.models import Msg
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from msgqpp.models import Product2
from msgqpp.models import Cart,Order
from django.db.models import Q
import random
import razorpay
from django.core.mail import send_mail

def makepayment(request):
    orders=Order.objects.filter(uid=request.user.id)
    s=0
    for x in orders:
        s=s+x.pid.price*x.gty
        oid=x.order_id
    client = razorpay.Client(auth=("rzp_test_E9w9Tvgdt4IVfn", "dgX67ts0DKXKVLg6E0pvq8St"))
    data = { "amount": s*100, "currency": "MYR", "receipt": "oid" }
    payment = client.order.create(data=data)
    print(payment)
    context={}
    context['data']=payment
    return render(request,'payment.html',context)
    return HttpResponse("in make payment")

def sendusermail(request):
    uemail=request.user.email 
    print(uemail)
    send_mail(
    "Ecart-Order Placed Successfully",
    "Order details are:",
    "mahajanasmita442@gmail.com",
    [uemail],
    fail_silently=False,
)
    
    return HttpResponse("mail is sent sucessfully")


def place_order(request):
    userid=request.user.id
    c=Cart.objects.filter(uid=userid) 
    oid=random.randrange(1000,9999)
    print("order.id:",oid)
    for x in c:
        print(x)
        print(x.pid)
        print(x.uid)
        print(x.gty)
        o=Order.objects.create(order_id=oid, pid=x.pid, uid=x.uid, gty=x.gty)
        o.save()
        x.delete()
    orders=Order.objects.filter(uid=request.user.id)
    s=0
    n=len(orders)
    for x in orders:
        s=s+x.pid.price*x.gty
    context={}
    context['np']=n
    context['total']=s
    context['products']=orders
    return render(request,'place_order.html',context)

def cart(request):
    userid=request.user.id
    c=Cart.objects.filter(uid=userid)
    # print(c)
    # print(c[0])
    # print(c[1])
    # print(c[0].pid.name)
    # print(c[0].pid.price)
    n=len(c)
    s=0
    for x in c:
        # print(x)
        s=s+x.pid.price
    print(s)
    context={}
    context['np']=n
    context['total']=s
    context['products']=c
    return render(request,'cart.html',context)
    return render(request,'cart.html')

def remove(request,cid):
    c=Cart.objects.filter(id=cid)
    c.delete()
    return redirect('/cart')

def updategty(request,qv,cid):
    # print(type(qv))
    # return HttpResponse("in update quantity")
    c=Cart.objects.filter(id=cid)
    # print(c)
    # print(c[0].gty)
    if qv=='1':
        t=c[0].gty+1
        c.update(gty=t)
    else:    
        if c[0].gty>1:
            t=c[0].gty-1
            c.update(gty=t) 
    s=0
    for x in c:
         s= s+ x.pid.price * x.gty
    context={}
    context['products']=c
    context['total']=s
    return render(request,'cart.html',context)
    return redirect('/cart')
    return HttpResponse("in update quantity")

# Create your views here.
def addcart(request,pid):
    if request.user.is_authenticated:
        # print("user is logged")
        # return HttpResponse("User log in")
        u=User.objects.filter(id=request.user.id)
        # print(u)
        # print(u[0])
        # print(u[0].username)
        # print(u[0].is_superuser)
        p=Product2.objects.filter(id=pid)
        q1=Q(uid=u[0])
        q2=Q(pid=p[0])
        c=Cart.objects.filter(q1&q2)
        print(c)
        n=len(c)
        print(n)
        context={}
        context['products']=p
        if n==1:
            context['msg']="Product alredy exist !!"
        else:
        #print(p) check product exits
        #return HttpResponse("Product is added in cart")
             c=Cart.objects.create(uid=u[0],pid=p[0])
             c.save()
             context['success']="Product added sucessfully to cart"
        return render(request,'product_details.html',context)
    else:
        return redirect("/login")

def home2(request):
    # userid=request.user.id
    # print("id is logg",userid)
    # print("result:",request.user.is_authenticated)

    context={}
    p=Product2.objects.filter(is_active=True)
    print(p)
    print(p[0])
    print(p[0].price)
    print(p[0].cate)
    context['products']=p
    return render(request,'index.html',context)

def pd(request,pid):
    context={}
    context['products']=Product2.objects.filter(id=pid)
    return render(request,'product_details.html',context)

def home3(request):
    context={}
    p=Product2.objects.all()
    context['products']=p
    return render(request,'index.html',context)

def catfilter(request,cv):
    q1=Q(is_active=True)
    q2=Q(cate=cv)
    p=Product2.objects.filter(q1&q2)
    context={}
    context['products']=p
    return render(request,'index.html',context)

def range(request):
    min=request.GET['min']
    max=request.GET['max']
    # print(min)
    # print(max)
    q1=Q(price__gte=min)
    q2=Q(price__lte=max)
    q3=Q(is_active=True)
    p=Product2.objects.filter(q1&q2&q3)
    context={}
    context['products']=p
    return render(request,'index.html',context)

    return HttpResponse("values fetched")

def sort(request,sv):
    # print(type(sv))
    if sv=='0':
        col='price'
    else:
        col='-price'
    p=Product2.objects.filter(is_active=True).order_by(col)
    context={}
    context['products']=p
    return render(request,'index.html',context)


def user_logout(request):
    logout(request)
    # context={}
    # context['title']="logout"
    #demo(request)
    #return render(request,'header.html',context)
# def demo(request):
    return redirect('/home2')

def registration(request):
    context = {}
    if request.method=='POST':
        uname=request.POST['uname']
        upass=request.POST['upass']
        ucpass=request.POST['ucpass']
        if uname=="" or upass=="" or ucpass=="":
            context['errmsg']="filed cannot be empty"
            return render(request,'registration.html',context)
        elif upass!=ucpass:
            context['errmsg']="password and confirm passsword did not match"
            return render(request,'registration.html',context)
        else:
            try:
                u=User.objects.create(username=uname, email=uname)
                u.set_password(upass)
                u.save()
                context['sucess']="user creates succesfully"
                return render(request,'registration.html',context)
            except Exception:
                context['errmsg']="This user alredy existy"
                return render(request,'registration.html',context)
        #return HttpResponse("User created Sucessfully")
    else:
        return render(request,'registration.html')
def login_user(request):
    context={}
    if request.method=='POST':
        uname=request.POST['uname']
        upass=request.POST['upass']
        if uname=="" or upass=="" :
            context['errmsg']="filed cannot be empty"
            return render(request,'login.html',context)
        else:
            u=authenticate(username=uname,password=upass)
            # print(u)
            # print(u.email)
            # print(u.is_superuser)
            # return HttpResponse("in else part")
            if u is not None:
                login(request,u)#start session and store id of logged in user seeion
                return redirect('/home2')
            else:
                context['errmsg']="invalid username and password"
                return render(request,'login.html',context)
    return render(request,'login.html')
def contact(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
    return render(request,'contact.html',{'form':form})
def about(request):
    return render(request,'about.html')
def product_details(request):
    return render(request,'product_details.html')
###def testing(request):
    return HttpResponse("Hello linked sucessfully")
def create(request):
    #print("request is: ",request.method)
    if request.method=='GET':
       return render(request,'create.html')
    else:
        #fetch data from form
        n=request.POST['uname']
        e=request.POST['uemail']
        m=request.POST['mobile']
        msg=request.POST['msg']
        print(n)
        print(e)
        print(m)
        print(msg)
        m=Msg.objects.create(name=n,email=e,mobile=m,msg=msg)
        m.save()
        return HttpResponse("data Inserted")
def dashbord(request):
    m=Msg.objects.all()
    print(m)
    print(m[0].name)
    print(m[0].email)
    print(m[0].mobile)
    print(m[0].msg)
    context={}
    context['data']=m
    #return HttpResponse("data Fetch ")
    return render(request,'dashbord.html',context)
def delete(request,rid):
    m=Msg.objects.filter(id=rid)
    m.delete()
    return HttpResponse("Data Delete")



def edit(request,rid):
    m=Msg.objects.get(id=rid)
    print(m)
    if request.method=='POST':
        n=request.POST['uname']
        e=request.POST['uemail']
        m=request.POST['mobile']
        msg=request.POST['msg']
        #Update using sql
        k=Msg.objects.filter(id=rid).update(name=n,email=e,mobile=m,msg=msg)
        return redirect('/dashbord')
    return render(request,'edit.html',{'data':m})
       # return HttpResponse("Data Edited")
    print(m)
    context={}
    context['data']=m
    return render(request,'edit.html')
    #return HttpResponse("Data Edited")
    #return redirect('/dashbord')




