#
# Skeleton file for the Python "Hello World" exercise.
#


def hello(name=''):
    if not name:
        out = "Hello, World!"
    else:
        out = u"Hello, {}!".format(name)
    return out
