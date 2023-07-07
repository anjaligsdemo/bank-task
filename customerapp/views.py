from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth import get_user_model
from .models import District, Branch, AbstractUser, UserMaterials, Material, CustomUser
from django.http import JsonResponse

# Create your views here.
User = get_user_model()

def home(request):
    district_list = District.objects.all()
    context = {
        'districts': district_list,
    }
    print(context)
    return render(request, 'home.html',context)


# Create your views here.


def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if User.objects.filter(username=username).exists():
            messages.info(request, "Username already taken")
            return redirect('/user/register')
        elif password != confirm_password:
            messages.info(request, "Password not matching")
            return redirect('/registration')
        else:
            create_user = User.objects.create_user(username=username, password=password)
            create_user.save()
            return redirect('/login')
    else:
        return render(request, 'registration.html')
    return render(request, 'registration.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/userhome')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('/login')

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)

    return redirect('/home')


def userhome(request):
    if request.method == 'POST':
        errors = {}
        user = request.user
        first_name = request.POST.get('firstname')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        district = request.POST.get('district')
        branch = request.POST.get('branch')
        account_type = request.POST.get('account_type')
        materials = request.POST.getlist('materials')
        if not first_name or len(first_name) < 2:
            errors['first_name'] = 'First name must be at least 2 characters long.'
        if not phone:
            errors['phone'] = 'Phone number should contain only digits.'
        elif not phone.isdigit():
            errors['phone'] = 'Phone number field is required.'
        if not age:
            errors['age'] = 'Age field is required.'
        elif not age.isdigit():
            errors['age'] = 'Age must be a valid number.'
        if not dob:
            errors['dob'] = 'Date of birth is required.'

        if errors:
            pass
        else:
            user.first_name = first_name
            user.gender = gender
            user.date_of_birth = dob
            user.age = age
            user.phone = phone
            user.email = email
            user.address = address
            user.district_id = district
            user.branch_id = branch
            user.bank_account_type = account_type
            user.save()
            messages.success(request, "User data has been saved successfully")

        for material_id in materials:
            material = Material.objects.get(id=material_id)
            UserMaterials.objects.create(user_profile=user, material=material)
    else:
        errors = {}
    district_list = District.objects.all()
    gender_choices = CustomUser.GENDER_CHOICES
    account_type_choices = CustomUser.ACCOUNT_TYPE_CHOICES
    material_type = Material.objects.all()
    context = {
        'gender_choices': gender_choices,
        'account_type_choices': account_type_choices,
        'districts': district_list,
        'materials': material_type,
        'errors': errors,

    }
    return render(request, 'userhome.html', context)


def get_branches_by_district(request, district_id):
    district = District.objects.get(id=district_id)
    branches = Branch.objects.filter(district=district)
    return render(request, 'your_template.html', {'branches': branches})


def get_branches_by_district(request):
    district_id = request.GET.get('district_id')
    branches = Branch.objects.filter(district_id=district_id).values('id', 'name')
    return JsonResponse(list(branches), safe=False)