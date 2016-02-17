import cmath


def get_log10(x):
    return cmath.log10(complex(x))


def get_sin(x):
    return cmath.sin(int(x))


def get_sqrt(x):
    return cmath.sqrt(complex(x))


def do_something():
    print "ok"


def check_sqrt(x, res):
    if cmath.sqrt(complex(x)) != complex(res):
        AssertionError("Given result is not proper")
