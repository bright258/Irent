# in buiilt django dependencies
from django.db.models import TextChoices


# enums
class Currency(TextChoices):
    NGN = 'naira'
    USD = 'dollar'
    CND = 'canadian dollar'


class Category(TextChoices):
    RENT ='for rent'
    SALE = 'for sale'


class HouseStatus(TextChoices):
    SOLD = 'sold out'
    AVAILABLE = 'available'

class HouseType(TextChoices):
    SELF_CON = 'self contain'
    DUPLEX = 'duplex'
    ONE_BEDROOM_FLAT = 'one bedroom flat'