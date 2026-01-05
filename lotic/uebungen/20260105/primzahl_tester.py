def is_prime(n):
    # 1 is per definition not a prime number. So we handle it first.
    if n == 1:
        return False
    # 2 is the only even prime.
    if n == 2:
        return True
    # There is a lot of room for optimiziation. But for now, lets just Bruteforce it!
    for i in range (2, n):
        if n % i == 0:
            return False
    return True

while True:
    print('Bitte gib eine Zahl ein oder q um zu beenden.')
    user_input = input()
    if user_input == 'q':
        break
    try:
        number = int(user_input)
        number_is_prime = is_prime(number)
        if number_is_prime:
            print(f'{number} ist eine Primzahl')
        else:
            print(f'{number} ist keine Primzahl')
    except:
        print('Ungültige Eingabe')
