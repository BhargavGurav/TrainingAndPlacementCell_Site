from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from App.models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib import messages
from django.db.models import Q 
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    return render(request, 'home.html')

def team(request):
    return render(request, 'team.html')

def iiicell(request):
    return render(request, 'IIICell.html')

def placementprocedure(request):
    return render(request, 'placementProcedure.html')

def contact(request):
    return render(request, 'contact.html')

def contact_us(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['contact-email']
        message = request.POST['message']

        query = Query(name=name, email=email, message=message)
        query.save()
        messages.success(request, 'Query collected successfully.')
        return HttpResponseRedirect('/')


@cache_control(no_cache=True, must_revalidade=True, no_store=True)
def students(request):
    # if 'q' in request.GET:
    #     q = request.GET.get('q')
    #     all_student_list = Student.objects.filter(
    #     Q(name__icontains=q) | Q(cgpa__icontains=q) | Q(branch__icontains=q) | Q(passing_year__icontains=q) | Q(prn__icontains=q)
    #     ).order_by('prn')
        
    # else:
    all_student_list = Student.objects.all().order_by('prn')
        
        
    # paginator = Paginator(all_student_list, 10)
    # page = request.GET.get('page')
    # all_student = paginator.get_page(page) 

    list_file = open('media/Students.csv', 'w')
    list_file.write('Name'+','+'PRN'+','+'Branch'+','+'CGPA'+','+'Passing Year'+',\n')
    for i in all_student_list:
        list_file.write(i.name + ','+str(i.prn) + ','+str(i.branch) + ','+str(i.cgpa) + ','+str(i.passing_year)+ ',\n')
    
    
    return render(request, 'students.html', {'data' : all_student_list})

@cache_control(no_cache=True, must_revalidade=True, no_store=True)
def profile(request):
    user = Student.objects.get(student=request.user)
    return render(request, 'profile.html', {'data' : user})

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        year = request.POST.get('year')
        branch = request.POST.get('branch')
        cgpa = request.POST.get('cgpa')
        prn = request.POST.get('prn')
        password = request.POST.get('password')
        resume = request.FILES.get('resume')

        if name == '':
            messages.error(request, 'Name is required')
            return HttpResponseRedirect('/register')
        if email == '':
            messages.error(request, 'Email is required')
            return HttpResponseRedirect('/register')
        if len(User.objects.filter(email=email)):
            messages.error(request, 'Email is already registered')
            return HttpResponseRedirect('/register')
        if year == '':
            messages.error(request, 'Passing Year is required')
            return HttpResponseRedirect('/register')
        if branch == '':
            messages.error(request, 'Branch is required')
            return HttpResponseRedirect('/register')
        if cgpa == '':
            messages.error(request, 'CGPA is required')
            return HttpResponseRedirect('/register')
        if prn == '':
            messages.error(request, 'PRN is required')
            return HttpResponseRedirect('/register')
        if resume == '':
            messages.error(request, 'Resume is required')
            return HttpResponseRedirect('/register')
        if password == '':
            messages.error(request, 'Password is required')
            return HttpResponseRedirect('/register')
        if len(password) < 8:
            messages.error(request, 'Password must be at least 8 character long')
            return HttpResponseRedirect('/register')
        if not any(i.isupper() for i in password):
            messages.error(request, 'Password must contain at least one upper case letter')
            return HttpResponseRedirect('/register')
        if not any(i.islower() for i in password):
            messages.error(request, 'Password must contain at least one lower case letter')
            return HttpResponseRedirect('/register')
        if not any(i.isdigit() for i in password):
            messages.error(request, 'Password must contain at least one digit')
            return HttpResponseRedirect('/register')
        else:
            data = User.objects.create_user(email, email, password)
            data.save()
            user = Student(student=data, name=name, passing_year=year, branch=branch, cgpa=cgpa, prn=prn, resume=resume)
            user.save()
            messages.success(request, 'Registration successfully')
            return HttpResponseRedirect('/')
        

    return render(request, 'register.html')

def tandpactivity(request):
    return render(request, 'tandpactivity.html')

@cache_control(no_cache=True, must_revalidade=True, no_store=True)
def recruiter(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == "":
            messages.error(request, 'Username is required')
            return HttpResponseRedirect('/recruiter')
        if password == "":
            messages.error(request, 'Password is required')
            return HttpResponseRedirect('/recruiter')
        if len(password) < 8:
            messages.error(request, 'Password must be at least 8 character long')
            return HttpResponseRedirect('/recruiter')
        if not any(i.isupper() for i in password):
            messages.error(request, 'Password must contain at least one upper case letter')
            return HttpResponseRedirect('/recruiter')
        if not any(i.islower() for i in password):
            messages.error(request, 'Password must contain at least one lower case letter')
            return HttpResponseRedirect('/recruiter')
        if not any(i.isdigit() for i in password):
            messages.error(request, 'Password must contain at least one digit')
            return HttpResponseRedirect('/recruiter')
        else:
            data = User.objects.create_user(username=username, password=password, is_staff=True)
            data.save()
            messages.success(request, 'Registration successful')
            return HttpResponseRedirect('/')

@cache_control(no_cache=True, must_revalidade=True, no_store=True)
def broucher(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        fil = request.FILES.get('file')

        if title == '':
            messages.error(request, 'filename is required')
            return HttpResponseRedirect('/broucher')
        if fil == '':
            messages.error(request, 'File is required')
            return HttpResponseRedirect('/broucher')

        else:
            data = Broucher(title=title, broucher=fil)
            data.save()
            messages.success(request, 'Uploaded successfully')
            return HttpResponseRedirect('/broucher')
    data = Broucher.objects.all()
    return render(request, 'broucher.html' , {'data' : data})

@cache_control(no_cache=True, must_revalidade=True, no_store=True)
def placementreport(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        fil = request.FILES.get('file')

        if title == '':
            messages.error(request, 'filename is required')
            return HttpResponseRedirect('/PlacementReport')
        if fil == '':
            messages.error(request, 'File is required')
            return HttpResponseRedirect('/PlacementReport')

        else:
            data = PlacementReport(title=title, report=fil)
            data.save()
            messages.success(request, 'Uploaded successfully')
            return HttpResponseRedirect('/PlacementReport')

    data = PlacementReport.objects.all()
    # numbers = [int(x) for x in range(0, len(data))]
    # # print(numbers)
    # # print(data, len(data))
    context = {}
    context['data'] = data
    # for i, j in zip(data, numbers):
    #     context[j+1] = i
    # for i, j in context.items():
    #     print(i, j)
    return render(request, 'placementreport.html', context)

@cache_control(no_cache=True, must_revalidade=True, no_store=True)
def mou(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        fil = request.FILES.get('file')

        if title == '':
            messages.error(request, 'filename is required')
            return HttpResponseRedirect('/mou')
        if fil == '':
            messages.error(request, 'File is required')
            return HttpResponseRedirect('/mou')

        else:
            data = Mou(title=title, mou=fil)
            data.save()
            messages.success(request, 'Uploaded successfully')
            return HttpResponseRedirect('/mou')
    data = Mou.objects.all()
    return render(request, 'mou.html', {'data' : data})

@cache_control(no_cache=True, must_revalidade=True, no_store=True)
def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == "":
            messages.error(request, 'Username is required')
            return HttpResponseRedirect('/loginuser')
        if password == "":
            messages.error(request, 'Password is required')
            return HttpResponseRedirect('/loginuser')
        else:
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, 'Login Successful')
                return HttpResponseRedirect('/')
            else:
                messages.error(request, 'User not found')
                return HttpResponseRedirect('/')

    return render(request, 'login.html')

@cache_control(no_cache=True, must_revalidade=True, no_store=True)
def logoutuser(request):
    logout(request)
    messages.success(request, 'Logout Successful')
    return HttpResponseRedirect('/')
