from django.urls import path
from .views import *

urlpatterns = [
    path('Product/', ProductApiView.as_view()),
    path('Product/<int:pk>/', ProductApiView.as_view()),

    path('Manufacture/', ManufacturerApiView.as_view()),
    path('Manufacture/<int:pk>/', ManufacturerApiView.as_view()),

    path('Category/', CategoryApiView.as_view()),
    path('Category/<int:pk>/', CategoryApiView.as_view()),

]
