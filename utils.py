

def is_correct(cval, nvals):
    """The function checks whether 'cval' belongs to range(nvals)

    Arguments:
    ----------
        cval:    int                checked value
        nvals:   int  {nvals >= 2}  upper bound of the range

        return:  bool | TypeError | ValueError
    """
    if not isinstance(cval, int):
        return TypeError("type of 'cval' is invalid")
    if not isinstance(nvals, int):
        return TypeError("type of 'nvals' is invalid")
    if nvals < 2:
        return ValueError("value of 'nvals' is invalid")
    if cval < 0 or cval >= nvals:
        return ValueError("value of 'cval' is invalid")
    return True


def inc(cval, nvals):
    """The function increments value of 'cval' keeping the condition
        cval < nvals

    Arguments:
    ----------
        cval:   int   {0 <= cval < nvals}  increased value
        nvals:  int   {nvals >= 2}         upper bound of the range

        return:  int  increased value
    """
    result = is_correct(cval, nvals)
    if isinstance(result, Exception):  # checking is not successful
        raise result
    cval += 1
    return min(cval, nvals - 1)


def dec(cval, nvals):
    """The function decrements value of 'cval' keeping the condition
        cval >= 0

    Arguments:
    ----------
        cval:   int   {0 <= cval < nvals}  decreased value
        nvals:  int   {nvals >= 2}         upper bound of the range

        return:  int  decreased value
    """
    result = is_correct(cval, nvals)
    if isinstance(result, Exception): raise result
    cval -= 1
    return max(0, cval)
