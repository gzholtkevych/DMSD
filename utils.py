

def is_correct(cval, nvals):
    """The function checks whether 'cval' belongs to range(nvals)

    Arguments:
    ----------
        cval:    int                checked value
        nvals:   int  {nvals >= 2}  upper bound of the range

        return:  int | TypeError | ValueError
    """
    if not isinstance(cval, int):
        return TypeError("type of 'cval' is invalid")
    if not isinstance(nvals, int):
        return TypeError("type of 'nvals' is invalid")
    if nvals < 2:
        return ValueError("value of 'nvals' is invalid")
    if cval < 0 or cval >= nvals:
        return TypeError("value of 'cval' is invalid")
    return 0


def inc(cval, nvals):
    res = is_correct(cval, nvals)
    if not isinstance(res, int): raise res
    cval += 1
    return min(cval, nvals - 1)


def dec(cval, nvals):
    res = is_correct(cval, nvals)
    if not isinstance(res, int): raise res
    cval -= 1
    return max(0, cval)
