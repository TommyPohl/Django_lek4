from django.shortcuts import render
from django.http import HttpResponse


def cookies_view(request):
    username = request.COOKIES.get("username", "Neznámy")
    return render(request, "cookies_template.html", {"username":username})


def set_cookie1(request):
    #username = request.COOKIES.get("username", "Neznámy")
    response = render(request, "cookies_template.html", {"username":"Adam"})
    response.set_cookie("username", "Adam", max_age=3600)
    return response


def set_cookie2(request):
    response = render(request, "cookies_template.html", {"username":"Eva"})
    response.set_cookie("username", "Eva", max_age=3600)
    return response


def delete_cookie(request):
    response = render(request, "cookies_template.html")
    response.delete_cookie("username")
    return response