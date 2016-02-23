import cmath
'''
Wrapper module for RobotFramework
Module implements keywords for using cmath functions
cmath_tests.tsv contains tests which can be executed in RobotFramework: pybot cmath
'''


def get_log10(x):
    """
    Wrapper method for cmath.log10(x) function, calculates log10 for complex number

    Examples:
    | Get log10 | 100 + 0j |
    """
    return cmath.log10(complex(x))


def get_sin(x):
    """
    Wrapper method for cmath.sin(x) function, calculates sinus for int number. Can be implemented for complex number too

    Examples:
    | Get Sin | 30 |
    """
    return cmath.sin(int(x))


def get_sqrt(x):
    """
    Wrapper method for cmath.sqrt(x) function, calculates sqrt for complex number

    Examples:
    | Get Sqrt | 16 + 16j |
    """
    return cmath.sqrt(complex(x))


def check_sqrt(x, res):
    """
    Method which checks, whether given result of sqrt equals sqrt of cmath.sqrt method.

    Examples:
    | Check Sqrt | 4 + 0j | 16 + 0j |
    """
    if cmath.sqrt(complex(x)) != complex(res):
        AssertionError("Given result is not proper")
