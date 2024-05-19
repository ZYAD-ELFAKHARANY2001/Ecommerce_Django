from django.db import models

# Create your models here.
class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()
class Category(models.Model):
    Title = models.CharField(max_length=255)
    featuredProduct = models.ForeignKey("Product", on_delete=models.SET_NULL,null=True,related_name='+')

class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, default=99.99)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    Promotions = models.ManyToManyField(Promotion)

    def __str__(self):
        return self.title

class Customer(models.Model):
    MemberShip_Bronze ='B'
    MemberShip_Silver ='S'
    MemberShip_Gold ='G'

    MEMBERSHIP_CHOICES = [
        (MemberShip_Bronze, 'Bronze'),
        (MemberShip_Silver, 'Silver'),
        (MemberShip_Gold, 'Gold'),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MemberShip_Bronze)

    class Meta:
        db_table = 'store_customer'
        indexes = [
            models.Index(fields=['last_name', 'first_name']),
        ]

class Order(models.Model):
    Payment_Status_Pending ='P'
    Payment_Status_Complete ='C'
    Payment_Status_Failed ='F'

    PAYMENT_STATUS_CHOICES = [
        (Payment_Status_Pending, 'Pending'),
        (Payment_Status_Complete, 'Complete'),
        (Payment_Status_Failed, 'Failed'),
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICES, default=Payment_Status_Pending)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    zip = models.CharField(max_length=100,null=True)



