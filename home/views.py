from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from listings.models import Listing
from listings.forms import CATEGORY_CHOICES
from django.urls import reverse_lazy

from django.shortcuts import render
from listings.models import Listing
from listings.forms import CATEGORY_CHOICES

def home(request):
    listings = Listing.objects.all()

    # Fetch state, category, search query, min_price, and max_price from GET request
    state = request.GET.get('state')
    category = request.GET.get('category')
    search_query = request.GET.get('search')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if state:
        listings = listings.filter(state=state)

    if category:
        listings = listings.filter(category=category)

    if search_query:
        listings = listings.filter(title__icontains=search_query.lower())

    if min_price:
        listings = listings.filter(price__gte=min_price)

    if max_price:
        listings = listings.filter(price__lte=max_price)
    
    

    context = {
        'listings': listings,
        'state': state,
        'category': category,
        'search_query': search_query,
        'min_price': min_price,
        'max_price': max_price,
        'CATEGORY_CHOICES': CATEGORY_CHOICES,
    }

    return render(request, 'homepage/home.html', context)


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'homepage/register.html'
    success_url = reverse_lazy('home:login')  

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home:home')  
        return super().get(request, *args, **kwargs)

class CustomLoginView(LoginView):
    template_name = 'homepage/login.html'

    def get_success_url(self):
        return reverse_lazy('home:home')

def logout_view(request):
    logout(request)
    return redirect('home_app:home')

def profile(request):
    user_listings = Listing.objects.filter(seller=request.user)
    return render(request, 'homepage/profile_page.html', {'listings': user_listings})
