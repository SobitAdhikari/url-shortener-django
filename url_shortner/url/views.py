from django.shortcuts import render, redirect
from .models import URL
from .utils import generate_short_code
from django.shortcuts import get_object_or_404
from django.db.models import F

def home(request):
    if request.method == "POST":
        long_url = request.POST.get("long_url")
        short_code = generate_short_code()

        # Ensure uniqueness
        while URL.objects.filter(short_code=short_code).exists():
            short_code = generate_short_code()

        url = URL.objects.create(
            long_url=long_url,
            short_code=short_code
        )

        short_url = request.build_absolute_uri(f"/{short_code}")
        return render(request, "url/home.html", {"short_url": short_url})

    return render(request, "url/home.html")



def redirect_url(request, code):
    url = get_object_or_404(URL, short_code=code)
    
    url.clicks = F('clicks') + 1
    url.save()
    return redirect(url.long_url)