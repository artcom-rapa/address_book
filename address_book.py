class Cards:
   def __init__(self, first_name, last_name, company, position, email_address):
       self.first_name = first_name
       self.last_name = last_name
       self.company = company
       self.position = position
       self.email_address = email_address

pers_1 = Cards(first_name="Urjasz", last_name="Nowakowski", company="Argus Tapes", position="Aircraft pilot", email_address="UrjaszNowakowski@jourrapide.com")
pers_2 = Cards(first_name="Jakub", last_name="Kamiński", company="Mostow Co", position="Baker", email_address="JakubKaminski@rhyta.com")
pers_3 = Cards(first_name="Gabrysz", last_name="Jaworski", company="House Of Denmark", position="Floor installer", email_address="GabryszJaworski@dayrep.com")
pers_4 = Cards(first_name="Jowita", last_name="Majewska", company="Tee Town", position="Acoustical carpenter", email_address="JowitaMajewska@jourrapide.com")

name_list = [pers_1, pers_2, pers_3, pers_4]

for name in name_list:
    print("Imię: %s, nazwisko: %s, adres email: %s"% (name.first_name, name.last_name, name.email_address))
