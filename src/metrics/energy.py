"""
Energy metrics.
"""


def joules(power_watts, seconds):
    return power_watts * seconds


def energy_per_prediction(power, runtime, predictions):
    return joules(power, runtime) / predictions


def power_efficiency(predictions, joules_used):
    return predictions / joules_used
