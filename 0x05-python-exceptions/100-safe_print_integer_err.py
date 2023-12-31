#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return True
    except TypeError as te:
        print("Exception:", te, file=sys.stderr)
        return False
    except ValueError as ve:
        print("Exception:", ve, file=sys.stderr)
        return False
