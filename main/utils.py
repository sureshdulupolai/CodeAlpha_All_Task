import string
import random
from .models import URL


def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits

    while True:
        # Randomly create a 6-character code
        code = ''.join(random.choice(characters) for _ in range(length))

        # Check if code already exists in the database
        if not URL.objects.filter(short_code=code).exists():
            return code
