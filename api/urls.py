from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session),
    path('success/', views.success, name='success'),
    path('cancelled/', views.cancel, name='cancel'),
    path('webhook/', views.stripe_webhook),
]
