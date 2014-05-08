### all classes to be used
from django.shortcuts import render
from django.db import models
from models import info
from django import forms
from django.http import HttpResponse
from django.core.mail import send_mail
import string
import random
### creating form fields joined to database
class registerform(forms.ModelForm):
    class Meta:
        model = info
        fields = '__all__'
form = registerform()
def index(request):
    return render(request, 'Registration.html')
### main website
def mainf(request):
    return render(request, 'main.html')
###
# random key generator
def id_generator(size=20, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

### form submission checking
def submit(request):
    error = ''
    a = request.POST.get('name')
    b = request.POST.get('email_id')
    c = request.POST.get('password')
    d = request.POST.get('re_password')
    e = request.POST.get('mob_num')
    f = request.POST.get('gender')
    g = request.POST.get('dob')
    h = request.POST.get('year')
    i = request.POST.get('roll')
    j = request.POST.get('branch')
# If a field is empty, which is no required, saved it as NULL by us.    
    if info.objects.filter(email_id=b).exists():
        error += 'This email id has already been Taken'
        return render(request, 'Registration.html', {'error' : error})
        error = ''
    elif a == '':
        error += 'What? You DON\'T have a name? I think you do. Enter it here.'
        return render(request, 'Registration.html', {'error' : error})
        error = ''
    elif a.replace(' ','').isalpha()==False:
        error += 'That\'s your name huh? Enter a valid one.'
        return render(request, 'Registration.html', {'error' : error})
        error = ''
    elif b == '':
        error += 'You cannot register with us without an email id. ENTER it.'
        return render(request, 'Registration.html', {'error' : error})
        error = ''
    elif '@' not in b or '.' not in b:
        error += 'That\'s not a valid email id. Enter a valid one.'
        return render(request, 'Registration.html', {'error' : error})
        error = ''
    elif c == '':
        error += 'You cannot register with us without a password. ENTER a password.'
        return render(request, 'Registration.html', {'error' : error})
        error = ''        
    elif c != d:
        error+='Password fields did not match. You don\'t have dyslexia, right?'
        return render(request, 'Registration.html', {'error' : error})
        error = ''
    elif e == '':
        error += 'We don\'t communicate only with emails. Don\'t worry, it SHALL be safe with us.'
        return render(request, 'Registration.html', {'error' : error})
        error = ''
    elif i == '':
        error+='The Institue has provided you one. USE it.'
        return render(request, 'Registration.html', {'error' : error})
        error = ''

# VALIDATIONS UNTIL HERE. DATA ENTRY TO DATABASE FOLLOWS!!!
    else:
        rand = id_generator()
        data = {'name' : a.title(), 'password' : c, 'year' : h, 'roll' : i, 'mob_num' : e, 'email_id' : b, 'gender' : f, 'dob' : g, 'branch' : j, 'verify' : False, 'rand' : rand}
        k = registerform(data)
        k.save()
        x = info.objects.get(email_id=b)
        send = '127.0.0.1:8000/verify/' + b + '/' + rand				#call the encryption function. Code is returned by the function
        
        if send_mail('Verify', send, 'csiweblogin@gmail.com',[b], fail_silently=False):
          return render(request, 'submit.html', {'name' : x.name})
        else:
          return render(request, 'submit.html', {'name' : 'srthk'})
### LOGIN CHECK AND LOGIN REDIRECTION!!!
def login(request):
    varb = request.POST.get('email_id')
    if info.objects.filter(email_id=varb).exists():
        a = info.objects.get(email_id=varb)
        b = request.POST.get('password')
        if b == a.password:
            return render(request, 'login.html', {'name' : a.name.title()})
        else:									#incorrect password
            return HttpResponse('incorrect')
    else:									#id not found
        return HttpResponse('enter correct email id')

def verify(request,emailid,qid):
    a = info.objects.get(email_id=emailid)
    if a.rand == qid:								# Call the check function
        a.verify = True
	a.save()
        return render(request, 'verify.html', {'the_email' : a.email_id+' d', 'the_url' : qid})
    else:
        return render(request, 'verify.html', {'the_email' : 'FUCK', 'the_url' : 'YOU'})
