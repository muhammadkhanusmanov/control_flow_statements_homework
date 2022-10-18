def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if a>99:
        if a%2==0:
            message = 'three-digit even number'
        else:
            message = 'three-digit odd number'
    else:
        if a%2==0:
            message = 'two-digit even number'
        else:
            message = 'two-digit odd number'
    return message