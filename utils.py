

def is_correct(val, nov):
    """The function checks whether 'val' belongs to range(nov)

    Arguments:
        val  int :  the checked value
        nov  int  {nov > 1}:  the number of observed values

    Returns:
        bool | TypeError | ValueError
    """
    if not isinstance(val, int):
        return TypeError("type of 'val' is invalid")
    if not isinstance(nov, int):
        return TypeError("type of 'nov' is invalid")
    if nov < 2:
        return ValueError("value of 'nov' is invalid")
    if val < 0 or val >= nov:
        return ValueError("value of 'val' is invalid")
    return True


def inc(val, nov):
    """The function increments value of 'val' keeping the condition
        val < nov

    Arguments:
        val  int  {0 <= cval < nov}:  the value being increased
        nov  int  {nov > 1}:  the number of observed values

    Returns:
        int:  the increased value
    """
    result = is_correct(val, nov)
    if isinstance(result, Exception):  # checking is not successful
        raise result
    val += 1
    return min(val, nov - 1)


def dec(val, nov):
    """The function decrements value of 'cval' keeping the condition
        val >= 0

    Arguments:
        val  int  {0 <= val < nov}:  the value being decreased
        nov  int  {nov > 1}:  the number of observed values

    Returns:
        int:  the decreased value
    """
    result = is_correct(val, nov)
    if isinstance(result, Exception): raise result
    val -= 1
    return max(0, val)


def config2str(config): pass