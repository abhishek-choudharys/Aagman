from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
        return render(request, 'created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'create.html', {'form': form})

def MyOrders(request):
    myorderlist = OrderItem.objects.filter(order = request.user)
    print(myorderlist)
