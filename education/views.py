from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import EducationForm
from .models import Education


def show_education(request):
    context = {
        "name": "Marclay Ardell",
        "title_query": request.GET.get("title", "").strip(),
        "form": EducationForm(),
        "is_editor": request.user.groups.filter(name="Editor").exists(),
    }
    return render(request, "pages/education/index.html", context)


@login_required(login_url="/login/")
def create_education(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    form = EducationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Added Successfully!")
        return redirect("education:show_education")

    return render(request, "pages/education/form.html", {"name": "Marclay Ardell", "form": form})


@login_required(login_url="/login/")
def edit_education(request, education_id):
    if not request.user.is_superuser and not request.user.groups.filter(name="Editor").exists():
        raise PermissionDenied

    education = get_object_or_404(Education, pk=education_id)
    form = EducationForm(request.POST or None, instance=education)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Updated Successfully!")
        return redirect("education:show_education")

    return render(
        request,
        "pages/education/form.html",
        {"name": "Marclay Ardell", "form": form, "education": education},
    )


@login_required(login_url="/login/")
def delete_education(request, education_id):
    if not request.user.is_superuser:
        raise PermissionDenied

    education = get_object_or_404(Education, pk=education_id)
    if request.method == "POST":
        education.delete()
        messages.success(request, "Deleted")
    return redirect("education:show_education")


def get_education_json(request):
    educations = Education.objects.all()
    title_query = request.GET.get("title", "").strip()
    if title_query:
        educations = educations.filter(institution__icontains=title_query)

    data = [
        {
            "pk": str(education.id),
            "fields": {
                "institution": education.institution,
                "degree": education.degree,
                "field_of_study": education.field_of_study,
                "description": education.description,
                "started_at": education.started_at.isoformat(),
                "ended_at": education.ended_at.isoformat() if education.ended_at else None,
                "thumbnail": education.thumbnail,
            },
        }
        for education in educations
    ]
    return JsonResponse(data, safe=False)


@require_POST
def create_education_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan pendidikan."},
            status=403,
        )

    form = EducationForm(request.POST)
    if form.is_valid():
        education = form.save()
        return JsonResponse(
            {"message": "Pendidikan berhasil ditambahkan.", "pk": str(education.id)},
            status=201,
        )
    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)
