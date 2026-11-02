from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import ExperienceForm
from .models import Experience


def show_experience(request):
    context = {
        "name": "Marclay Ardell",
        "title_query": request.GET.get("title", "").strip(),
        "form": ExperienceForm(),
        "is_editor": request.user.groups.filter(name="Editor").exists(),
    }
    return render(request, "pages/experience/index.html", context)


@login_required(login_url="/login/")
def toggle_star(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)
    if request.method == "POST":
        if request.user in experience.starred_by.all():
            experience.starred_by.remove(request.user)
        else:
            experience.starred_by.add(request.user)
    return redirect("experience:show_experience")


@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    form = ExperienceForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Added Successfully!")
        return redirect("experience:show_experience")

    return render(request, "pages/experience/form.html", {"name": "Marclay Ardell", "form": form})


@login_required(login_url="/login/")
def edit_experience(request, experience_id):
    if not request.user.is_superuser and not request.user.groups.filter(name="Editor").exists():
        raise PermissionDenied

    experience = get_object_or_404(Experience, pk=experience_id)
    form = ExperienceForm(request.POST or None, instance=experience)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Updated Successfully!")
        return redirect("experience:show_experience")

    return render(
        request,
        "pages/experience/form.html",
        {"name": "Marclay Ardell", "form": form, "experience": experience},
    )


@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied

    experience = get_object_or_404(Experience, pk=experience_id)
    if request.method == "POST":
        experience.delete()
        messages.success(request, "Deleted")
    return redirect("experience:show_experience")


def get_experience_json(request):
    experiences = Experience.objects.prefetch_related("starred_by").all()
    title_query = request.GET.get("title", "").strip()
    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    data = []
    for experience in experiences:
        starred_users = experience.starred_by.all()
        data.append(
            {
                "pk": str(experience.id),
                "fields": {
                    "title": experience.title,
                    "description": experience.description,
                    "category": experience.category,
                    "category_display": experience.get_category_display(),
                    "started_at": experience.started_at.isoformat(),
                    "ended_at": experience.ended_at.isoformat() if experience.ended_at else None,
                    "thumbnail": experience.thumbnail,
                    "star_count": starred_users.count(),
                    "is_starred": request.user in starred_users if request.user.is_authenticated else False,
                    "starred_by_names": ", ".join(user.username for user in starred_users),
                },
            }
        )
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
