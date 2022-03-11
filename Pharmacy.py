import random
import  numpy


class Event():
    type = 'a'
    time = 0


def get_next_delay(Lambda):
    return random.expovariate(Lambda)


def get_service_time(exp_time, std_dev_time):
    return random.normalvariate(exp_time, std_dev_time)


def pharmacy(daily_working_time, exp_presciptions_day, exp_prescr_time, stdev_presc_time):
    # interesting events:
    # (a) arrival of presciptions
    # (s) starting of prescriptions filling
    # (f) finishing of prescriptions filling

    events = []
    busy = False
    in_queue = 0

    e = Event()
    e.type = "A"
    e.time = get_next_delay(exp_presciptions_day / daily_working_time)

    events.append(e)

    while len(events) > 0:

        # pick next event:
        k = numpy.argmin([events[i].time for i in range(len(events))])
        current = events[k]
        events = events[:k] + events[k + 1:]

        # print("handling event at time", current.time, "of time", current.type)
        # print("pharmacist busy: ", busy, "in qeue", in_queue)

        if current.type == "A":

            # Generating a new arrival event
            e = Event()
            e.type = "A"
            e.time = current.time + get_next_delay(exp_presciptions_day / daily_working_time)

            if e.time <= daily_working_time:
                # I could check how many prescription will i lose if i stop working at 5 PM
                events.append(e)

            if not busy:
                e = Event()
                e.type = "S"
                e.time = current.time

                events.append(e)

            else:
                in_queue += 1

        elif current.type == "S":
            busy = True
            # Filling in time
            s_time = get_service_time(exp_prescr_time, stdev_presc_time)

            e = Event()
            e.type = "F"
            e.time = current.time + s_time

            events.append(e)

        elif current.type == "F":
            busy = False

            if in_queue > 0:
                # Start the filling of a new prescription
                e = Event()
                e.type = "S"
                e.time = current.time

                events.append(e)

                in_queue = in_queue - 1

    # return max(current.time, daily_working_time)
    return current.time >= 510
