def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    to_swap_lower = to_swap.lower()
    to_swap_upper = to_swap.upper()

    # Build a new string with the case flipped for the characters matching to_swap
    result = [
        char.swapcase() if char == to_swap_lower or char == to_swap_upper else char
        for char in phrase
    ]

    # Join the list into a string and return it
    return ''.join(result)