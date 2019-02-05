from collections import namedtuple


def str2bool(str):
    if type(str) == bool:
        return str
    return str.lower() in ["true", "t", 1]


def time_from_secs(time):
    minutes, seconds = divmod(time, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    Time = namedtuple("Time", "days hours minutes seconds")
    return Time(days=days, hours=hours, minutes=minutes, seconds=seconds)


def format_s2hms(seconds):
    duration = time_from_secs(seconds)
    return "%d:%02d:%02d" % (duration.hours, duration.minutes, duration.seconds)
