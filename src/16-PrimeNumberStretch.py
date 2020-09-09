def isPrimeNum():
    while True:
        num=int(input('Give any number greater than 1 to evaluate: '))
        if num == 1:
            continue
        else:
            for i in range(2,num):
                if num % i == 0:
                    print(f'{num} is not a prime number')
                    break
            else:
                print(f'{num} is a prime number')
            break

isPrimeNum()