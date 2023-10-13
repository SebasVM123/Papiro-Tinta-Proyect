from django.db import models


class Client(models.Model):
    dni = models.IntegerField()
    name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=75, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    password = models.CharField(max_length=50, blank=False, null=False)
    birthday = models.DateField()
    address = models.CharField(max_length=150)
    country = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    province = models.CharField(max_length=60)

    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {}".format(self.name, self.last_name)


class Card(models.Model):
    number = models.IntegerField(blank=False, null=False)
    security_code = models.SmallIntegerField(blank=False, null=False)
    expiration_date = models.DateField(blank=False, null=False)
    bank = models.CharField(max_length=50, blank=True, null=True)
    franchise = models.CharField(max_length=30, blank=False, null=False)
    owner_full_name = models.CharField(max_length=60, blank=False, null=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {}".format(len(str(self.number)[:-4]) * "*", str(self.number)[-4:])
