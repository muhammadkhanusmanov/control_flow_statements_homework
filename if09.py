def main(a):
    """
    The two-digit integer is given.
    Replace the digits of the number.
    True if the resulting number is less than or equal to the old number, otherwise return False.
    
    Args:
        a: integer
    Returns:
        boolean: True if the resulting number is less than or equal to the old number, otherwise return False.
    """
    t=a%10
    o=(a%100-t)//10
    new_num=t*10+o
    if a>=new_num:
        b = True
    else:
        b = False
    return b 
