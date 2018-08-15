from glob import glob


class FileManager:
    def __init__(self):
        pass

    def wac2wav(self, path):
        pass

    def wac2flac(self, path):
        pass


def get_all_files(root, extensions, recursive=True):
    pattern = root
    if recursive:
        pattern += "/**"
    files = []
    for ext in extensions:
        pattrn = pattern + "/*" + ext
        print(pattrn)
        files.extend(glob(pattrn, recursive=True))
    return (files)


# convert batch from wac to wav

# convert wav to flac?

# create database
