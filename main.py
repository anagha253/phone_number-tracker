from text import phone
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier


first=phonenumbers.parse(phone,"CH")
print(geocoder.description_for_number(first,"en"))
first=phonenumbers.parse(phone,"RO")
print(carrier.name_for_number(first,"en"))
