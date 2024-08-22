def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    vowels = 'aeiou'
    
    vowel_list = [char for char in s if char.lower() in vowels]
    
    
    vowel_list.reverse()
    
    
    result = []
    for char in s:
        if char.lower() in vowels:
            result.append(vowel_list.pop(0))
        else:
            result.append(char)
    
    return ''.join(result)