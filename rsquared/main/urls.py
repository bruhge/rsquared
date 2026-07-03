from django.urls import path
from .views import index, contact, evaluations, therapy, speciality, modalities

urlpatterns = [
    path('', index, name='home'),
    path('contact/', contact, name='contact'),
    path('evaluations/', evaluations, name='evaluations'),
    path('therapy/', therapy, name='therapy'),
    path('speciality/', speciality, name='speciality'),
    path('modalities/', modalities, name='modalities'),
]