from django.db import models
from django.contrib.auth.models import User


# class Transaction(models.Model):
# user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
# biling_profile = models.ForeignKey(Billing, on_delete=models.DO_NOTHING)
# products    = models.ManyToManyField(Course, blank=True)
# name = models.CharField(max_length=150)
# amount = models.DecimalField(max_digits=10, decimal_places=2)
# tran_id = models.CharField(max_length=15)
# val_id = models.CharField(max_length=75)
# card_type = models.CharField(max_length=150)
# store_amount = models.DecimalField(max_digits=10, decimal_places=2)
# card_no = models.CharField(max_length=55, null=True)
# bank_tran_id = models.CharField(max_length=155, null=True)
# status = models.CharField(max_length=55)
# tran_date = models.DateTimeField()
# currency = models.CharField(max_length=10)
# card_issuer = models.CharField(max_length=255)
# card_brand = models.CharField(max_length=15)
# card_issuer_country = models.CharField(max_length=55)
# card_issuer_country_code = models.CharField(max_length=55)
# currency_rate = models.DecimalField(max_digits=10, decimal_places=2)
# verify_sign = models.CharField(max_length=155)
# verify_sign_sha2 = models.CharField(max_length=255)
# risk_level = models.CharField(max_length=15)
# risk_title = models.CharField(max_length=25)

# def __str__(self):
#     return self.tran_id


class PaymentGatewaySettings(models.Model):

    store_id = models.CharField(max_length=500, blank=True, null=True)
    store_pass = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        verbose_name = "PaymentGatewaySetting"
        verbose_name_plural = "PaymentGatewaySettings"
        db_table = "paymentgatewaysettings"


class Home_Banner(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.FileField(upload_to='home_banner', default='homebanner.jpg')

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)


class Offer(models.Model):
    name = models.CharField(max_length=20)
    image = models.FileField(upload_to='offer')

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=100, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.name + ': ' + self.subject


class Subscribe(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class Custom_User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.FileField(
        upload_to='profile/avatar/', default='default_profile320.png', blank=True, null=True)

    join_date = models.DateTimeField(auto_now_add=True)
    delivery_address = models.TextField(blank=True, null=True, default='None')

    def __str__(self):
        return str(self.user)

    def delete(self, *args, **kwargs):
        self.avatar.delete()
        super().delete(*args, **kwargs)

    def get_avatar(self):
        try:
            avatar = self.avatar.url
            return avatar
        except:
            return '/media/default_profile320.png'


class Contact_Number(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number_type = models.CharField(max_length=20, blank=True, null=True)
    number = models.CharField(max_length=20)

    def __str__(self):
        return str(self.user) + ': ' + self.number


class Brand(models.Model):
    name = models.CharField(max_length=30, unique=True)
    image = models.FileField(upload_to='brand/', default='brand.jpg')

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)
