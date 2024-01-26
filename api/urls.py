from django.urls import path

from .views import (
    HomePageView,
    ItemPageView,
    SuccessView,
    CancelView,
    CreateCheckoutSessionView,
    CreateCheckoutCartSessionView,
    stripe_config,
    stripe_webhook,
    AddToCartView,
    CartView,
    clear_cart
)


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('success/', SuccessView.as_view(), name='success'),
    path('cancelled/',  CancelView.as_view(), name='cancel'),
    path('item/<int:pk>/', ItemPageView.as_view(), name='item_page'),
    path('buy/<int:pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('buy-cart/', CreateCheckoutCartSessionView.as_view(), name='create-checkout-session-cart'),
    path('config/', stripe_config),
    path('webhook/', stripe_webhook),
    path('add-to-cart/<int:item_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('clear-cart/', clear_cart, name='clear_cart'),
    path('cart/', CartView.as_view(), name='cart'),
]
