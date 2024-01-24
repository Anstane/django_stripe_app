import stripe
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView, View

from .models import Item, Order, OrderItem


class HomePageView(TemplateView):
    """Главная страница со всеми объектами."""

    template_name = 'main/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = Item.objects.all()
        return context


class ItemPageView(TemplateView):
    """Страница с конкретным объектом."""

    template_name = 'main/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        item_id = self.kwargs.get('pk')
        item = get_object_or_404(Item, pk=item_id)
        context['item'] = item
        return context


class SuccessView(TemplateView):
    """Успешная оплата."""

    template_name = 'main/success.html'


class CancelView(TemplateView):
    """Отмена оплаты."""

    template_name = 'main/cancelled.html'


@csrf_exempt
def stripe_config(request):
    """Функция для получения токена."""

    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)


class CreateCheckoutSessionView(View):
    """Оплата товара."""

    def get(self, request, *args, **kwargs):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        item_id = self.kwargs["pk"]
        item = Item.objects.get(id=item_id)
        try:
            domain_url = settings.MY_DOMAIN
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                mode='payment',
                success_url=domain_url + '/success/',
                cancel_url=domain_url + '/cancelled/',
                line_items=[
                    {
                        'price': item.price_stripe_id,
                        'quantity': 1,
                    },
                ],
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        print("Payment was successful.")

    return HttpResponse(status=200)


class CartView(TemplateView):
    """Вью для корзины."""

    template_name = 'main/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order, created = Order.objects.get_or_create()
        context['cart'] = order
        return context


class AddToCartView(View):
    """Добавление предмета в корзину."""

    def post(self, request, item_id, *args, **kwargs):
        item = Item.objects.get(id=item_id)
        order, created = Order.objects.get_or_create()

        order_item, created = OrderItem.objects.get_or_create(
            order=order,
            item=item
        )

        order_item.quantity += 1
        order_item.save()

        return JsonResponse({'status': 'success'})


def clear_cart(request):
    """Чистка корзины."""

    OrderItem.objects.all().delete()
    return redirect('cart')
