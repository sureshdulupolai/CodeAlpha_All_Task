from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .models import URL
from .utils import generate_short_code

def home(request):
    if request.method == "POST":
        original = request.POST.get("original_url")
        short_code = generate_short_code()
        new_url = URL.objects.create(original_url=original, short_code=short_code)
        # Use correct relative path for redirect link
        short_url = request.build_absolute_uri(f'/{short_code}')
        return render(request, 'task1/home.html', {"short_url": short_url})
    
    # Default GET request loads the template
    return render(request, 'task1/home.html')

def redirect_url(request, code):
    try:
        url = URL.objects.get(short_code=code)
        return redirect(url.original_url)
    except URL.DoesNotExist:
        return HttpResponse("Invalid Short URL", status=404)

def api_create_short_url(request):
    if request.method == "POST":
        original = request.POST.get("url")
        code = generate_short_code()
        URL.objects.create(original_url=original, short_code=code)
        return JsonResponse({"short_url": request.build_absolute_uri(f'/{code}')})
    return JsonResponse({"error": "POST method required"}, status=400)
