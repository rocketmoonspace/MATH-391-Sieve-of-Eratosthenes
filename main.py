def main():
    print('\n\t\tSIEVE OF ERATOSTHENES')
    print('_' * 53, '\n')
    print('The Sieve of Eratosthenes is an ancient algorithm')
    print('for finding all prime numbers up to any given limit.')
    print('_' * 53, '\n')

    num = int(input('Enter a limit: '))
    print(f'\nThe primes up to and including {num} are:')
    SieveOfEratosthenes(num)

    again = input('\n\nWould you like to go again? [Y/N] ')
    print('_' * 53 + '\n')
    
    while again.upper() == 'Y':
        num = int(input('Enter a limit: '))
        print(f'\nThe primes up to and including {num} are:')
        SieveOfEratosthenes(num)

        again = input('\n\nWould you like to go again? [Y/N] ')
        print('_' * 53 + '\n')

    input('\n\nPress "Enter" to exit')

def SieveOfEratosthenes(num):
    prime = [True for i in range(num + 1)]
    p = 2
    while (p * p <= num):
        if (prime[p] == True):
 
            for i in range(p * p, num + 1, p):
                prime[i] = False
        p += 1
 
    for p in range(2, num + 1):
        if prime[p]:
            print(p, end=' ')

main()