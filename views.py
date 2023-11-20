from django.http import HttpResponse


def SubmoduleView(request):
    return HttpResponse({'msg': "remote submodule"})