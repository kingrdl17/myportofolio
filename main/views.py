from django.shortcuts import render
from main.models import Experience, Education
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from main.forms import EducationForm
from main.forms import ExperienceForm

# ====================================================================================================== SHOW =====================================================

def show_main(request):
    context = {
        "name": "Marclay Ardell",
        "npm": "2506621024",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Passionate computer science student at Universitas Indonesia, with a keen interest in software development and problem-solving. Constantly learning new things and developing my skills."
        ),
    }
    return render(request, "index.html", context)

def show_experience(request):
    context = {
        "name": "Marclay Ardell",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)


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
    }
    return render(request, "education.html", context)

# ====================================================================================================== CREATE =====================================================

def create_education(request):
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

def create_experience(request):
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



# ====================================================================================================== DELETE =====================================================

def delete_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        education.delete()
        messages.success(request, "Deleted")
        return redirect("main:show_education")

    return redirect("main:show_education")

def delete_experience(request, experience_id):
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
    experience = Experience.object.all()

    if title_query:
        experience = experience.filter(title__icontains=title_query)

    experience_json = serializers.serialize("json", experience)
    return HttpResponse(experience_json, content_type="application/json")
