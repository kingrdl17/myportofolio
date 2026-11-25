from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import ProjectForm
from .models import Project


def show_project(request):
    context = {
        "name": "Marclay Ardell",
        "title_query": request.GET.get("title", "").strip(),
        "form": ProjectForm(),
        "is_editor": request.user.groups.filter(name="Editor").exists(),
    }
    return render(request, "pages/project/index.html", context)


@login_required(login_url="/login/")
def toggle_project_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == "POST":
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)
    return redirect("projects:show_project")


@login_required(login_url="/login/")
def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    form = ProjectForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Added Successfully!")
        return redirect("projects:show_project")
    return render(request, "pages/project/form.html", {"name": "Marclay Ardell", "form": form})


@login_required(login_url="/login/")
def edit_project(request, project_id):
    if not request.user.is_superuser and not request.user.groups.filter(name="Editor").exists():
        raise PermissionDenied
    project = get_object_or_404(Project, pk=project_id)
    form = ProjectForm(request.POST or None, instance=project)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Updated Successfully!")
        return redirect("projects:show_project")
    return render(request, "pages/project/form.html", {"name": "Marclay Ardell", "form": form, "project": project})


@login_required(login_url="/login/")
def delete_project(request, project_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    project = get_object_or_404(Project, pk=project_id)
    if request.method == "POST":
        project.delete()
        messages.success(request, "Deleted")
    return redirect("projects:show_project")


def get_project_json(request):
    projects = Project.objects.prefetch_related("starred_by").all()
    title_query = request.GET.get("title", "").strip()
    if title_query:
        projects = projects.filter(project_name__icontains=title_query)
    data = [{
        "pk": str(project.id),
        "fields": {
            "project_name": project.project_name,
            "project_description": project.project_description,
            "category": project.category,
            "category_display": project.get_category_display(),
            "technologies_used": project.technologies_used,
            "project_link": project.project_link,
            "star_count": project.starred_by.count(),
            "is_starred": request.user in project.starred_by.all() if request.user.is_authenticated else False,
        },
    } for project in projects]
    return JsonResponse(data, safe=False)


@require_POST
def create_project_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse({"message": "Only the portfolio owner can add projects."}, status=403)
    form = ProjectForm(request.POST)
    if form.is_valid():
        project = form.save()
        return JsonResponse({"message": "Project added successfully.", "pk": str(project.id)}, status=201)
    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)
