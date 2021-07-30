"""cuenta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from cuenta.views import saludo, saludo2, hija1, hija2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/',saludo),
    path('saludo2/',saludo2),
    path('hija1/',hija1),
    path('hija2/',hija2),
    path("", include("authentication.urls")), # Auth routes - login / register
    path("", include("app.urls"))             # UI Kits Html files
]
