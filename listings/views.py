from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from .models import Listing, ListingImage
from .forms import ListingForm,ListingImageForm
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import View
from .models import Listing, CATEGORY_CHOICES


def add_listing(request, listing_id=None):
    ListingImageFormSet = modelformset_factory(ListingImage, form=ListingImageForm, extra=4, can_delete=True)

    if listing_id:
        listing = get_object_or_404(Listing, id=listing_id)
    else:
        listing = None

    if request.method == 'POST':
        listing_form = ListingForm(request.POST, instance=listing)
        formset = ListingImageFormSet(request.POST, request.FILES, queryset=ListingImage.objects.filter(listing=listing))

        if listing_form.is_valid() and formset.is_valid():
            listing = listing_form.save(commit=False)
            listing.seller = request.user  # Assign the current user as the seller
            listing.save()

            for form in formset.cleaned_data:
                if form:
                    image = form.get('image')
                    if image:
                        ListingImage.objects.create(listing=listing, image=image)

            return redirect('home_app:home')
    else:
        listing_form = ListingForm(instance=listing)
        formset = ListingImageFormSet(queryset=ListingImage.objects.filter(listing=listing))

    return render(request, 'listings/add_listing.html', {'listing_form': listing_form, 'formset': formset})


class ListingListView(ListView):
    model = Listing
    template_name = 'listings/listing_list.html'
    context_object_name = 'listings'
    paginate_by = 9 

    def get_queryset(self):
        queryset = Listing.objects.all()

        state = self.request.GET.get('state')
        category = self.request.GET.get('category')
        search = self.request.GET.get('search')

        if state:
            queryset = queryset.filter(state=state)
        if category:
            queryset = queryset.filter(category=category)
        if search:
            queryset = queryset.filter(title__icontains=search)

        return queryset
    
def search(request):
    query = request.GET.get('search')
    if query:
        listings = Listing.objects.filter(title__icontains=query)
    else:
        listings = Listing.objects.all()
    return render(request, 'listing_page.html', {'listings': listings})
    
def listing_list(request):
    category = request.GET.get('category', 'all')
    state = request.GET.get('state', None)
    
    listings = Listing.objects.all()
    
    if category and category != 'all':
        listings = listings.filter(category=category)
    
    if state:
        listings = listings.filter(state=state)

    context = {
        'listings': listings,
        'category': category,
        'state': state,
    }
    
    return render(request, 'listings/listing_list.html', context)

def listing_details(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    return render(request, 'listings/listing_details.html', {'listing': listing})

def contact_seller(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    return render(request, 'listings/contact_seller.html', {'listing': listing})

    
class ListingDeleteView(LoginRequiredMixin, View):
    template_name = 'listings/listing_delete.html'

    def get(self, request, listing_id):
        listing = get_object_or_404(Listing, pk=listing_id, seller=request.user)
        context = {'listing': listing}
        return render(request, self.template_name, context)

    def post(self, request, listing_id):
        listing = get_object_or_404(Listing, pk=listing_id, seller=request.user)
        if listing.seller == request.user:
            listing.delete()
        return redirect('home:profile')  


   