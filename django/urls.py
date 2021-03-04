from django.urls import path
from . import views

urlpatterns = [
    path('<str:_type>/', views.TRANSLATE_API),
    # path('xml/', views.XML_API)#.as_view())
]