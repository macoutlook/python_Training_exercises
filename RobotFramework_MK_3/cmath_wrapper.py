import cmath
'''
Wrapper module for RobotFramework
Module implements keywords for using cmath functions
cmath_tests.tsv contains tests which can be executed in RobotFramework: pybot cmath
'''


def get_log10(x):
    """
    wrapper method for cmath.log10(x) function, calculates log10 for complex number
    :param x: complex number
    :return: log 10 of complex number
    """
    return cmath.log10(complex(x))


def get_sin(x):
    """
    wrapper method for cmath.sin(x) function, calculates sinus for int number. Can be implemented for complex number too
    :param x: int number
    :return: sinus for int number x
    """
    return cmath.sin(int(x))


def get_sqrt(x):
    """
    wrapper method for cmath.sqrt(x) function, calculates sqrt for complex number
    :param x: complex number
    :return: sqrt of complex number
    """
    return cmath.sqrt(complex(x))


def check_sqrt(x, res):
    """
    method which checks, whether given result of sqrt equals sqrt of cmath.sqrt method.
    :param x: complex number for which sqrt is calculated
    :param res: result which should be equaled to calculated sqrt of x
    :return: raises assertion error, if res is not equaled to x
    """
    if cmath.sqrt(complex(x)) != complex(res):
        AssertionError("Given result is not proper")
