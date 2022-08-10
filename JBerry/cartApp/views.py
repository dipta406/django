from email.mime import image
from django.shortcuts import redirect,render
from django.contrib.auth.decorators import login_required
from .models import cartItem
from productApp.models import Product

# Create your views here.
@login_required
def viewCart(request, uid):
    cartitmes = cartItem.objects.filter(uid=uid, in_cart=True)
    cartItems = []
    cart_total = 0.0

    for item in cartitmes:
        product = Product.objects.get(pid=item.pid)
        citems = {
            "pid": product.pid,
            "title": product.title,
            "image": product.image,
            "qty": item.qty,
            "price": float(product.price) * float(item.qty),
        }
        cartItems.append(citems)
        cart_total = cart_total + citems["price"]
    return render(
        request, "cart.html", context={"items": cartItems, "cart_total": cart_total, 'CartCount': request.session['CartCount']}
    )


@login_required
def addToCart(request):
    if request.method == "POST":
        uid = request.POST["uid"]
        pid = request.POST["pid"]
        qty = request.POST["qty"]
        cartitem = cartItem(pid=pid, uid=uid, qty=qty)
        cartitem.save()
        return redirect('home')
    return render(request, "cart.html", context={'CartCount': request.session['CartCount'],})
