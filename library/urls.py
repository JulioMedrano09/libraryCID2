from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='book'),
    path('<letter>', views.index, name='book'),
    path('view/<int:id>', views.view, name='book_view')
]

