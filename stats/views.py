import shopify
from django.shortcuts import render
from shopify_auth.decorators import login_required


@login_required
def home(request, *args, **kwargs):

    # Get a list of the user's products.
    with request.user.session:
        products = shopify.Product.find()

    return render(request, "stats/home.html", {'products': products})
