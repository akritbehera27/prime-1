### logic ###
''' How many prime numbers exist which are two digits appart like 11 and 13   
    are two apart, do they ever stop at certain point. as we know that primes get
    further form each other as we progress towards infinity..
'''

import prime

def find_primes2_appart(list_of_primes):
    primes2_appart_list=[]
    # len(prime_list)-1 beacuse we are not gonna concider the last element.
    for i in range(0,len(list_of_primes)-1):
        current_number=list_of_primes[i]
        next_number=list_of_primes[i+1]

        if next_number-current_number == 2:
            primes2_appart_list.append(f"{current_number}:{next_number}")
            
    return primes2_appart_list

if __name__=='__main__':
    upper_limit_imput=int(input("Find primes form 1 to : "))
    input_prime_list = prime.find_prime_list(upper_limit_imput)
    output_list=find_primes2_appart(input_prime_list)

    print(output_list)