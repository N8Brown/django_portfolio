from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('<project_slug>', project, name='project'),
]