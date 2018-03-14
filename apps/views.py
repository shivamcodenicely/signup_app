from django.shortcuts import render
from .models import Sign
from django.core.mail import EmailMessage
from django.template import Context
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.http import HttpResponse
from django.http import JsonResponse
import random
import json
from django.views.decorators.csrf import csrf_exempt


def post_list(request):
    return render(request,
                  'signup.html',
                  )
def ajax(request):
    return render(request,
                  'signupajax.html',
                  )


def new1(request):
    if request.method=="POST":
        print("##############################################")
        fname = request.POST.get("first_name")
        lname = request.POST.get("last_name")
        username = request.POST.get("user_name")
        password = request.POST.get("user_password")
        #confirm_password=request.POST.get("confirm_password")
        global email,fname,username,contact

        email = request.POST.get("email")
        contact=request.POST.get("contact_no")
        profile_picture = request.POST.get("profile_picture")
        print(profile_picture)
        # profile=Sign()

        # profile.emp=username
        # profile.save()

        for x in range(1000,9999):
            global otp
            otp = random.randrange(1000,9999)
            print(otp)
            break

        send_mail('test email', str(otp), 'shivam.mittal38@gmail.com', [email])

        emp=Sign.objects.create(fname=fname,lname=lname,username=username,password=password,email=email,contact=contact,profile_picture=profile_picture)
        emp.save()



        return render(request,
                      'otp.html',{"email":email})

def Otp(request):
    otp1 = request.POST.get("OTP")

    if otp1 == str(otp):
        return render(request, "profile.html",
                      {"Name": fname, "email": email, "username": username, "contact": contact})
    else:
        print("error")
        return render(request, "otp.html")

def login(request):

    email=request.POST.get("email")
    password = request.POST.get("user_password")
    user=authenticate(email="email",password="user_password")

    if user is not None:
        return render(request,"profile.html")
    else:
        return render(request,"login.html")


def authn(request):
     if request.method=="POST":
         data = Sign.objects.all()
         for i in data:
             # print("#################")
             pssword =(i.password)
             email=(i.email)
             name=(i.fname)
             user=(i.username)
             contact=(i.contact)

         get_pwd=request.POST.get('user_password')
         get_email=request.POST.get('email')
         if pssword==get_pwd and email==get_email:
             print("true")
             return render(request, "profile.html",{'email':email,'Name':name,'username':user,'contact':contact})

         else:

             return render (request,"login.html")
@csrf_exempt
def validate_username(request):
    contxt={}
    if request.method=="POST":
        email = request.POST.get('email')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        uname=request.POST.get('uname')
        pwd=request.POST.get('pwd')
        contact=request.POST.get('contact')
        for x in range(1000,9999):
            global otp
            otp = random.randrange(1000,9999)
            print(otp)
            break

        # contxt['email']=email
        # contxt['fname']=fname
        # contxt['lname']=lname
        # contxt['uname']=uname
        # contxt['pwd']=pwd
        # contxt['contact']=contact
        # print(contxt)
        send_mail('test email', str(otp), 'shivam.mittal38@gmail.com', [email])
        emp = Sign.objects.create(fname=fname, lname=lname, username=uname, password=pwd, email=email,
                                  contact=contact)
        emp.save()

        return render(request,'otp.html')

def loginajax(request):

    email=request.POST.get("email")
    password = request.POST.get("user_password")
    user=authenticate(email="email",password="user_password")

    if user is not None:
        return render(request,"profile.html")
    else:
        return render(request,"loginajax.html")

def signajax(request):
    if request.method=="POST":
        print("##############################################")
        fname = request.POST.get("first_name")
        lname = request.POST.get("last_name")
        username = request.POST.get("user_name")
        password = request.POST.get("user_password")
        #confirm_password=request.POST.get("confirm_password")
        #global email,fname,username,contact
        email = request.POST.get("email")
        contact=request.POST.get("contact_no")

        for x in range(1000,9999):
            global otp
            otp = random.randrange(1000,9999)
            print(otp)
            break

            # emailid = EmailMessage('Subject', otp, to=['email'])
            # print(emailid)
            # emailid.send()
            #
            # msg = EmailMessage('subject', otp , to = [])
            # msg.send()

        send_mail('test email', str(otp), 'shivam.mittal38@gmail.com', [email])

        emp=Sign.objects.create(fname=fname,lname=lname,username=username,password=password,email=email,contact=contact)
        emp.save()

        return render(request,
                      'otp.html',{"email":email})

# def myview(request):
#     if request.method == 'POST':
#         form = MyForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#     else:
#         form = MyForm()
#     return render(request, 'otp.html', {'form': form})


# def show_images(request):
#     context = {
#         'images': Sign.objects.all().order_by('-created_at'),
#         'media_url': settings.MEDIA_URL,
#     }
#     return render(request,'profile.html', context)

def forget_pass(request):
    return render(request,'forget_pass.html')

def new2(request):
    if request.method=='POST':
        data1 = Sign.objects.all()
    get_email=request.POST.get("email")
    get_contact = request.POST.get("contact_no")

    reset_pass1=Sign.objects.get(email=get_email)
    # emailid=Sign.objects.get(email=get_email)
    # reset_pass=Sign.objects.all()

    reset_pass=reset_pass1.password
    emailid=reset_pass1.email

    send_mail('Password email', str(reset_pass), 'shivam.mittal38@gmail.com', [emailid])

    return render(request, 'login.html')
