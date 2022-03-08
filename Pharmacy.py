import random


class Event:
    type = ''
    time = 0


def get_next_delay(Lambda):
    return random.expovariate(Lambda)


def get_service_time(exp_time, std_dev_time):
    return random.normalvariate(exp_time, std_dev_time)


def pharmacy(sim_time, daily_working_time, exp_presc_day, exp_prescr_time, stddev_prescr_time):
    busy = False
    queue = 0

    # interesting events
    # a - arrival of prescription
    # f - finishing of prescription filling process
    # s - starting of prescription filling process

    current = Event()
    current.type = 'A'
    current.time = 0

    while sim_time < time:


