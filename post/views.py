from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import PostForm
from .models import Post


def show_post(request):
    context = {
        "name": "Marclay Ardell",
        "title_query": request.GET.get("title", "").strip(),
        "form": PostForm(),
        "is_editor": request.user.groups.filter(name="Editor").exists(),
    }
    return render(request, "pages/post/index.html", context)


@login_required(login_url="/login/")
def create_post(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    form = PostForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Added Successfully!")
        return redirect("post:show_post")
    return render(request, "pages/post/form.html", {"name": "Marclay Ardell", "form": form})


@login_required(login_url="/login/")
def edit_post(request, post_id):
    if not request.user.is_superuser and not request.user.groups.filter(name="Editor").exists():
        raise PermissionDenied
    post = get_object_or_404(Post, pk=post_id)
    form = PostForm(request.POST or None, instance=post)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Updated Successfully!")
        return redirect("post:show_post")
    return render(request, "pages/post/form.html", {"name": "Marclay Ardell", "form": form, "post": post})


@login_required(login_url="/login/")
def delete_post(request, post_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        post.delete()
        messages.success(request, "Deleted")
    return redirect("post:show_post")


def get_post_json(request):
    posts = Post.objects.all()
    title_query = request.GET.get("title", "").strip()
    if title_query:
        posts = posts.filter(title__icontains=title_query)
    data = [{
        "pk": str(post.id),
        "fields": {
            "title": post.title,
            "image_url": post.image_url,
            "content": post.content,
            "category": post.category,
            "category_display": post.get_category_display(),
        },
    } for post in posts]
    return JsonResponse(data, safe=False)


@require_POST
def create_post_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse({"message": "Only the portfolio owner can add posts."}, status=403)
    form = PostForm(request.POST)
    if form.is_valid():
        post = form.save()
        return JsonResponse({"message": "Post added successfully.", "pk": str(post.id)}, status=201)
    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)
