from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils import timezone
# from celery import shared_task
# from accounts.models import Account
from transactions.models import Transaction


@receiver(post_save, sender=Transaction)
def update_account_balance(sender, instance, **kwargs):
    if instance.payment_date.date() <= timezone.now().date():
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

    # @shared_task
# def update_account_balance_async(account, value, type):
#     account = Account.objects.get(pk=account)
#     if type == "D":
#         account.balance -= value
#     elif type == "C":
#         account.balance += value
#     account.save()

# @receiver(post_save, sender=Transaction)
# def schedule_update_account_balance(sender, instance, **kwargs):
#     account = instance.account
#     value = instance.value
#     type = instance.type

#     # Obtenha a data de pagamento da instância
#     payment_date = instance.payment_date

#     # Converta a data de pagamento para datetime se for uma data
#     if isinstance(payment_date, timezone.datetime):
#         payment_date = payment_date.date()

#     # Verificar se a data de pagamento é futura
#     if payment_date > timezone.now().date():
#         # Agendar a tarefa para a data de pagamento
#         update_account_balance_async.apply_async(args=[account, value, type], eta=payment_date)
#     else:
#         # A data de pagamento é hoje ou passada, executar imediatamente
#         update_account_balance_async(account, value, type)
