def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """

    size = len(matrix)
    
    
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0
    
    for i in range(size):
        primary_diagonal_sum += matrix[i][i]           
        secondary_diagonal_sum += matrix[i][size - 1 - i]  
    
    return primary_diagonal_sum + secondary_diagonal_sum