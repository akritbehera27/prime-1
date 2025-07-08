import math

### Base logic to find prime numbers ###
''' A number is prime if its only divible by 1 and itself 
    in other words if we check if a number is divible by certain range of numbers 
    and if the range of numbers are not its factors then we can confer that the number is prime. the range of number will be( 2 to squrt(N) )
'''


## Settings Variables ##
logs=False
record=True
STORAGE_FILE="Prime_Records.txt"

def save_generated_primes(string):
    if record:
        with open(STORAGE_FILE, 'w') as f:
            f.write(string)
    else:
        print("Please Enable Recoding Via Variables")

def find_primes(Upper_Limit):
    Prime_list=[]
    # 1 is not a prime number thus we start form 2
    for number in range(2,Upper_Limit):
        divisiblity_list=[]
        if logs:
            print(f"\ntaking number {number} and checking if its a prime")
        # To check divisibly form 2 to sqrt n
        # print(f"range = {round(math.sqrt(number))+1}")
        for diviser in range(2,round(math.sqrt(number))+1):
            if number/diviser != round(number/diviser):
                if logs:
                    print(f"{number}/{diviser} Prime.....")
                divisiblity_list.append("P")
            else:
                if logs:
                    print(f"{number}/{diviser} Composit...")
                divisiblity_list.append("C")
        if logs:
            print("This is the Whole list for divisiblity")
            print(divisiblity_list)

        if "C" not in divisiblity_list:
            Prime_list.append(number)
            if logs:
                print("Prime Found...")
                print(number)

    return Prime_list

if __name__=='__main__':
    upper_limit_imput=int(input("Enter the Upper Limit : "))
    prime_list=find_primes(upper_limit_imput)

    print(f"\n\nPrimes numbers form 2 to {upper_limit_imput} are :\n{prime_list}\n")
    save_generated_primes(str(prime_list))

