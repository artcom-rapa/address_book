from faker import Faker

fake = Faker("pl_PL")
fake.first_name()
fake.last_name()
fake.company()
fake.job()
fake.company_email()

class Card:
   def __init__(self, first_name, last_name, company, position, email_address):
       self.first_name = first_name
       self.last_name = last_name
       self.company = company
       self.position = position
       self.email_address = email_address

   def __str__(self):
       return f"{self.first_name} {self.last_name}, {self.email_address},"

pers_1 = Card(first_name= fake.first_name(), last_name= fake.last_name(), company= fake.company(), position= fake.job(), email_address= fake.company_email())
pers_2 = Card(first_name= fake.first_name(), last_name= fake.last_name(), company= fake.company(), position= fake.job(), email_address= fake.company_email())
pers_3 = Card(first_name= fake.first_name(), last_name= fake.last_name(), company= fake.company(), position= fake.job(), email_address= fake.company_email())
pers_4 = Card(first_name= fake.first_name(), last_name= fake.last_name(), company= fake.company(), position= fake.job(), email_address= fake.company_email())
pers_5 = Card(first_name= fake.first_name(), last_name= fake.last_name(), company= fake.company(), position= fake.job(), email_address= fake.company_email())

name_list = [pers_1, pers_2, pers_3, pers_4]

#or name in name_list:
    #print("Imię: %s, nazwisko: %s, adres email: %s"% (name.first_name, name.last_name, name.email_address))

by_first_name = sorted(name_list, key=lambda pers: pers.first_name)
by_last_name = sorted(name_list, key=lambda pers: pers.last_name)
by_email = sorted(name_list, key=lambda pers: pers.email_address)

print(*by_first_name, sep= "\n")
print()
print(*by_last_name, sep= "\n")
print()
print(*by_email, sep= "\n")