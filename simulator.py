from utils import inc
from utils import dec


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
            the normal termination is describd by the message
            "Simulation has successfully completed"

    """
    try:
        report_file = open(report, 'wt')
    except FileNotFoundError:
        return "Bad report file specification"
    vars = set(init.keys())  # save the set of system variables
    cconfig = init
    for counter in range(nsteps):
        # write the current report line
        report_file.write("{0:6d} #".format(counter))
        for var in cconfig:
            report_file.write(" {0}:{1:2d}".format(var, cconfig[var]))
        report_file.write("\n")
        # form the next current configuration
        impacts = impact(cconfig)
        for var in vars:
            if impacts[var] > 0:
                cconfig[var] = inc(cconfig[var], nov)
            elif impacts[var] < 0:
                cconfig[var] = dec(cconfig[var], nov)
            elif impacts[var] == 0:
                pass
            else:
                report_file.close()
                return "Unexpected impact value"
    report_file.close()
    return "Simulation has successfully completed"
