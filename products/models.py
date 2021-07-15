from django.db import models
from django.contrib.auth.models import User
from base.models import Custom_User


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    image = models.FileField(upload_to='category', default='now')

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)


class Sub_Category(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to='products/')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)

    sub_category = models.ForeignKey(
        Sub_Category, on_delete=models.SET_NULL, null=True)

    product_id = models.CharField(max_length=30, blank=True, null=True)
    description = models.TextField()
    tags = models.CharField(max_length=100, blank=True, null=True)
    tag_list = models.CharField(max_length=100, blank=True, null=True)
    brand = models.CharField(max_length=30, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    views = models.IntegerField(default=0, blank=True, null=True)

    discount_price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)

    discount_percent = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)

    featured_post = models.BooleanField(default=False, blank=True, null=True)
    video = models.FileField(
        upload_to='products/video/', default='product_video', blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.tags is not None and self.tags != '':
            self.tag_list = list(
                map(lambda x: x.strip(), self.tags.split(',')))
        else:
            self.tag_list = '["No Tags"]'
        super(Product, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.image.delete()
        self.video.delete()
        super().delete(*args, **kwargs)

    def rating(self):
        ratings = Rating.objects.filter(product=self)

        stars = 0
        for rating in ratings:
            stars += rating.star

        try:
            avg_rating = stars / len(ratings)
        except ZeroDivisionError:
            avg_rating = 'Not rated'

        return avg_rating


class DeliveryAddress(models.Model):
    types = (
        ('Home', 'Home'),
        ('Office', 'Office'),
        ('Business', 'Business'),
    )
    address_type = models.CharField(max_length=15, choices=types)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    postalCode = models.CharField(max_length=200, null=True, blank=True)
    shippingPrice = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.address_type + ': ' + self.address


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.user) + ': ' + str(self.product) + ' (' + str(self.quantity) + ')'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_ids = models.CharField(max_length=200, null=True)
    product_ids = models.CharField(max_length=200)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True)
    tran_id = models.CharField(max_length=20, null=True)

    delivery_charge = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    delivery_address = models.TextField()

    confirm = models.BooleanField(default=False)
    paid_at = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    is_delivered = models.BooleanField(default=False)
    delivered_at = models.DateTimeField(
        auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return str(self.user) + ': ' + str(self.created_at) + '; Confirm: ' + str(self.confirm)

    def save(self, *args, **kwargs):
        carts = Cart.objects.filter(user=self.user)
        carts.delete()
        super(Order, self).save(*args, **kwargs)


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user) + ': ' + self.comment[0:20]

    def user_avatar(self):
        user = Custom_User.objects.get(user=self.user)
        avatar = user.avatar
        return avatar


class ReplyReview(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rep_comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.rep_comment)[0:50]

    def cu(self):
        cu = Custom_User.objects.get(user=self.user)
        return cu


class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    star = models.IntegerField(default=0)

    def __str__(self):
        return str(self.product) + ': ' + str(self.star) + ' stars'
