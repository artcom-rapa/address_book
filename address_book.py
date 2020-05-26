from faker import Faker

fake = Faker("pl_PL")

"""
class Card:
    def __init__(self, first_name, last_name, company, position, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.position = position
        self.email_address = email_address

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.email_address}"

    def __repr__(self):
        return f"Card(first_name={self.first_name} last_name={self.last_name}, email_address={self.email_address})"

    def contact(self):
        return f"Kontaktuję się z: {self.first_name} {self.last_name}, position - {self.position}, email_address - {self.email_address})"

    @property
    def count_letters(self):
        return sum([len(self.first_name), len(self.last_name), 1])


pers_1 = Card(first_name=fake.first_name(), last_name=fake.last_name(), company=fake.company(), position=fake.job(),
              email_address=fake.company_email())
pers_2 = Card(first_name=fake.first_name(), last_name=fake.last_name(), company=fake.company(), position=fake.job(),
              email_address=fake.company_email())
pers_3 = Card(first_name=fake.first_name(), last_name=fake.last_name(), company=fake.company(), position=fake.job(),
              email_address=fake.company_email())
pers_4 = Card(first_name=fake.first_name(), last_name=fake.last_name(), company=fake.company(), position=fake.job(),
              email_address=fake.company_email())
pers_5 = Card(first_name=fake.first_name(), last_name=fake.last_name(), company=fake.company(), position=fake.job(),
              email_address=fake.company_email())

name_list = [pers_1, pers_2, pers_3, pers_4]

# or name in name_list:
# print("Imię: %s, nazwisko: %s, adres email: %s"% (name.first_name, name.last_name, name.email_address))

by_first_name = sorted(name_list, key=lambda pers: pers.first_name)
by_last_name = sorted(name_list, key=lambda pers: pers.last_name)
by_email = sorted(name_list, key=lambda pers: pers.email_address)

print(*by_first_name, sep="\n")
print()
print(*by_last_name, sep="\n")
print()
print(*by_email, sep="\n")

print(pers_1)
print(pers_1.contact())
print(pers_1.count_letters)
"""
class BaseContact:
    def __init__(self, first_name, last_name, email_address, tel_personal):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.tel_personal = tel_personal

    def __str__(self):
        return f"{self.first_name} {self.last_name}, email_address: {self.email_address}, tel_personal: {self.tel_personal}"

    def contact(self):
        return f"Wybieram numer {self.tel_personal}  i dzwonię do {self.first_name} {self.last_name}"

    @property
    def label_length(self):
        return sum([len(self.first_name), len(self.last_name)])


persona_1 = BaseContact(first_name=fake.first_name(), last_name=fake.last_name(), email_address=fake.email(), tel_personal=fake.phone_number())
print(persona_1)
print(persona_1.contact())


class BusinessContact(BaseContact):
    def __init__(self, company, position, email_business, tel_business, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company = company
        self.position = position
        self.email_business = email_business
        self.tel_business = tel_business

    def __str__(self):
        return f"{self.first_name} {self.last_name}, company: {self.company}, position: {self.position}, email_business: {self.email_business}, tel_business: {self.tel_business}"

    @property
    def label_length(self):
        return sum([len(self.first_name), len(self.last_name)])

    def contact(self):
        return f"Wybieram numer: {self.tel_business}  i dzwonię do {self.first_name} {self.last_name}"


def create_contacts(cards_count, card_type="personal"):
    if card_type == "personal":
        personal_card = [BaseContact(first_name=fake.first_name(), last_name=fake.last_name(), email_address=fake.email(), tel_personal=fake.phone_number()) for _ in range(cards_count)]
        print(*personal_card, sep="\n")
    if card_type == "business":
        business_card = [BusinessContact(first_name=fake.first_name(), last_name=fake.last_name(), email_address=fake.email(), tel_personal=fake.phone_number(), company=fake.company(), position=fake.job(),
              email_business=fake.company_email(), tel_business=fake.phone_number()) for _ in range(cards_count)]
        print(*business_card, sep="\n")

create_contacts(5, "business")