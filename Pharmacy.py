import random


class Event():
    type = 'a'
    time = 0


def get_next_delay(Lambda):
    return random.expovariate(Lambda)


def get_service_time(exp_time, std_dev_time):
    return random.normalvariate(exp_time, std_dev_time)


def pharmacy(sim_time, daily_working_time, exp_presciptions_day, exp_prescr_time, stdev_presc_time):
    # interesting events:
    # (a) arrival of presciptions
    # (s) starting of prescriptions filling
    # (f) finishing of prescriptions filling

    events = []
    busy = False
    in_queue = 0

    current = Event()
    current.type = "A"
    current.time = get_next_delay(exp_presciptions_day / daily_working_time)

    while current.time < sim_time:
        if current.type == "A":

            e = Event()
            e.type = "A"
            e.time = current.time + get_next_delay(exp_presciptions_day / daily_working_time)
            events.append(e)

            if not busy:

                s_time = get_service_time(exp_prescr_time, stdev_presc_time)

                e = Event()
                e.type = "F"
                e.time = current.time + s_time

                events.append(e)

            else:
                in_queue += 1
