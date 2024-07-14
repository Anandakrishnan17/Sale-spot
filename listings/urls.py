from django.urls import path
from listings import views
from .views import ListingListView

app_name = 'listings'

urlpatterns = [
    path('add/', views.add_listing, name='add_listing'),
    path('listings/',ListingListView.as_view(), name='listing_list'),
    path('listing/<int:listing_id>/', views.listing_details, name='listing_details'),
    path('listings/<int:listing_id>/contact/', views.contact_seller, name='contact_seller'),
    path('edit/<int:listing_id>/', views.add_listing, name='edit_listing'),
    path('delete/<int:listing_id>/', views.ListingDeleteView.as_view(), name='delete_listing'),
]
