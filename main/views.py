from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Baby Akiko Gracia",
        "npm": "2506625224",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "An Information System student at Universitas Indonesia interested "
            "in UI/UX"
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Baby Akiko Gracia",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)