# 📚 Bookr – Platforma recenzji książek (Django)

Projekt **Bookr** to aplikacja internetowa zbudowana w Django, umożliwiająca przeglądanie książek, dodawanie recenzji oraz zarządzanie treścią. Stworzony na potrzeby nauki frameworka Django według książki _"Django. Tworzenie nowoczesnych aplikacji internetowych w Pythonie"_

![Image](https://github.com/user-attachments/assets/d955c860-c3fc-4bc9-a06d-50f9c59a514c)
<sub>Rys. 1. Strona główna aplikacji Bookr.</sub>

---

## 🛠 Funkcjonalności

- Przeglądanie książek i recenzji
- Dodawanie nowych książek i opinii (dla zalogowanych użytkowników)
- Panel administracyjny Django
- Własne modele danych (książki, autorzy, recenzje)
- Obsługa mediów (okładki książek)
- Rejestracja i logowanie użytkowników
- REST API (opcjonalnie w rozszerzeniu projektu)

---

## 🧩 Struktura projektu

| 📁 bookr/                                     | Katalog główny                                |
|:----------------------------------------------|:----------------------------------------------|
| 📁 .venv/                                     | Środowisko wirtualne (ignorowane przez Git)   |
| 📁 bookr/                                     | Główna konfiguracja Django (settings, urls)   |
| &nbsp;&nbsp;&nbsp;&nbsp;├── 📄 __init__.py    | Plik inicjalizujący moduł                     |
| &nbsp;&nbsp;&nbsp;&nbsp;├── 📄 asgi.py        | Konfiguracja ASGI                             |
| &nbsp;&nbsp;&nbsp;&nbsp;├── 📄 settings.py    | Ustawienia projektu                           |
| &nbsp;&nbsp;&nbsp;&nbsp;├── 📄 urls.py        | Definicje URL-i                               |
| &nbsp;&nbsp;&nbsp;&nbsp;└── 📄 wsgi.py        | Konfiguracja WSGI                             |
| 📁 reviews/                                   | Aplikacja do obsługi książek i recenzji       |
| &nbsp;&nbsp;&nbsp;&nbsp;├── 📁 migrations/    | Migracje bazy danych                          |
| &nbsp;&nbsp;&nbsp;&nbsp;├── 📄 __init__.py    | Plik inicjalizujący moduł                     |
| &nbsp;&nbsp;&nbsp;&nbsp;├── 📄 admin.py       | Rejestracja modeli w panelu admina            |
| &nbsp;&nbsp;&nbsp;&nbsp;├── 📄 apps.py        | Konfiguracja aplikacji                        |
| &nbsp;&nbsp;&nbsp;&nbsp;├── 📄 models.py      | Definicje modeli                              |
| &nbsp;&nbsp;&nbsp;&nbsp;├── 📄 tests.py       | Testy jednostkowe                             |
| &nbsp;&nbsp;&nbsp;&nbsp;└── 📄 views.py       | Widoki aplikacji                              |
| 📁 bookr_admin/                               | Rozszerzenia panelu administracyjnego         |
| 📁 bookr_test/                                | Testy jednostkowe i integracyjne              |
| 📁 templates/                                 | Szablony HTML                                 |
| 📁 static/                                    | Pliki statyczne (CSS, JS, obrazy)             |
| 📁 media/                                     | Przesyłane pliki użytkowników (np. okładki)   |
| 📄 .gitignore                                 | Lista plików ignorowanych przez Git           |
| 📄 manage.py                                  | Narzędzie do zarządzania projektem Django     |
| 📄 db.sqlite3                                 | Baza danych SQLite                            |
| 📄 requirements.txt                           | Lista zależności Pythona                      |
| 📄 README.md                                  | Dokumentacja projektu                         |

---

## ⚙️ Etapy projektu

### 1. Wprowadzenie do Django i projektu Bookr
- Instalacja Django i konfiguracja środowiska.
- Struktura projektu Django.
- Tworzenie aplikacji i uruchamianie serwera deweloperskiego.
### 2. Modele i relacje
- Tworzenie modeli Django i pól bazodanowych.
- Relacje między modelami: OneToMany i ManyToMany.
- Migracje i korzystanie z ORM.
### 3. Panel administracyjny
- Rejestracja modeli w panelu admina.
- Dostosowanie widoków administracyjnych.
- Filtry, pola wyszukiwania i pola tylko do odczytu.
### 4. Widoki i szablony
- Tworzenie widoków funkcjonalnych i klasowych.
- Przekazywanie danych do szablonów.
- Tworzenie i dziedziczenie szablonów HTML.
### 5. Uwierzytelnianie i autoryzacja
- Tworzenie użytkowników, logowanie, wylogowywanie.
- Ochrona widoków i ról użytkowników.
- Szablony z treściami zależnymi od zalogowania.
### 6. Tworzenie API z Django REST Framework
- Serializatory i widoki API.
- Endpointy do pobierania i zapisywania danych.
- Autoryzacja na poziomie API.
### 7. Testowanie aplikacji
- Testy jednostkowe modeli i widoków.
- Testy integracyjne z użyciem klienta Django.
- Korzyści z pokrycia testami.

---

## 📘 Źródło

Ten projekt został wykonany na podstawie książki:

_Django. Tworzenie nowoczesnych aplikacji internetowych w Pythonie_  
Autor: Ben Shaw  
Wydawnictwo: Helion
