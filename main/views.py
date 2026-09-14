from django.shortcuts import render

from main.models import Experience, Project


def show_main(request):
    context = {
        "name": "Baby Akiko Gracia",
        "npm": "2506625224",
        "study_program": "S1 Sistem Informasi",
        "bio": "Second year Information System student at Universitas Indonesia ",
        "experience_list": Experience.objects.all(),
        "project_list": Project.objects.all(),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Baby Akiko Gracia",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_projects(request):
    context = {
        "name": "Baby Akiko Gracia",
        "project_list": Project.objects.all(),
    }
    return render(request, "projects.html", context)