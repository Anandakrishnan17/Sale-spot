from django import forms
from .models import Listing, ListingImage

STATE_CHOICES = [
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Goa', 'Goa'),
    ('Gujarat', 'Gujarat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jharkhand', 'Jharkhand'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Uttarakhand', 'Uttarakhand'),
    ('West Bengal', 'West Bengal'),
    ('Chandigarh', 'Chandigarh'),
    ('Delhi', 'Delhi'),
    ('Lakshadweep', 'Lakshadweep'),
    ('Puducherry', 'Puducherry'),
]

CATEGORY_CHOICES = [
        ('cars', 'Cars'),
        ('bikes', 'Bikes'),
        ('mobiles', 'Mobiles'),
        ('pets', 'Pets'),
        ('fashion', 'Fashion'),
        ('books', 'Books'),
        ('furniture', 'Furniture'),
        ('electronics', 'Electronics & Appliances'),
        ('properties', 'Properties'),
        ('sports', 'Sports'),
        ('commercial_vehicle', 'Commercial Vehicle Spares'),
        ('other', 'Other'),
    ]
CONDITION_CHOICES = [
        ('used', 'Used'),
        ('new', 'New'),
    ]



class ListingForm(forms.ModelForm):

    category = forms.ChoiceField(choices=CATEGORY_CHOICES)
    condition = forms.ChoiceField(choices=CONDITION_CHOICES)
    phone_number = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))

    class Meta:
        model = Listing
        fields = [ 'title','description','category','condition', 'price', 'state','phone_number']

    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control',}))
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}))
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, widget=forms.Select(attrs={'class': 'form-control', 'style': 'height: 39px; border: 1px solid #d5c8c8; border-radius: 7px;'}))
    condition = forms.ChoiceField(choices=CONDITION_CHOICES, widget=forms.Select(attrs={'class': 'form-control', 'style': 'height: 39px; border: 1px solid #d5c8c8; border-radius: 7px;'}))
    price = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    state = forms.ChoiceField(choices=STATE_CHOICES, widget=forms.Select(attrs={'class': 'form-control', 'style': 'height: 39px; border: 1px solid #d5c8c8; border-radius: 7px;'}))
    phone_number = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.seller = self.user  
            instance.save()
        return instance


class ListingImageForm(forms.ModelForm):
    class Meta:
        model = ListingImage
        fields = ['image']

ListingImageFormSet = forms.modelformset_factory(ListingImage, form=ListingImageForm, extra=4)




