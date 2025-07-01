from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def greeting_view(request):
    """Powitanie użytkownika."""
    return HttpResponse("Witaj w witrynie Bookr! Jedyne miejsce w którym możesz tworzyć recenzje książek.")

@login_required
def greeting_view_user(request):
    """Powitanie użytkownika."""
    user = request.user
    return HttpResponse("Witaj w witrynie Bookr! {username}".format(username=user))