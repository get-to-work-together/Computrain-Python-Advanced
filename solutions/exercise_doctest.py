import doctest

def cube(x):
    """Calculates the third power of x

    Doctests:

    >>> cube(4)
    64

    >>> [cube(x) for x in range(10)]
    [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
    """
    return x**3


# -------------------------------------

if __name__ == '__main__':

    print(cube(3))
    print(list(cube(x) for x in range(10)))

    print(help(cube))

    doctest.testmod(verbose=True)
