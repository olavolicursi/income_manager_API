from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils import timezone
from transactions.models import Transaction


@receiver(post_save, sender=Transaction)
def update_account_balance(sender, instance, **kwargs):
    if instance.payment_date is not None:
        if instance.payment_date <= timezone.now().date():
            account_id = instance.account_id
            if instance.type == "D":
                account_id.balance -= instance.value
            elif instance.type == "C":
                account_id.balance += instance.value
            account_id.save()


@receiver(post_delete, sender=Transaction)
def delete_account_balance(sender, instance, **kwargs):
    account_id = instance.account_id
    if instance.type == "D":
        account_id.balance += instance.value
    elif instance.type == "C":
        account_id.balance -= instance.value
    account_id.save()
