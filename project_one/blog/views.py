from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm, CompanyForm, AffiliaterForm, EmployeeForm, ServicesForm
from django.contrib.auth.decorators import login_required
from .models import Profile, Company, Affiliater, Employee, Services


@login_required
def dashboard(request):
    company_info_name = Company.objects.all().filter(author=request.user)
    affiliater_info_name = Affiliater.objects.all()
    return render(request, 'account/main.html', {'company_info_name': company_info_name, 'affiliater_info_name': affiliater_info_name})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
        else:
            return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
# Создаем нового пользователя, но пока не сохраняем в базу данных.
            new_user = user_form.save(commit=False)
# Задаем пользователю зашифрованный пароль.
            new_user.set_password(user_form.cleaned_data['password'])
# Сохраняем пользователя в базе данных.
# Создание профиля пользователя.
            Profile.objects.create(user=new_user)
            new_user.save()
            return render(request,
                'registration/register_done.html',
                {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})


@login_required
def my_progect(request):
    global affiliater_info_name
    company_info_name = Company.objects.all().filter(author=request.user)
    if company_info_name:
        for i in company_info_name:
            affiliater_info_name = Affiliater.objects.all().filter(company_name=i.id)
    return render(
        request, 'account/my_progect.html',
        {'company_info_name': company_info_name, 'affiliater_info_name': affiliater_info_name})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
            data=request.POST,
            files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'registration/edit.html',
              {'user_form': user_form, 'profile_form': profile_form})


def company(request):
    print(request)
    return HttpResponse ('Hello World Company')


@login_required
def create_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('my_progect')
        else:
            return HttpResponse('Ошибка заполнения')
    else:
        form = CompanyForm()
    return render(request, 'account/create_company.html', {'form': form})


@login_required
def create_affiliater(request):
    if request.method == 'POST':
        form = AffiliaterForm(request.POST)
        if form.is_valid():
            company_id = Company.objects.all().filter(author=request.user)
            for i in company_id:
                form.instance.company_name = i
            form.save()
            return redirect('my_progect')
        else:
            return HttpResponse('Ошибка заполнения')
    else:
        form = AffiliaterForm()
    return render(request, 'account/create_affiliater.html', {'form': form})


@login_required
def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
        else:
            return HttpResponse('Ошибка заполнения')
    else:
        form = EmployeeForm()
    return render(request, 'account/create_employee.html', {'form': form})


@login_required
def employee_list(request):
    employee_lists = Employee.objects.all()
    return render(request, 'account/employee_list.html', {'employee_lists': employee_lists})


@login_required
def create_services(request):
    if request.method == 'POST':
        form = ServicesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('services_list')
        else:
            return HttpResponse('Ошибка заполнения')
    else:
        form = ServicesForm()
    return render(request, 'account/create_services.html', {'form': form})


@login_required
def del_services(request):
    try:
        services = Services.objects.get(id=id)
        services.delete()
        return redirect('services_list')
    except Services.DoesNotExist:
        return HttpResponse("<h2>Person not found</h2>")


@login_required
def services_list(request):
    services_lists = Services.objects.all()
    return render(request, 'account/services_list.html', {'services_lists': services_lists})