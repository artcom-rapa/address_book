from faker import Faker

fake = Faker("pl_PL")
# import datetime
import time


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


"""
persona_1 = BaseContact(first_name=fake.first_name(), last_name=fake.last_name(), email_address=fake.email(), tel_personal=fake.phone_number())
print(persona_1)
print(persona_1.contact())

"""


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


def elapsed_time(func):

    def calculate(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print("Funkcja", func.__name__, "wykonywała się", end - start, "sekund.")
        return result
    return calculate


@elapsed_time
def create_contacts(cards_count):
    cards = [BaseContact(first_name=fake.first_name(), last_name=fake.last_name(), email_address=fake.email(),
                         tel_personal=fake.phone_number()) for _ in range(cards_count)]
    print(*cards, sep="\n")


print(create_contacts(1000))