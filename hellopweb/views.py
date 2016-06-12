from django.http import HttpResponse


def Hi(req):
    return HttpResponse("Hi")
