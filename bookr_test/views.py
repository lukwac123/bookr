from django.http import HttpResponse

def greeting_view(request):
    """Powitanie użytkownika."""
    return HttpResponse("Witaj w witrynie Bookr! Jedyne miejsce w którym możesz tworzyć recenzje książek.")

