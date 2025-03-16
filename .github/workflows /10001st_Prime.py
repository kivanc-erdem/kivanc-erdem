import math


def is_prime(n):
    factor = 3
    while factor <= math.sqrt(n):
        if n % factor == 0:
            return False
        factor += 2
    return True


count = 1
x = 3

while count != 10001:
    if is_prime(x):
        count += 1
    x += 2

x -= 2
print(x)

github_user_name: kivanc-erdem
 
