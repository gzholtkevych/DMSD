import matplotlib.pyplot as plt


def plot_history(report):
    """The function visualizes behaviour of system variables

    Args:
        report  str:
            this string contains the specification of the report file
            being visualized
    Returns:
        diagnostic_message  str:
            this message describes problem of visualization process;
            the normal termination is described by the message
            "Visualization has successfully completed"
    """
    try:  # opening the file contained simulation report
        report_file = open(report, 'rt')
    except FileNotFoundError:
        return "Report file not found"
    # restoring the system variables
    vars = report_file.readline()[:-1].split(' ')
    nvars = len(vars)
    # preparing data arrays
    data = dict([(var, []) for var in vars])
    for line in report_file:
        vals = line[:-1].split(' ')
        for var_id in range(nvars):
            data[vars[var_id]].append(int(vals[var_id]))
    # determining plotting boundaries
    xmax, ymax = 0, 0
    for var in vars:
        xmax = max(xmax, len(data[var]) - 1)
        ymax = max(ymax, max(data[var]))
    # pyplot commands
    fig = plt.figure()
    plt.title("History of the system behaviour")
    plt.xlabel("Time tiсks")
    plt.ylabel("Values of the system variables")
    plt.xlim((0, xmax + 1))
    plt.ylim((-0.25, ymax + 0.5))
    plt.yticks(range(ymax + 1))
    ax = fig.add_axes()
    plt.grid()
    for var in vars:
        plt.plot(data[var])
    plt.legend(vars)
    plt.show()
    return "Visualization has successfully completed"
