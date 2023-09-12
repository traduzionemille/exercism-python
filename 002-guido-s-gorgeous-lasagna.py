"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define the 'EXPECTED_BAKE_TIME' constant.
EXPECTED_BAKE_TIME = 40

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    EXPECTED_BAKE_TIME = 40
    remaining_time = EXPECTED_BAKE_TIME - elapsed_bake_time

    return remaining_time


#TODO: Define the 'preparation_time_in_minutes()' function below.
# You might also consider using 'PREPARATION_TIME' here, if you have it defined.
def preparation_time_in_minutes(number_of_layers):
    """Calculate the lasagna preparation time
    
    :param number_of_layers: int - total number of lasagna layers
    :constant PREPARATION_TIME: time it takes to prepare one layer (2 minutes)
    :return: int - preparation time (in minutes) derived from PREPARATION_TIME
    """
    PREPARATION_TIME = 2
    prep_time_in_min = number_of_layers * PREPARATION_TIME
    return prep_time_in_min

    
#TODO: define the 'elapsed_time_in_minutes()' function below.
# Remember to add a docstring (you can copy and then alter the one from bake_time_remaining.)
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the sum of preparation time and elapsed bake time
    
    :param number_of_layers: int - total number of lasagna layers
    :param elapsed_bake_time: int - total minutes elapsed since starting baking
    :prep_time_in_min = int - multiply number of layers by prep time per layer (2 min)
    :return: int - sum of preparation time and elapsed bake time
    """
    PREPARATION_TIME = 2
    prep_time_in_min = number_of_layers * PREPARATION_TIME
    total_cooking_time = prep_time_in_min + elapsed_bake_time
    return total_cooking_time
