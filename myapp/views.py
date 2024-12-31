from django.shortcuts import render,redirect
from django.contrib.auth import logout
from .forms import*
from django.core.mail import send_mail
import random
from empowerilliterate  import settings
from .crud import*
from django.http import HttpResponse


# Create your views here.
def index(request):
    user=request.session.get('user')
    return render(request,'index.html',{'user':user})

def hireee(request):
    user=request.session.get('user')
    worker_data=addworker_model.objects.all()
    return render(request,'hiree.html',{'user':user,'worker_data':worker_data})
def add_worker(request):
    user=request.session.get('user')
    if request.method=="POST":
        hireedata=add_workerform(request.POST)
        if hireedata.is_valid():
            hireedata.save()
            print("data has benn saved!")
            return redirect('hiree')
        
        else:
            print(hireedata.errors)    
    return render(request,'add_worker.html',{'user':user})

def job(request):
    user=request.session.get('user')
    jobdata=addjob_model.objects.all()
    return render(request,'job.html',{'user':user,'jobdata':jobdata})

def add_job(request):
    user=request.session.get('user')
    if request.method=="POST":
        jobdata=add_jobform(request.POST)
        if jobdata.is_valid():
            jobdata.save()
            print("data has benn saved!")
            return redirect('job')
        
        else:
            print(jobdata.errors)    
    return render(request,'add_job.html',{'user':user})
def signup(request):
    massage = ""  
    global data
    if request.method == "POST":
        data = signupform(request.POST)
        if data.is_valid():
            email = data.cleaned_data['email']
            try:
                signupmodel.objects.get(email=email)
                print("Username is already exists!")
                massage = "Username is already exists!"
            except signupmodel.DoesNotExist:
                print("Signup successfully!")
                # Email OTP sending code
                global otp
                otp = random.randint(1111, 9999)
                sub = "Your One Time Password"
                msg = f"Hello User!\n\nThanks for registration with us!\n\nYour one time password is {otp}.\n\nThanks & Regards!\nEmpower Illiterate - \n+91 9737439749 | pratixagosai2000@gmail.com"
                from_ID = settings.EMAIL_HOST_USER
                to_ID = [request.POST['email']]
                send_mail(subject=sub, message=msg, from_email=from_ID, recipient_list=to_ID)
                return redirect('otpverify')
        else:
            
            massage = "something went wrong.. "
            print(data.errors)  
    
    return render(request, 'signup.html', {'massage': massage})



def update_profile(request):
    msg=""
    user=request.session.get('user')
    uid=request.session.get('uid')
    cuser=signupmodel.objects.get(id=uid)
    if request.method=='POST':
        updateReq=signupform(request.POST,instance=cuser)
        if updateReq.is_valid():
            updateReq.save()
            
            print("Your profile has been updated!")
            msg="Your profile has been updated!"
            return redirect('/')
        else:
            print(updateReq.errors)
            msg="Error!Something went wrong...Try again!"
    return render(request,'update_profile.html',{'user':user,'cuser':cuser,'msg':msg})
    


def login(request):
    msg=""
    if request.method=='POST':
        unm=request.POST['email']
        pas=request.POST['password']

        user=signupmodel.objects.filter(email=unm,password=pas)
        uid=signupmodel.objects.get(email=unm)
        if user:
            print("Login successfully")
            msg="Login sucessfully"
            request.session['user']=unm
            request.session['uid']=uid.id
            return redirect('/')
        else:
            print("Error! login faild...")  
            msg="Error! login faild..."  
    return render(request,'login.html',{'msg':msg})

def contact(request):
    msg=""

    user=request.session.get('user')
    if request.method=='POST':
        conreq=contactform(request.POST)
        if conreq.is_valid():
            conreq.save()
            print(" Your response has been submitted! ")
            msg="Your response has been submitted!"
            #Email Sending
            sub="Thankyou!"
            msg=f"Hello User!\n\nThanks for connecting with us!\nWe will contact you shortly!\n\nThanks & Regards\n+919737439749 | pratixagosai2000@gmail.com"
            from_ID=settings.EMAIL_HOST_USER
            to_ID=[request.POST['email']]
            send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=to_ID)

        else:
            print(conreq.errors)    
            msg="something went wrong.."

    return render(request,'contact.html',{'user':user})

def otpverify(request):
    msg=""
    if request.method=='POST':
        if request.POST['otp']==str(otp):
            data.save()
            print("Verification done!")
            return redirect('login')
        else:
            print("Error!Invalid OTP")
            msg="Error!Invalid OTP"
    return render(request,'otpverify.html',{'msg':msg})

