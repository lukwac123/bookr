"""
URL configuration for bookr project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import reviews.views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from bookr.views import profile, reading_history

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(('django.contrib.auth.urls', 'auth'), namespace='accounts')),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/profile/reading_history', reading_history, name='reading_history'),
    path('', reviews.views.index),
    path('book-search/', reviews.views.book_search, name='book_search'),
    path('', include('reviews.urls')),
    path('', include('bookr_test.urls')),  
    path('react-example/', reviews.views.react_example),
]

if settings.DEBUG:
    
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    import debug_toolbar
    
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
