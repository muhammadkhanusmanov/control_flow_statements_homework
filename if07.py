def main(a):
    """
    Given an integer a, check the following conditions:
    "positive odd number",
    "positive even number",
    "negative odd number",
    "negative even number",
    "the number is zero"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if a>0:
        if a%2==0:
            message = 'positive even number'
        else:
            message = 'positive odd number'
    elif a<0:
        if a%2==0:
            message = 'negative even number'
        else:
            message = 'negative odd number'
    else:
        message = 'the number is zero'
       
    return message