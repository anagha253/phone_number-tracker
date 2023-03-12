from text import phone
import phonenumbers
from phonenumbers import geocoder

first=phonenumbers.parse(phone,"CH")
print(geocoder.description_for_number(first,"en"))