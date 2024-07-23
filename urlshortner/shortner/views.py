from django.shortcuts import render, redirect
import uuid
from .models import Url
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=link,uuid=uid)
        new_url.save()
        return HttpResponse(uid)

from django.shortcuts import get_object_or_404

# Example handling in shortner/views.py
from django.shortcuts import redirect
def go(request, pk):
    if pk == 'admin':
        return redirect('/admin/')  # Redirect to Django admin
    else:
        try:
            url_details = Url.objects.get(uuid=pk)
            url_details=url_details.link[8::]
            return redirect('https://'+url_details)
        except Url.DoesNotExist:
            return HttpResponseNotFound('URL not found')

