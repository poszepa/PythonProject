import RandomExample

def run_program_lotto(number_unique_number) :
    number_list = []
    while(True):
        random_number = RandomExample.random_int(1,50)
        if(is_number_in_list(random_number, number_list) == False):
            number_list.append(random_number)
        if(len(number_list) == number_unique_number):
            break;
    return number_list



def is_number_in_list(number, list):
    return number in list

