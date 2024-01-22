from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('cancelled/',  views.CancelView.as_view(), name='cancel'),
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session, name='create_checkout_session'),
    path('webhook/', views.stripe_webhook),
    path('item/<int:pk>/', views.ItemPageView.as_view(), name='item_page'),
]
