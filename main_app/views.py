from django.shortcuts import render, redirect
from .models import DishCategory, Dish, Gallery
from .forms import ReservationForm


# Create your views here.
def main_view(request):
    if request.method == 'POST':
        form_reserve = ReservationForm(request.POST)
        if form_reserve.is_valid():
            form_reserve.save()
            return redirect('/')


    categories = DishCategory.objects.filter(is_visible=True)
    dishes = Dish.objects.filter(is_visible=True, is_special=False, is_signature=False)
    special_dishes = Dish.objects.filter(is_visible=True, is_special=True)
    signature_dishes = Dish.objects.filter(is_signature=True, is_visible=True)
    gallery = Gallery.objects.all()
    form_reserve = ReservationForm()
    return render(request, 'main_page.html', context={
        'categories': categories,
        'dishes': dishes,
        'special_dishes': special_dishes,
        'signature_dishes': signature_dishes,
        'gallery': gallery,
        'form_reserve': form_reserve,
    })
