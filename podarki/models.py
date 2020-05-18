from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.sessions.models import Session


class ShopUser(User):
    phone_number = models.CharField(max_length=20)


class ShopCategory(models.Model):
    name = models.CharField(max_length=50)


class ShopEntry(models.Model):
    title = models.CharField(max_length=100, help_text='Enter the title')
    description = models.TextField(blank=True, help_text='Description for shop entry')
    price = models.PositiveIntegerField(blank=True, null=True)
    buy_link = models.CharField(max_length=100, help_text='Link to shop where you can buy it', blank=True, null=True)
    category = models.ManyToManyField(ShopCategory)

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of MyModelName.
        """
        return reverse('shop:detail', args=[str(self.id)])

    def __str__(self):
        return self.title


class Photo(models.Model):
    entry = models.ForeignKey(ShopEntry, on_delete=models.CASCADE)
    content = models.ImageField(upload_to='photos')
    description = models.CharField(max_length=150, help_text='Photo description')


class UserAddress(models.Model):
    user = models.ForeignKey(ShopUser, on_delete=models.CASCADE)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    building = models.CharField(max_length=5)
    apartments_number = models.CharField(max_length=5, null=True, blank=True)


class ShopCart(models.Model):
    entries = models.ManyToManyField(ShopEntry, through='ShopCartEntry')
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def get_total_price(self):
        res = 0
        for entry in self.entries.get():
            res += int(entry.price)
        return res


class ShopCartEntry(models.Model):
    cart = models.ForeignKey(ShopCart, on_delete=models.CASCADE)
    entry = models.ForeignKey(ShopEntry, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True)
