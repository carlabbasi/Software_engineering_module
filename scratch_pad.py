
# 4.3.1.9 LAB - Prime number finder

def is_prime(num):

    for a in range(2, int(1 + num **0.5)):
        if num % a == 0:
            return False
    return True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
