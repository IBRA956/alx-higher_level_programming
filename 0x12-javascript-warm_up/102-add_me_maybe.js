def add_me_maybe(number, the_function):
    """
    Adds 1 to the given number and calls the provided function with the result.
    
    Args:
        number (int): The input number.
        the_function (function): The function to be called with the result.
    """
    the_function(number + 1)

# Example usage
def print_result(result):
    print(f"Result: {result}")

add_me_maybe(5, print_result)

