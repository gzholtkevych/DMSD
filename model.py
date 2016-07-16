from utils import inc, dec


# model parameters
__number_of_values = None   # this parameter sets the range for values
__current_config   = None   # this parameter refers to the current system config
__next             = None   # this parameter refers to the operator determined dynamics

class Model:
    """The class represents a descriptive model

    """
    def __init__(self, nvals, params, dynamics):
        """Construct of the model

        Arguments:
        ----------
            # the number of the observed values
            nvals:     int           {nvals >= 2}
            # the dictionary of parameters with their initial values
            params:    dict          {len(params) >= 2}
            # the dynamic operator on parameter space
            dynamics:  dict -> dict
        """
        self.__nvs = nvals
        self.__cfg = params
        self.__dyn = dynamics
        pass

    def get_cfg(self):
        """Method is devoted to inspect the current model configuration

        Arguments are absent
        --------------------
        Return
        ------
            dict()
        """
        pass

    def __next__(self):
        impacts = self.__dyn(self.get_cfg())
        res = {}
        for param in self.__cfg:
            if impacts[param] < 0:
                res[param] = dec(self.__cfg[param], self.__nvs)
            elif impacts[param] > 0:
                res[param] = inc(self.__cfg[param], self.__nvs)
            else:
                res[param] = self.__cfg[param]
        return res

    def run(self, life_length, report):
        file = open(report, mode='w')
        counter = 0
        while counter < life_length:
            file.write(counter, self.get_cfg())
            self.__cfg = self.__next()
            counter += 1
        file.write(counter, self.get_cfg())
        file.close()
