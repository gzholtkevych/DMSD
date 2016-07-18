import simulator


init = {'victim': 1, 'predator': 1}
range_capacity = 3


def vp(config):
    impacts = dict(victim=0, predator=0)
    impacts['victim'] =\
        -1 if config['victim'] <= config['predator'] else 1
    impacts['predator'] =\
        -1 if config['victim'] <= config['predator'] else 1
    return impacts


response = simulator.run("report", range_capacity, init, vp)
print(response)