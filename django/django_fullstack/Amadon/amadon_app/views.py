from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "index.html", context)

def buy(request):
    if request.method == 'POST':
        product_id = request.POST['product_id']
        quantity = int(request.POST['quantity'])
        product = Product.objects.get(id=product_id)
        total_charge = float(product.price) * quantity  

       
        Order.objects.create(product=product, quantity_ordered=quantity, total_price=total_charge)

       
        request.session['total_charge'] = float(total_charge)  
        request.session['total_quantity'] = quantity

        return redirect('/checkout')
    return redirect('/')

def checkout(request):
    total_charge = request.session.get('total_charge', 0)
    total_quantity = request.session.get('total_quantity', 0)
    context = {
        'total_charge': total_charge,
        'total_quantity': total_quantity,
        'total_orders': Order.objects.count(),
        'total_amount': sum(float(order.total_price) for order in Order.objects.all())  
    }
    return render(request, "checkout.html", context)