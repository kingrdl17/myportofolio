from django.shortcuts import render
from main.models import Experience, Education
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404, redirect, render
from main.forms import EducationForm
from main.forms import ExperienceForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render
import datetime
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from main.forms import EducationForm


# ====================================================================================================== SHOW =====================================================

def show_main(request):
    last_login = request.COOKIES.get('last_login', 'No login session found.')
    context = {
        "name": "Marclay Ardell",
        "npm": "2506621024",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Passionate computer science student at Universitas Indonesia, with a keen interest in software development and problem-solving. Constantly learning new things and developing my skills."
        ),
        "last_login": last_login,
    }
    return render(request, "index.html", context) 

def show_experience(request):
    title_query = request.GET.get("title", "").strip()
    context = {
        "name": "Marclay Ardell",
        "title_query": title_query,
        "form": ExperienceForm(),
        "is_editor": request.user.groups.filter(name="Editor").exists(),
    }
    return render(request, "experience.html", context)

@login_required(login_url="/login/")
def toggle_star(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        if request.user in experience.starred_by.all():
            experience.starred_by.remove(request.user)
        else:
            experience.starred_by.add(request.user)

    return redirect("main:show_experience")

def show_education(request):
    json_response = get_education_json(request)

    educations = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    educations = [education.object for education in educations]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Marclay Ardell",
        "education_list": educations,
        "title_query": title_query,
        "is_editor": request.user.groups.filter(name="Editor").exists(),
    }
    return render(request, "education.html", context)

# ====================================================================================================== CREATE =====================================================

@login_required(login_url="/login/")
def create_education(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    form = EducationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Added Successfully!")
        return redirect("main:show_education")

    context = {
        "name": "Marclay Ardell",
        "form": form,
    } 
    return render(request, "education_form.html", context)

@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Added Successfully!")
        return redirect("main:show_experience")

    context = {
        "name": "Marclay Ardell",
        "form": form,
    }
    return render(request, "experience_form.html", context)

@login_required(login_url="/login/")
def edit_education(request, education_id):
    if not request.user.is_superuser and not request.user.groups.filter(name="Editor"):
        raise PermissionDenied

    education = get_object_or_404(Education, pk=education_id)
    form = EducationForm(request.POST or None, instance=education)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Updated Successfully!")
        return redirect("main:show_education")

    context = {
        "name": "Marclay Ardell",
        "form": form,
        "education": education,
    }
    return render(request, "education_form.html", context)

@login_required(login_url="/login/")
def edit_experience(request, experience_id):
    if not request.user.is_superuser and not request.user.groups.filter(name="Editor"):
            raise PermissionDenied

    experience = get_object_or_404(Experience, pk=experience_id)
    form = ExperienceForm(request.POST or None, instance=experience)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Updated Successfully!")
        return redirect("main:show_experience")

    context = {
        "name": "Marclay Ardell",
        "form": form,
        "experience": experience,
    }
    return render(request, "experience_form.html", context)

# ====================================================================================================== DELETE =====================================================

@login_required(login_url="/login/")
def delete_education(request, education_id):
    if not request.user.is_superuser:
        raise PermissionDenied

    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        education.delete()
        messages.success(request, "Deleted")
        return redirect("main:show_education")

    return redirect("main:show_education")

@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied

    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Deleted")
        return redirect("main:show_experience")

    return redirect("main:show_experience")

# ====================================================================================================== GET JSON =====================================================

def get_education_json(request):
    title_query = request.GET.get("title", "").strip()
    educations = Education.objects.all()

    if title_query:
        educations = educations.filter(institution__icontains=title_query)

    educations_json = serializers.serialize("json", educations)
    return HttpResponse(educations_json, content_type="application/json")

def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experience = Experience.objects.prefetch_related('starred_by').all()

    if title_query:
        experience = experience.filter(title__icontains=title_query)

    data = []
    for exp in experience:
        starred_users = exp.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])
        data.append({
            "pk": str(exp.id),
            "fields": {
                "title": exp.title,
                "description": exp.description,
                "category": exp.category,
                "category_display": exp.get_category_display(),
                "started_at": exp.started_at.isoformat(),
                "ended_at": exp.ended_at.isoformat() if exp.ended_at else None,
                "thumbnail": exp.thumbnail,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })
    return JsonResponse(data, safe=False)

@require_POST
def create_experience_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan pengalaman."},
            status=403,
        )
    form = ExperienceForm(request.POST)
    if form.is_valid():
        experience = form.save()
        return JsonResponse(
            {"message": "Pengalaman berhasil ditambahkan.", "pk": str(experience.id)},
            status=201,
        )
    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)

# ====================================================================================================== AUTH =====================================================
def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Account successfully created, please login.")
        return redirect("main:login")

    context = {
        "name": "Clay",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Clay",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response