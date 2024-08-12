from django.db import models

class BankAccount(models.Model):
    account_number = models.PositiveIntegerField()
    balance = models.PositiveIntegerField(default=0)
    account_holder = models.ForeignKey(to='AccountHolder.AccountHolder', on_delete=models.CASCADE,null=True)

    def transfer(self,des_acc_number,amount):
        dest_acc = BankAccount.objects.get(account_number = des_acc_number)
        self.balance -= amount
        dest_acc.balance += amount
        self.save()
        dest_acc.save()
        