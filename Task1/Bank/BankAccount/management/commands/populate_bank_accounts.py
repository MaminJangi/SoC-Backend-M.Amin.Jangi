from django.core.management.base import BaseCommand
from AccountHolder.models import AccountHolder
from BankAccount.models import BankAccount
import string
import csv
import random

# Step 1: Load names from the CSV file
def load_names_from_csv(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        names = [row[0] for row in reader]
    return names

# Step 2: Use the names to create random BankHolders
def populate_bankholders_and_accounts():
    first_names = load_names_from_csv('names.csv')
    last_names = load_names_from_csv('names.csv')

    holders = []
    for i in range(20000):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        nid = ''.join(random.choices(string.digits, k=10))  # Random NID
        
        holder = AccountHolder(
            first_name=first_name,
            last_name=last_name,
            NID=nid
        )
        holders.append(holder)

        if len(holders) >= 10000:
            AccountHolder.objects.bulk_create(holders)
            holders = []

    if holders:
        AccountHolder.objects.bulk_create(holders)

    # After creating AccountHolder, create BankAccounts for them
    holders = list(AccountHolder.objects.all())
    accounts = []

    for i in range(20000):
        account_number = ''.join(random.choices(string.digits, k=16))  # Random account number
        account = BankAccount(
            account_number=account_number,
            balance = round(random.uniform(0,1000000000),2),
            account_holder=random.choice(holders)
        )
        accounts.append(account)

        if len(accounts) >= 10000:
            BankAccount.objects.bulk_create(accounts)
            accounts = []

    if accounts:
        BankAccount.objects.bulk_create(accounts)

# Run the population script
populate_bankholders_and_accounts()