from django.shortcuts import render, redirect
from .models import *
import pandas as pd
from django.core.mail import EmailMessage
import random
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout

otp_time = 0
def form(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username, email, password)
        user.save()
    return render(request, 'form.html')


    # global otp_time
    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     phone_number = request.POST.get('phone_number')
    #     email = request.POST.get('email')
    #     password = request.POST.get('password')
    #
    #     email_otp = random.randint(1000, 9999)
    #     mobile_otp = random.randint(1000, 9999)
    #
    #     request.session['email'] = email
    #     print('Email OTP = ', email_otp)
    #
    #     request.session['phone_number'] = phone_number
    #     print('Phone OTP = ', mobile_otp)
    #
    #     # otp = ''.join(random.choices('0123456789', k=4))
    #
    #     print(username, phone_number, email, password, email_otp)
    #
    #     d = {"username": [username],
    #          "phone_number": [phone_number],
    #          "email": [email],
    #          "password": [password],
    #          "email_otp": [email_otp],
    #          "mobile_otp": [mobile_otp]
    #          }
    #
    #     df = pd.DataFrame(d)
    #     df.to_csv('media/data.csv', index=False)
    #
    #     data = MyModel(username=username,
    #                    phone_number=phone_number,
    #                    email=email,
    #                    password=password,
    #                    email_otp=email_otp,
    #                    mobile_otp=mobile_otp
    #                    )
    #     data.save()
    #
    #     csv_file_path = "/media/data.csv"
    #
    #     csv_data = df.to_csv(index=False)
    #
    #     # Create an EmailMessage object
    #     email = EmailMessage(
    #         subject='CSV File Attached',
    #         body=f'Hello {username},\n\nYour OTP is: {email_otp}\n\nPlease use this OTP to verify your email.\n\nThank you.',
    #         from_email='settings.EMAIL_HOST_USER',
    #         to=[email],
    #     )
    #
    #     # Attach the CSV file
    #     email.attach('data.csv', csv_data, 'text/csv')
    #
    #     # Send the email
    #     email.send()
    #     otp_time = 3
    #     return redirect('e_otp')
    # return render(request, template_name='form.html')
def table(request):
    data = MyModel.objects.all()
    return render(request, template_name='table.html', context={'data': data})


def dashboard(request):
    data = MyModel.objects.all()
    return render(request, 'dashboard.html', {'data': data})

def userdashboard(request):
    data = MyModel.objects.all()
    return render(request, 'userdashboard.html',{'data': data})

# def loginform(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         print(username, password)
#         try:
#             obj = MyModel.objects.filter(username=username,
#                                          password=password).first()
#             if obj:
#                 return redirect('userdashboard')
#         except:
#             return render(request, 'loginform.html', {'error': f"Invalid username and password"})
#     return render(request, 'loginform.html')

