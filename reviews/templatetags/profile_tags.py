from django import template
from reviews.models import Review

register = template.Library()

@register.inclusion_tag('book_list.html')
def book_list(username):
    """Renderowanie listy książek przeczytanych przez użytkownika.
    :param: str username Nazwa użytkownika, którego książki należy pobrać
    :return: Słownik książek przeczytanych przez użytkownika.
    """
    reviews = Review.objects.filter(creator__username__contains=username)
    book_list = [review.book.title for review in reviews]

    return {'books_read': book_list}