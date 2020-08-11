from collections import namedtuple


def is_df_empty(df):
    return df is None or df.empty


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


def fullclassname(cls):
    return cls.__module__ + "." + cls.__name__


def frange_positive(start, stop=None, step=None, endpoint=True, decimals=2):
    if stop is None:
        stop = start + 0.0
        start = 0.0
    if step is None:
        step = 1.0

    count = 0
    has_end = False
    while True:
        temp = float(start + count * step)
        if temp >= stop:
            if endpoint:
                if has_end:
                    break
                else:
                    temp = stop
                    has_end = True
        if decimals:
            temp = round(temp, decimals)
        yield temp
        count += 1


def range_list(start, stop, step, endpoint=True, decimals=2):
    if isinstance(start, float) or isinstance(stop, float) or isinstance(step, float):
        return list(frange_positive(start, stop, step, endpoint, decimals))
    else:
        res = list(range(start, stop, step))
        if endpoint:
            res.append(stop)
        return res
