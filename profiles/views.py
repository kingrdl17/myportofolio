from django.shortcuts import render


def show_main(request):
    last_login = request.COOKIES.get("last_login", "No login session found.")
    context = {
        "name": "Marclay Ardell",
        "npm": "2506621024",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Passionate computer science student at Universitas Indonesia, with a keen "
            "interest in software development and problem-solving. Constantly learning "
            "new things and developing my skills."
        ),
        "last_login": last_login,
    }
    return render(request, "pages/profile/index.html", context)
