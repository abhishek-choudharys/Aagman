from django.shortcuts import render, get_object_or_404
from .models import Category, Product,Review
from cart.forms import CartAddProductForm
from django.db.models import Q

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
    search_term = ''
    if 'search' in request.GET:
        products = Product.objects.all()
        products = products.filter(Q(name__icontains=search_term)| Q(category__name__icontains=search_term)| Q(description__icontains=search_term))
        search_term = request.GET['search']
        if 'pop' in request.GET:
            products = products.order_by('-no_of_views')
        if 'priceasc' in request.GET:
            products = products.order_by('price')
        if 'pricedesc' in request.GET:
            products = products.order_by('-price')
        context={
            'products': products,
            'search_term': search_term
        }
        return render(request, 'product-list.html', context)
    else:
        if 'pop' in request.GET:
            products= products.order_by('-no_of_views')
        if 'priceasc' in request.GET:
            products = products.order_by('price')
        if 'pricedesc' in request.GET:
            products = products.order_by('-price')
        context = {
            'category': category,
            'categories': categories,
            'products': products,
        }
        return render(request, 'product-list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    if 'search' in request.GET:
        products = Product.objects.all()
        print(products)
        search_term = request.GET['search']
        products = products.filter(name__icontains=search_term)
        context={
            'products': products,
            'search_term': search_term
        }
        return render(request, 'product-list.html', context)
    else:
        ratings_reviews = Review.objects.filter(product = product)
        request.session.setdefault('history', []).append(product.name)
        request.session.modified = True
        star1 = 0
        star2 = 0
        star3 = 0
        star4 = 0
        star5 = 0
        totalstar=0
        for i in ratings_reviews:
            totalstar+=1
            if(i.rating==1):
                star1+=1
            elif (i.rating == 2):
                star2 += 1
            elif (i.rating == 3):
                star3 += 1
            elif (i.rating == 4):
                star4 += 1
            elif (i.rating == 5):
                star5 += 1
        if(totalstar == 0):
            totalstar=1
        star1per = star1/totalstar*100
        star2per = star2 / totalstar*100
        star3per = star3 / totalstar*100
        star4per = star4 / totalstar*100
        star5per = star5 / totalstar*100
        avgstar = (star1*1+star2*2+star3*3+star4*4+star5*5)/totalstar
        product.no_of_views=(product.no_of_views)+1
        product.save(update_fields=["no_of_views"])
        context = {
            'product': product,
            'cart_product_form': cart_product_form,
            'ratings_reviews':ratings_reviews,
            'star1': star1,
            'star2': star2,
            'star3': star3,
            'star4': star4,
            'star5': star5,
            'totalstar': totalstar,
            'star1per': star1per,
            'star2per': star2per,
            'star3per': star3per,
            'star4per': star4per,
            'star5per': star5per,
            'avgstar': avgstar,
        }
        return render(request, 'product-detail.html', context)

def HomePage(request,category_slug=None):

    if 'search' in request.GET:
        products = Product.objects.all()
        print(products)
        search_term = request.GET['search']
        products = products.filter(Q(name__icontains=search_term)| Q(category__name__icontains=search_term)| Q(description__icontains=search_term))
        context={
            'products': products,
            'search_term': search_term
        }
        return render(request, 'product-list.html', context)
    else:

        category = None
        categories = Category.objects.all()
        products = Product.objects.filter(available=True)
        trending = Product.objects.all().order_by('-no_of_views')
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products = Product.objects.filter(category=category)
        context = {
            'category': category,
            'categories': categories,
            'products': products,
            'trending': trending
        }
        return render(request, 'homepage.html',context)
