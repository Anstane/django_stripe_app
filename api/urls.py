from django.urls import path

from .views import (
    HomePageView,
    ItemPageView,
    SuccessView,
    CancelView,
    CreateCheckoutSessionView,
    stripe_config,
    stripe_webhook
)


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('success/', SuccessView.as_view(), name='success'),
    path('cancelled/',  CancelView.as_view(), name='cancel'),
    path('config/', stripe_config),
    path('webhook/', stripe_webhook),
    path('item/<int:pk>/', ItemPageView.as_view(), name='item_page'),
    path('create-checkout-session/<int:pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session')
]
