from utils import inc, dec, config2str


# ----------------------------------------------------------------------
# Model parameters -----------------------------------------------------
# ----------------------------------------------------------------------
__ubrv = None  # : this parameter sets the upper bound of a range values
#
__impact = lambda cfg: 0  # : this parameter refers to the function that
# determines dict of impact values {-1, 0, 1} for each configuration
# ----------------------------------------------------------------------


def __next(config):
    global __impact
    impacts = __impact(config)
    for key in config:
        if impacts[key] < 0:
            config[key] = dec(config[key], __ubrv)
        elif impacts[key] > 0:
            config[key] = inc(config[key], __ubrv)
        elif impacts[key] == 0:
            pass
        else: raise ValueError("incorrect impact value")
    return config


def run(report, init_config, nsteps=100):
    """The function simulates system behaviour

    Arguments:
    ----------
        report  str : the file name for report saving
        init_config  dict : the initial model configuration
        nsteps  int  {nsteps > 0} : the length of the simulation history

    Return:
    -------
        return_code  int  {return <= 0} : 0 in the case of the
            successful termination and in other cases negative integer
            corresponding to kind of the detected problem
    """
    report_file = open(report, mode='w')
    config = init_config
    for step in range(nsteps):
        report_string = "{0}: {1}".format(step, config2str(config))
        report_file.write(report_string)
        config = __next(config)
    report_file.close()
