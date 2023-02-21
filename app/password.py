import random
import string
from datetime import datetime

def generate_random_password(length = 8):
    return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k = length))

# print(generate_random_password(12))
# print(string.punctuation)
# print(datetime.now())
