from django.shortcuts import render
from .form import UserRegistrationForm, UserInfoForm, UserDeleteForm, CourseInfoForm, CourseDeleteForm
from .models import Userinfo, Courseinfo
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "User/home.html")

def register(request):
    if(request.method == "POST"):
        form = UserRegistrationForm(request.POST)
        if(form.is_valid()):
            form.save()
            return render(request, "User/home.html")
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, "User/register.html", context)

def login(request):
    return render(request, "User/login.html")

@login_required
def logout(request):
    return render(request, "User/logout.html")

@login_required
def profile(request):
    context = {
        'fname': request.user.first_name,
        'lname': request.user.last_name,
        'email': request.user.email,
    }
    return render(request, "User/profile.html", context)

@login_required
def userinfo(request):
    uinfo = Userinfo.objects.all().order_by('user_id', '-user_semester')
    context = {'uinfo': uinfo}
    return render(request, "User/userinfo.html", context)

@login_required()
def enteruserinfo(request):
    if(request.method == "POST"):
        form = UserInfoForm(request.POST)
        if(form.is_valid()):
            this_user= form.save(commit=False)
            this_user.user=request.user.username
            this_user.user_firstname=request.user.first_name
            this_user.user_lastname = request.user.last_name
            this_user.save()
            uinfo = Userinfo.objects.all().order_by('user_id', '-user_semester')
            context = {'uinfo': uinfo}
            return render(request, "User/userinfo.html", context)
    else:
        form = UserInfoForm()
    context = {'form': form}
    return render(request, "User/enteruserinfo.html", context)

@login_required()
def deleteuser(request, user_id):
    user = Userinfo.objects.get(user_id=user_id)
    form = UserDeleteForm(request.POST)
    if request.method == "POST":
        user.delete()
        uinfo = Userinfo.objects.all().order_by('user_id', '-user_semester')
        context = {'uinfo': uinfo}
        return render(request, "User/userinfo.html", context)

    context = {'form': form}
    return render(request, "User/delete.html", context)

@login_required()
def updateuser(request, user_id):
    user = Userinfo.objects.get(user_id=user_id)
    form = UserInfoForm(request.POST)
    if request.method == 'POST':
        form = UserInfoForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            uinfo = Userinfo.objects.all().order_by('user_id', '-user_semester')
            context = {'uinfo': uinfo}
            return render(request, "User/userinfo.html", context)
    form = UserInfoForm(initial=user.__dict__)
    context = {'form': form, 'user' : user}
    return render(request, "User/update.html", context)

@login_required
def courseinfo(request):
    cinfo = Courseinfo.objects.all().order_by('course_userid', '-course_semester')
    context = {'cinfo': cinfo}
    return render(request, "User/courseinfo.html", context)

@login_required()
def entercourseinfo(request):
    if(request.method == "POST"):
        form = CourseInfoForm(request.POST)
        if(form.is_valid()):
            form.save()
            cinfo = Courseinfo.objects.all().order_by('course_userid', '-course_semester')
            context = {'cinfo': cinfo}
            return render(request, "User/courseinfo.html", context)
    else:
        form = CourseInfoForm()
    context = {'form': form}
    return render(request, "User/entercourseinfo.html", context)

@login_required()
def deletecourse(request, course_id):
    course = Courseinfo.objects.get(course_id=course_id)
    form = CourseDeleteForm(request.POST)
    if request.method == "POST":
        course.delete()
        cinfo = Courseinfo.objects.all().order_by('course_userid', '-course_semester')
        context = {'cinfo': cinfo}
        return render(request, "User/courseinfo.html", context)

    context = {'form': form}
    return render(request, "User/deletecourse.html", context)

@login_required()
def updatecourse(request, course_id):
    course = Courseinfo.objects.get(course_id=course_id)
    if request.method == 'POST':
        form = CourseInfoForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            cinfo = Courseinfo.objects.all().order_by('course_userid', '-course_semester')
            context = {'cinfo': cinfo}
            return render(request, "User/courseinfo.html", context)
    form = CourseInfoForm(initial=course.__dict__)
    context = {'form': form, 'course' : course}
    return render(request, "User/updatecourse.html", context)