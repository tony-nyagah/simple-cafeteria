from django.db import models


class FoodItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to="food_images/")


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()


class Order(models.Model):
    class status(models.TextChoices):
        PAID = "Paid"
        UNPAID = "Unpaid"

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(FoodItem)
    total_price = models.DecimalField(max_digits=5, decimal_places=2)
    order_status = models.CharField(max_length=10, choices=status.choices)
    order_date = models.DateTimeField(auto_now_add=True)
