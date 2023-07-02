from django.shortcuts import render
from django.http import JsonResponse
from . import models


def index_view(request):
    if request.method == 'GET':
        domains = models.Domain.objects.all()
        # return render(request, 'index.html', {'domains': domains})
        return JsonResponse({'domain_list': list(domains.values())})
