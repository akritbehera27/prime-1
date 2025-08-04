### logic ###
''' Parimes get appart as we go up the number line, what is there distribuiton  over specfic intervals and classes .
'''

import prime

def dist_of_numbers(class_interval,number_list,list_mode):
    top_limit = top_limit_finder(class_interval,number_list)

    for r in range(1, int(top_limit/class_interval)+1):
        lower_limit = (r-1)*class_interval
        upper_limit = r*class_interval

        elements=[]
        for i in number_list:
            if i >= lower_limit and i < upper_limit:
                elements.append(i)

        if list_mode:
            print(f"{lower_limit} - {upper_limit} : {elements}")
        else:
            print(f"{lower_limit} - {upper_limit} : {len(elements)}")


def top_limit_finder(class_interval,num_list):
    if num_list[-1] % class_interval > 0 :
        top_limit = num_list[-1] + (class_interval - (num_list[-1] % class_interval))
    return top_limit


if __name__=='__main__':
    upper_limit_imput = int(input("Find primes form 1 to : "))
    class_input = int(input("Enter the Class Interval for Dist : "))

    prime_list = prime.find_prime_list(upper_limit_imput)
    dist_of_numbers(class_input,prime_list,False)