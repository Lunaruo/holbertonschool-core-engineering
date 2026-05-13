#!/usr/bin/env python3

def safe_print_integer(value):
    """print an integer with {:d} format"""
    """return false if value not an integer"""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False

