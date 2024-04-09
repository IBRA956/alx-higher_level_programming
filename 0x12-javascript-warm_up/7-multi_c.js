import sys

def print_c_is_fun(num_occurrences):
    if not num_occurrences.isdigit():
        print("Missing number of occurrences")
    else:
        num_occurrences = int(num_occurrences)
        while num_occurrences > 0:
            print("C is fun")
            num_occurrences -= 1

# Get the command line argument (number of occurrences)
if len(sys.argv) > 1:
    num_occurrences = sys.argv[1]
    print_c_is_fun(num_occurrences)
else:
    print("Missing number of occurrences")

