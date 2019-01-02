def str2bool(str):
    if type(str) == bool:
        return str
    return str.lower() in ["true", "t", 1]
