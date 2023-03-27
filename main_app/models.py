from django.db import models
from django.core.validators import RegexValidator

class DishCategory(models.Model):
    title = models.CharField(max_length=50, unique=True)
    position = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)

    def __iter__(self):
        for dish in self.dishes.all():
            yield dish

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('position', )
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Dish(models.Model):
    title = models.CharField(max_length=50, unique=True)
    position = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)
    category = models.ForeignKey(DishCategory, related_name='dishes', on_delete=models.CASCADE)
    is_special = models.BooleanField(default=False)
    is_signature = models.BooleanField(default=False)
    desc = models.TextField(max_length=200, blank=True, verbose_name='about dish')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.PositiveSmallIntegerField(default=0)
    ingredients = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='dishes')
    is_recommended = models.BooleanField(default=False)


    def total_price(self):
        return self.price - self.discount / 100 * self.price

    class Meta:
        ordering = ('position',)
        verbose_name = 'Dish'
        verbose_name_plural = 'Dishes'

    def __str__(self):
        return f'{self.title}'


class Gallery(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='gallery')


class Reservation(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=16)
    visit_datetime = models.DateTimeField()
    date_request = models.DateTimeField(auto_now_add=True)
    date_response = models.DateTimeField(auto_now=True)
    guests = models.PositiveSmallIntegerField(default=2)
    message = models.TextField(max_length=1000, blank=True)
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}\t{self.phone}\t{self.email}'

    class Meta:
        ordering = ('-date_request', )







