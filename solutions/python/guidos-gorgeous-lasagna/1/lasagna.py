"""Lasagna cooking time calculator.

This module helps calculate the expected bake time, remaining bake time,
preparation time, and total elapsed cooking time for making lasagna.
"""

# Constant for expected bake time in minutes.
EXPECTED_BAKE_TIME = 40  # in minutes


def bake_time_remaining(elapsed_bake_time):
    """Calculate the remaining bake time.

    :param elapsed_bake_time: int - minutes lasagna has been baking.
    :return: int - minutes remaining until lasagna is done baking.

    This function takes the elapsed bake time and returns how many more
    minutes are needed to reach the expected bake time.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :return: int - total preparation time in minutes.

    Assumes each layer takes 2 minutes to prepare.
    """
    return number_of_layers * 2


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed time in the kitchen.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - time already spent baking.
    :return: int - total time spent (in minutes) preparing and baking.

    This function adds the preparation time and elapsed bake time to
    get the total cooking time so far.
    """
    prep_time = preparation_time_in_minutes(number_of_layers)
    return prep_time + elapsed_bake_time
