"""myFirstProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.calculator, name='calculator')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='calculator')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from calculator.views import create_cal
from calculator.views import default
from calculator.views import wrong

urlpatterns = [
    path('<int:x>/<str:d>/<int:y>', create_cal),
    path('', default),
    path('<int:x>/<str:d>/<str:y>', wrong),
    path('<str:x>/<str:d>/<int:y>', wrong),
    path('<str:x>/<str:d>/<str:y>', wrong)
]
