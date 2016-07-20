import simulator
from utils import plot_history


init = {'victim': 0, 'predator': 2}
value_range = 3


def vp(config):
    impacts = dict(victim=0, predator=0)
    if config['victim'] < config['predator']:
        impacts['victim'] = -1
        impacts['predator'] = -1
    elif config['victim'] > config['predator']:
        impacts['victim'] = 1
        impacts['predator'] = 1
    else:
        impacts['victim'] = 1
        impacts['predator'] = -1
    return impacts


response = simulator.run("report", value_range, init, vp, nsteps=150)
print(response)
response = plot_history("report")
print(response)

