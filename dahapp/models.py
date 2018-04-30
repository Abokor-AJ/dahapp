from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    TELLER = 1
    CHIEF_CASHIER = 2
    ADMIN = 3
    ROLE_CHOICES = (
        (TELLER, 'Teller'),
        (CHIEF_CASHIER, 'Chief Cashier'),
        (ADMIN, 'Admin'),
    )

    user = models.OneToOneField(User)
    position = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Remittance(models.Model):
    usd = models.DecimalField(max_digits=10, decimal_places=2)
    djf = models.DecimalField(max_digits=12, decimal_places=2)
    created_on = models.DateTimeField('date created')
    created_by = models.ForeignKey(User)

    class Meta:
        get_latest_by = 'created_on'


class Payment(models.Model):
    usd = models.DecimalField(max_digits=10, decimal_places=2)
    djf = models.DecimalField(max_digits=12, decimal_places=2)
    created_on = models.DateTimeField('date created')
    created_by = models.ForeignKey(User)

    class Meta:
        get_latest_by = 'created_on'


class OpeningBalance(models.Model):
    usd = models.DecimalField(max_digits=10, decimal_places=2)
    djf = models.DecimalField(max_digits=12, decimal_places=2)
    receiver = models.CharField(max_length=50)
    created_on = models.DateTimeField('date created')
    created_by = models.ForeignKey(User)
    status = models.IntegerField(default=0)

    class Meta:
        get_latest_by = 'created_on'


class Stamp(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_on = models.DateTimeField('date created')
    created_by = models.ForeignKey(User)

    class Meta:
        get_latest_by = 'created_on'


class Cheque(models.Model):
    cheque_no = models.CharField(max_length=15)
    bank_name = models.CharField(max_length=70)
    customer_name = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_on = models.DateTimeField('date created')
    created_by = models.ForeignKey(User)
    currency = models.CharField(max_length=5, default="USD")

    class Meta:
        get_latest_by = 'created_on'


class Transfer(models.Model):
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.CharField(max_length=100)
    received_by = models.CharField(max_length=50)
    created_on = models.DateTimeField('date created')
    created_by = models.ForeignKey(User)

    class Meta:
        get_latest_by = 'created_on'


class Vouchers(models.Model):
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.CharField(max_length=100)
    signed_by = models.CharField(max_length=50)
    created_on = models.DateTimeField('date created')
    created_by = models.ForeignKey(User)

    class Meta:
        get_latest_by = 'created_on'


class Deposit(models.Model):
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.CharField(max_length=100)
    deposited_by = models.CharField(max_length=50)
    created_on = models.DateTimeField('date created')
    created_by = models.ForeignKey(User)

    class Meta:
        get_latest_by = 'created_on'


class Withdrawal(models.Model):
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.CharField(max_length=100)
    withdrawn_by = models.CharField(max_length=50)
    authorized_by = models.CharField(max_length=50)
    created_on = models.DateTimeField('date created')
    created_by = models.ForeignKey(User)

    class Meta:
        get_latest_by = 'created_on'


class Loan(models.Model):
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=50)
    authorized_by = models.CharField(max_length=50)
    created_on = models.DateTimeField('date created')
    created_by = models.ForeignKey(User)

    class Meta:
        get_latest_by = 'created_on'


class Refund(models.Model):
    tt_no = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    amount_full = models.DecimalField(max_digits=12, decimal_places=2)
    amount_net = models.DecimalField(max_digits=12, decimal_places=2)
    created_on = models.DateTimeField('date created')
    created_by = models.ForeignKey(User)

    class Meta:
        get_latest_by = 'created_on'
