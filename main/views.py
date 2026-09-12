from django.shortcuts import render

from main.models import Experience, Education


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
    context = {
        "name": "Marclay Ardell",
        "education_list": Education.objects.all(),
    }
    return render(request, "education.html", context)