def replace_in_list(my_list, idx, element):
    """
    Replaces an element in a list at a specific index.

    Args:
        my_list (list): The list to modify
        idx (int): Index of the element to replace
        element: New value to insert

    Returns:
        list: Modified list if idx is valid, otherwise original list
    """

    if idx < 0 or idx >= len(my_list):
        return my_list

    my_list[idx] = element
    return my_list
