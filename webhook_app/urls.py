

from django.urls import path
from . import views

app_name = 'webhook_app'

urlpatterns = [
    path('create_webhook/', views.create_webhook, name='create_webhook'),
    path('<str:webhook_id>/', views.webhook_detail, name='webhook_detail'),
]





