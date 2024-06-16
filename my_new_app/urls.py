from django.urls import path
from my_new_app.views import greeting_user

urlpatterns = [
    path('greeting/<str:your_name>/', greeting_user)
]