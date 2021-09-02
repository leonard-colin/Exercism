"""This module can calculate the bake time remaining since the lasagna has been in the oven,
the preparation time it will take to prepare the lasagna according to the number of layers you want to add
and the elapsed time in minutes since you started cooking the lasagna receipe.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    '''
    :param elapsed_bake_time: int baking time already elapsed
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    '''

    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    '''
    :param number_of_layers: int number of layers added to the lasagna
    :return: int total preparation time according to the number of layers

    Function that takes the number of layers you want to add to the lasagna as
    an argument and returns of many minutes you need to prepare the lasagna
    '''

    return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    '''
    :param number_of_layers: int number of layers added to the lasagna
    :param elapsed_bake_time: int baking time already elapsed
    :return: int total elapsed time cooking

    Function that takes the number of layers and the elapsed bake time as arguments and return
    the sum of your preparation time and the time the lasagna has already spent baking in the oven
    '''

    return sum((preparation_time_in_minutes(number_of_layers), elapsed_bake_time))
