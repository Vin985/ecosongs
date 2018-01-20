from glob import glob


class FileManager:
    def __init__(self):
        pass

    def wac2wav(self, path):
        pass

    def wac2flac(self, path):
        pass


def get_all_files(root, ext, recursive=True):
    pattern = root
    if recursive:
        pattern += "/**"
    pattern += "/*" + ext
    return (glob(pattern, recursive=recursive))


# convert batch from wac to wav

# convert wav to flac?

# create database
