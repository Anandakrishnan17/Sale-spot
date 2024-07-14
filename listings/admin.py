from django.contrib import admin
from .models import Listing, ListingImage

class ListingImageInline(admin.TabularInline):
    model = ListingImage
    extra = 4  

class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'seller', 'category', 'condition', 'price', 'state', 'created_at')
    search_fields = ('title', 'description', 'category', 'state')
    list_filter = ('category', 'condition', 'state')
    inlines = [ListingImageInline]

admin.site.register(Listing, ListingAdmin)
admin.site.register(ListingImage)

