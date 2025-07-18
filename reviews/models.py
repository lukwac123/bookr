from django.db import models
from django.contrib import auth

class Publisher(models.Model):
    """Firma wydająca ksiązki"""
    name = models.CharField(max_length=50, help_text="Nazwa wydawnictwa.")
    website = models.URLField(help_text="Witryna wydawnictwa.")
    email = models.EmailField(help_text="Adres e-mail wydawnictwa.")

    def __str__(self):
        return self.name


class Book(models.Model):
    """Opublikowana książka"""
    title = models.CharField(max_length=70, help_text="Tytuł książki.")
    publication_date = models.DateField(verbose_name="Data publikacji książki.")
    isbn = models.CharField(max_length=20, verbose_name="Numer ISBN książki.")
    
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    contributors = models.ManyToManyField('Contributor', through="BookContributor")

    cover = models.ImageField(null=True, blank=True, upload_to="book_covers/")
    sample = models.FileField(null=True, blank=True, upload_to="book_samples/")

    def __str__(self):
        return self.title


class Contributor(models.Model):
    """Współtwórca książki, np. autor, redaktor, współautor"""
    first_names = models.CharField(max_length=50, help_text="Imię lub imiona współtwórcy.")
    last_names = models.CharField(max_length=50, help_text="Nazwisko lub nazwiska współtwórcy.")
    email = models.EmailField(help_text="E-mail współtwórcy.")

    def initialled_name(self):
        initials = ''.join([name[0] for name in self.first_names.split(' ')])
        return "(), ()".format(self.last_names, initials)
    
    def number_contributions(self):
        return self.bookcontributor_set.count()

    def __str__(self):
        return self.initialled_name()
        

class BookContributor(models.Model):
    class ContributionRole(models.TextChoices):
        AUTHOR = "AUTHOR", "Author"
        CO_AUTHOR = "CO_AUTHOR", "Co-Author"
        EDITOR = "EDITOR", "Editor"

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    role = models.CharField(verbose_name="Rola, jaką współtwórca odegrał podczas tworzenia tej książki.", choices=ContributionRole.choices, max_length=20)

class Review(models.Model):
    content = models.TextField(help_text="Tekst recenzji.")
    rating = models.IntegerField(help_text="Ocena uzytkownika.")
    date_created = models.DateTimeField(auto_now_add=True, help_text="Data i czas utworzenia recenzji.")
    date_edited = models.DateTimeField(null=True, help_text="Data i czas ostatniej edycji recenzji.")
    creator = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, help_text="Recenzowana książka.")
