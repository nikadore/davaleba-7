from django.shortcuts import render

def info_view(request):
    context = {
        "first_name": "shmagi",
        "last_name": "tantalashvili",
        "age": 67,
        "height": "250 cm",
    }
    return render(request, "info.html", context)

def hobbies_view(request):
    hobbies = ["Reading", "Coding", "Football"]
    grade = 12
    context = {
        "hobbies": hobbies,
        "grade": grade,
    }
    return render(request, "hobbies.html", context)
