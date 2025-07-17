import math
from time import sleep

### Base logic to find prime numbers ###
''' A number is prime if its only divible by 1 and itself 
    in other words if we check if a number is divible by certain range of numbers 
    and if the range of numbers are not its factors then we can confer that the number is prime. the range of number will be( 2 to squrt(N) )
'''

def is_prime(number):
    divisiblity_list=[]
    for diviser in range(2,round(math.sqrt(number))+1):
            if number/diviser != round(number/diviser):
                divisiblity_list.append("P")
            else:
                divisiblity_list.append("C")

    if "C" not in divisiblity_list:
        return True
    else:
        return False

def find_prime_list(Upper_Limit):
    prime_list=[]
    for number in range(2,Upper_Limit):
        if is_prime(number):
            prime_list.append(number)

    return prime_list


def find_prime_list_continous():
    i=2
    while True:
        i=i+1
        if is_prime(i):
            print(i)
            sleep(0.6)


if __name__=='__main__':
    upper_limit_imput=int(input("Find primes form 1 to : "))

    if upper_limit_imput == 0:
        find_prime_list_continous()
    else:
        print(f"\nPrimes numbers form 2 to {upper_limit_imput} are :\n{find_prime_list(upper_limit_imput)}\n")



