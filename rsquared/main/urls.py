from django.urls import path
from .views import index, contact, evaluations, therapy, speciality, modalities

urlpatterns = [
    path('', index, name='home'),
    path('contact/', contact, name='contact'),
    path('evaluations/', evaluations, name='evaluations'),
    path('therapy/', therapy, name='therapy'),
    path('Specialties/', speciality, name='Specialties'),
    path('modalities/', modalities, name='modalities'),
]