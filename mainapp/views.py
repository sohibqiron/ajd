from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import CreateEmployeeForm,UserCreationForm

def logoutUser(request):
    logout(request)
    return redirect('login')

def registerUser(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            return redirect('dashboard')
    
    context = {
        'form':form
    }

    return render(request, 'mainapp/register.html')

def loginUser(request):
        if request.method == 'POST':
            username = request.POST.get('username') 
            password = request.POST.get('password') 

            user = authenticate(request, username=username, password=password) 

            if user is not None: 
                login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, "Username or password was incorrect")
        
        context = {

        }

        return render(request, 'mainapp/login.html')

# Create your views here.
def test(request):
    return render(request,'mainapp/bace.html')

@login_required(login_url='login')
def index(request):
    return render(request,'mainapp/index.html')

@login_required(login_url='login')
def bace(request):
    return render(request,'mainapp/bace.html')

@login_required(login_url='login')
def employeesTable(request):
    employees = Employee.objects.all()
    
    context = {
        'employees':employees
    }
    return render(request,'mainapp/table.html',context)


@login_required(login_url='login')
def employeCreate(request):
    form = CreateEmployeeForm()
    if request.method == "POST":
        form = CreateEmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('e_table')
        else:
            form = CreateEmployeeForm()
    context ={
        'form': form
    }
    return render(request,'mainapp/e-create.html',context)


@login_required(login_url='login')
def updateEmployee(request,pk):
    if request.user.is_superuser or request.user.is_staff:
            employee = Employee.objects.get(id=pk)
            form = CreateEmployeeForm(instance=employee)
            if request.method == "POST":
                form = CreateEmployeeForm(request.POST,instance=employee)
                if form.is_valid():
                    form.save()
                    return redirect('e_table')
                
            context = {
                'form':form
            }
            return render(request, 'mainapp/e-create.html', context)
    else:
        return redirect('e_table') 


@login_required(login_url='login')
def employeDelete(request,pk):
    if request.user.is_superuser:
        employee = Employee.objects.get(id=pk)
        if request.method =="POST":
                employee.delete()
                return redirect('e_table')

        context = {
                'employee':employee
            }
        return render(request,'mainapp/e-delete.html',context)
    else:
        return redirect('e_table') 
    
    
def productsTable(request):
    products = Products.objects.all()
    noutbooks = Noutbook.objects.all()
    
    context = {
        "products":products,
        "noutbooks":noutbooks,
    }
    
    return render(request,'mainapp/Products/p_table.html',context)



def noutbookTable(request):
    noutbooks = Noutbook.objects.all()
    
    context = {
        "noutbooks":noutbooks
    }
    
    return render(request,'mainapp/Products/noutbook.html',context)