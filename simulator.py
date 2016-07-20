#


def run(report, nov, init, impact, nsteps=100):
    """The function simulates the behaviour of descriptive model of
    a complex system

    Arguments:
        report  str:  the file specification for report saving
        nov  int  {nov > 1}:  the number of observed values
        init  dict[sysvar: value, ...]  {value in range(nov)}:
            the initial system configuration;
        impact  dict[sysvar: value, ...] -> dict[sysvar: ivalue, ...]
            {value in range(nov) and ivalue in {-1, 0, 1}}:
            the function determines dict of impacts taking the current
            configuration as input and return the impact for each
            system variable
        nsteps  int  {nsteps > 0}:  the number of simulation steps

    Returns:
        diagnostic_message  str:
            this message describes problem of simulation process;
            the normal termination is described by the message
            "Simulation has successfully completed"

    """
    try:
        report_file = open(report, 'wt')
    except FileNotFoundError:
        return "Bad report file specification"
    # saving the list of system variables
    vars = sorted(list(init.keys()))
    # writing the header in the report file
    for var in vars:
        report_file.write(var)
        report_file.write('\n' if var == vars[-1] else ' ')
    #
    cconfig = init
    for counter in range(nsteps):  # the main simulation loop
        # write the current report line
        for var in vars:
            report_file.write("{0:d}".format(cconfig[var]))
            report_file.write('\n' if var == vars[-1] else ' ')
        # form the next current configuration
        impacts = impact(cconfig)
        try:
            for var in vars:
                if impacts[var] > 0:
                    cconfig[var] = __inc(cconfig[var], nov)
                elif impacts[var] < 0:
                    cconfig[var] = __dec(cconfig[var], nov)
                elif impacts[var] == 0:
                    pass
                else:
                    report_file.close()
                    return "Unexpected impact value"
        except TypeError:
            report_file.close()
            return "Unexpected value type in init configuration"
        except ValueError:
            report_file.close()
            return "Unexpected value in init configuration"
    report_file.close()
    return "Simulation has successfully completed"


def __dec(val, nov):
    """The function decrements value of 'cval' keeping the condition
        val >= 0

    Arguments:
        val  int  {0 <= val < nov}:  the value being decreased
        nov  int  {nov > 1}:  the number of observed values

    Returns:
        int:  the decreased value
    """
    result = __is_correct(val, nov)
    if isinstance(result, Exception): raise result
    val -= 1
    return max(0, val)


def __inc(val, nov):
    """The function increments value of 'val' keeping the condition
        val < nov

    Arguments:
        val  int  {0 <= cval < nov}:  the value being increased
        nov  int  {nov > 1}:  the number of observed values

    Returns:
        int:  the increased value
    """
    result = __is_correct(val, nov)
    if isinstance(result, Exception):  # checking is not successful
        raise result
    val += 1
    return min(val, nov - 1)


def __is_correct(val, nov):
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
