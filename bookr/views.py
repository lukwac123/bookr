from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from plotly.offline import plot
import plotly.graph_objects as graphs

from .utils import get_books_read_by_month

@login_required
def profile(request):
    user = request.user
    permissions = user.get_all_permissions()
    # Pobieranie książek przeczytanych w poszczególnych miesiącach bieżącego roku.
    books_read_by_month = get_books_read_by_month(user.username)

    """Inicjalizacja osi wykresu. Oś X przedstawia miesiące, oś Y liczbę przeczytanych książek"""
    months = [i+1 for i in range(12)]
    books_read = [0 for _ in range(12)]

    # Ustawienie liczby przeczytanych książek w miesiącu na osi Y
    for num_books_read in books_read_by_month:
        list_index = num_books_read['date_created__month'] - 1
        books_read[list_index] = num_books_read['book_count']

    # Generowanie kodu HTML wykresu punktowego
    figure = graphs.Figure()
    scatter = graphs.Scatter(x=months, y=books_read)
    figure.add_trace(scatter)
    figure.update_layout(xaxis_title="Miesiąc", yaxis_title="Liczba przeczytanych książek")
    plot_html = plot(figure, output_type='div')

    # Dodawanie szablonów 
    return render(request, 'profile.html', {'user': user, 'permissions': permissions, 'books_read_plot': plot_html})
