from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    description = models.TextField(max_length=450, blank=False, null=False)
    image = models.ImageField(upload_to="images/", blank=False, null=False)
    price = models.IntegerField(blank=False, null=False)
    category = models.ForeignKey(Category, blank=False, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class Customer(models.Model):
    phone_number = models.CharField(max_length=50, blank=False, null=False)
    first_name = models.CharField(max_length=150, blank=False, null=False)
    last_name = models.CharField(max_length=150, blank=False, null=False)

    def __str__(self):
        return self.first_name


class Order(models.Model):
    address = models.CharField(max_length=100, blank=False, null=False)
    status = models.CharField(max_length=100, blank=False, null=False)
    payment_type = models.CharField(max_length=100, blank=False, null=False)
    customer = models.ForeignKey(Customer, blank=False, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.address


class OrderProduct(models.Model):
    amount = models.CharField(max_length=100, blank=False, null=False)
    price = models.IntegerField(blank=False, null=False)
    product = models.ForeignKey(Product, blank=False, null=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, blank=False, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.amount