def userlogout(request):
    logout(request)
    return redirect('login')

def verify_job(request):
    msg=""
    user=request.session.get('user')
    if request.method=='POST':
        unm=request.POST['phone']
        pas=request.POST['password']
        
        user=addjob_model.objects.filter(phone=unm,password=pas)
        uid=addjob_model.objects.get(phone=unm)
        if user:
            print(" successfully")
            request.session['uid']=uid.id
            
            return redirect('updatejob')
        else:
            print("password Wrong...")  
            msg="Error! password wrong..."  
       
    return render(request,'verify_job.html',{'msg':msg,'user':user})

def updatejob(request):
    msg=""
    user=request.session.get('user')
    uid=request.session.get('uid')
    jobuser=addjob_model.objects.get(id=uid)
    if request.method=='POST':
        updateReq=add_jobform(request.POST,instance=jobuser)
        if updateReq.is_valid():
            updateReq.save()
            
            print("Your profile has been updated!")
            msg="Your profile has been updated!"
            return redirect('job')
        else:
            print(updateReq.errors)
            msg="Error!Something went wrong...Try again!"
    return render(request,'updatejob.html',{'user':user,'jobuser':jobuser,'msg':msg})
    
def deletejob(request):
    uid=request.session.get('uid')
    deluser=addjob_model.objects.get(id=uid)
    deluser.delete()
    return redirect('job')


#for worker
def verify_worker(request):
    msg=" "
    user=request.session.get('user')
    if request.method=='POST':
        unm=request.POST['phone']
        pas=request.POST['password']
        
        user=addworker_model.objects.filter(phone=unm,password=pas)
        uid=addworker_model.objects.get(phone=unm)
        if user:
            print(" successfully")
            request.session['uid']=uid.id
            
            return redirect('update_worker')
        else:
            print("password Wrong...")  
            msg="Error! password wrong..."  
    
             
       
    return render(request,'verify_worker.html',{'msg':msg,'user':user})

def update_worker(request):
    msg=""
    
    user=request.session.get('user')
    uid=request.session.get('uid')
    workeruser=addworker_model.objects.get(id=uid)
    if request.method=='POST':
        updateReq=add_workerform(request.POST,instance=workeruser)
        if updateReq.is_valid():
            updateReq.save()
            
            print("Your profile has been updated!")
            msg="Your profile has been updated!"
            return redirect('hiree')
        else:
            print(updateReq.errors)
            msg="Error!Something went wrong...Try again!"
    return render(request,'update_worker.html',{'user':user,'workeruser':workeruser,'msg':msg})
    
def deleteworker(request):
    uid=request.session.get('uid')
    deluser=addworker_model.objects.get(id=uid)
    deluser.delete()
    return redirect('hiree')
 

def search_data(request):
    user = request.session.get('user')
    query = request.GET.get('q', '') 
    job_results = []
    worker_results = []
    
    if query:
        # Search in workers
        worker_results = addworker_model.objects.filter(
            models.Q(fullname__icontains=query) | 
            models.Q(skills__icontains=query) |
            models.Q(location__icontains=query)
        )
        
        # Search in jobs
        job_results = addjob_model.objects.filter(
            models.Q(job_title__icontains=query) | 
            models.Q(work_location__icontains=query) |
            models.Q(job_requirements__icontains=query)
        )

    return render(request, 'search_results.html', {
        'user': user,
        'query': query,
        'job_results': job_results,
        'worker_results': worker_results,
    })

def forgetpassword(request):
    if request.method == 'POST':
        email = request.POST['ema   il']
        if signupmodel.objects.filter(email=email).exists():
            user = signupmodel.objects.get(email=email)
            send_mail(
                "Reset Your Password",
                f"Hello {user.email},\n\nTo reset your password, click on the link below:\nhttp://127.0.0.1:8000/newpasswordpage/{user.id}/\n\nThanks & Regards,\nEmpower Illiterate Team",
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=True
            )
            return HttpResponse("Password reset link has been sent to your email.")
        else:
            return HttpResponse("Email does not exist.")
    return render(request, 'password_reset_request.html')


def newpasswordpage(request, user):
    userid = signupmodel.objects.get(id=user)
    if request.method == "POST":
        
        pas1 = request.POST['password1']
        pas2 = request.POST['password2']
        if pas1 == pas2:
            userid.password = pas1  
            userid.save()
            return HttpResponse("Password has been reset successfully.")
        else:
            return HttpResponse("Passwords do not match.")
    return render(request, 'newpasswordpage.html')
    












    