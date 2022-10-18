def main(a,b,c):
    """
    Find how many negative numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of negative numbers in the given numbers
    """
    i=0
    if a<0:
        i+=1
    if b<0:
        i+=1
    if c<0:
        i+=1
    return i