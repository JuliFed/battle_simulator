try:
    import numpy as np
except ImportError:
    print("Can't import numpy")
import random as rnd


ROUND_NUMBER = 2


def get_choice(obj):
    return rnd.choice(obj)


def geo_mean(num_list):
    """
    Function for geometric average from list
    """
    np_array = np.array(num_list)
    return np_array.prod() ** (1.0 / len(np_array))
