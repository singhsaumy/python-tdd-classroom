def reverse_list(input_list):
    """
    Reverses order of elements in list input_list.
    """
    
    input_list.reverse()
    return input_list
    

def count_digits(number):
    """
    Return count of digits
    """
    count = 0
    while(number>0):
        number=number//10
        count=count+1
    return count