def loginform(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        obj = authenticate(username=username, password=password)
        if obj:
            return redirect('userdashboard')
        # try:
        #     obj = MyModel.objects.filter(username=username, password=password).first()
        #     if obj:
        #         if newpassword:
        #             obj.set_password(newpassword)
        #             obj.save()
        #         return redirect('userdashboard')
        # except:
        else:
            return render(request, 'loginform.html', {'error': f"Invalid username and password"})
    return render(request, 'loginform.html')

def e_otp(request):
    global otp_time
    email = request.session.get('email')
    obj = MyModel.objects.filter(email=email).last()

    if request.method == 'POST':
        otp_time -= 1
        e = "Hello Are You have a {} try for otp verification".format(otp_time)
        while otp_time >= 0:
            otp1 = request.POST.get('otp1')
            otp2 = request.POST.get('otp2')
            otp3 = request.POST.get('otp3')
            otp4 = request.POST.get('otp4')

            user_otp = otp1 + otp2 + otp3 + otp4
            request.session = ['email']
            print("Email_otp::", e_otp)

            if user_otp == obj.email_otp:
                otp_time = 3
                return redirect('ph_otp')
            else:
                if otp_time == 0:
                    return redirect('form')

                print("OTP Not Match")
                print("Print otp is not match !!")
                return render(request, 'otp.html', context={'error': e})
        else:
            return redirect('form')
    else:
        return render(request, 'otp.html')

def email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        request.session['email'] = email
        return render(request, 'forgot_password.html')
    return render(request, 'email.html')

# def forgot_password(request):
#     if request.method == 'POST':
#         email = request.session.get('email')
#         newpassword = request.POST.get('newpassword')
#         user = User(email=email)
#         if user:
#             user.password = newpassword
#             user.set_password(newpassword)
#             user.save()
#         return render(request, 'loginform.html')
#     return render(request, 'forgot_password.html')

def forgot_password(request):
    if request.method == "POST":
        email = request.session.get('email')
        newpassword = request.POST.get('newpassword')
        if newpassword:
            try:
                user = User.objects.get(email=email)
                user.set_password(newpassword)
                user.save()
                return redirect('loginform')
            except User.DoesNotExits:
                messages.error(request,'user does not exits.')
                return render(request,'forgot_password.html')
        else:
            messages.error(request, 'newpassword cannot be empty.')
            return render(request, 'forgot_password.html')
    return render(request, 'forgot_password.html')


'''def e_otp(request):
    global otp_time
    email = request.session.get('email')
    obj = MyModel.objects.filter(email=email)
    for i in range(1, otp_time):
        print("In Loop ::=> ", i)
        if request.method == 'POST':
            print("In Post Method")
            print('otp_time : ', otp_time)
            otp1 = request.POST.get('otp1')
            otp2 = request.POST.get('otp2')
            otp3 = request.POST.get('otp3')
            otp4 = request.POST.get('otp4')

            user_otp = otp1 + otp2 + otp3 + otp4
            print("email_user_otp = ", user_otp)
            print(type(user_otp))
            print(obj[len(obj)-1].email_otp)
            if user_otp == str(obj[len(obj)-1].email_otp):
                # Handle the case where OTP is correct
                print("OTP Match")
                otp_time = 3
                return redirect('ph_otp')
            else:
                print("OTP Not Match")
                otp_time -= 1
                print("Print otp is not match !!")
                return render(request, 'otp.html', context={'error': f"{otp_time} Invalid OTP"})
        else:
            return redirect('form')
    return render(request, template_name='otp.html')
'''
def ph_otp(request):
    global otp_time
    print('otp_time : ', otp_time)
    phone_number = request.session.get('phone_number')
    # phn = "+91" + phone_number
    obj = MyModel.objects.filter(phone_number=phone_number).last()
    # url = f'https://2factor.in/API/V1/2a8f9503-cb39-11ee-8cbb-0200cd936042/SMS/{phn}/{obj[len(obj)-1].mobile_otp}/OTP1'

    # responseotp = requests.get(url)
    # print(responseotp.status_code)

    # if responseotp.status_code == 200:
    #     print("Yes OTP Sent Successfully")
    # else:
    #     print("OTP is not Sent Due to Some Error ", responseotp.status_code)



    if request.method == 'POST':
        otp_time -= 1
        while otp_time >= 0:
            otp1 = request.POST.get('otp1')
            otp2 = request.POST.get('otp2')
            otp3 = request.POST.get('otp3')
            otp4 = request.POST.get('otp4')

            user_otp = otp1 + otp2 + otp3 + otp4
            print("phone_user_otp = ", user_otp)
            print(type(user_otp))
            # correct_otp = request.POST.get('otp')

            if user_otp == obj.mobile_otp:
                # Handle the case where OTP is correct
                return redirect('dashboard')
            else:
                if otp_time == 0:
                    return redirect('form')

                print("Print otp is not match !!")
                return render(request, 'phnotp.html', context={'error': f"{otp_time}Invalid OTP"})
        else:
            return redirect('form')
    else:
        return render(request, template_name='phnotp.html')


def view(request, id):
    data = MyModel.objects.get(id=id)
    return render(request, 'view.html', {'data': data})

def edit(request, id):
    data = MyModel.objects.get(id=id) 
    if request.method == 'POST':
        data.username = request.POST.get('username')
        data.phone_number = request.POST.get('phone_number')
        data.email = request.POST.get('email')
        data.password = request.POST.get('password')
        print(data.username, data.phone_number, data.email, data.password)
        data.save()
        data = MyModel.objects.all()
        return render(request, template_name='table.html', context={'data': data})
    return render(request, template_name='edit.html', context={'data': data})

def delete(request, id):
    MyModel.objects.get(id=id).delete()
    data = MyModel.objects.all()
    return render(request, template_name='table.html', context={'data': data})

def logout_view(request):
    if request.method == "POST":
        if 'yes' in request.POST:
            logout(request)
            return redirect('loginform')
        elif 'no' in request.POST:
            return redirect('userdashboard')
    return render(request, 'logout.html')
