import os
import re
import time
import zipfile

from wac2wav import wac2wav


class WacConverter:
    def __init__(self, *args, **kwargs):
        print("init wacconverter")
        self.set_args(*args, **kwargs)
        self.archive = None

    def set_args(self, root="", dest="", files=[], compress_old=True):
        self.root_dir = root
        self.dest_dir = dest
        self.files = files
        self.compress_old = compress_old
        # Only compile regex if we need to move
        if dest:
            self.regex = re.compile(r"^" + self.root_dir + "(.*)\.wac$")

    def files_to_wav(self):
        for fn in self.files:
            self.file_to_wav(fn)

    def open_archive(self):
        if self.compress_old and self.root_dir:
            self.archive = zipfile.ZipFile(self.root_dir + "/backup_wac.zip", 'w')

    def close_archive(self):
        if self.archive:
            self.archive.close()

    def backup_wac(self):
        if self.compress_old and self.root_dir:
            with zipfile.ZipFile(self.root_dir + "/backup_wac.zip", 'w') as archive:
                for fn in self.files:
                    print("compressing")
                    archive.write(fn)

    def remove_wac(self):
        self.log("removing files")
        for fn in self.files:
            os.remove(fn)

    def file_to_wav(self, filename):
        if self.dest_dir:
            new = self.regex.sub(self.dest_dir + "\\1.wav", filename)
            dirname = os.path.dirname(new)
            if not os.path.exists(dirname):
                os.makedirs(dirname)
        else:
            new = filename.replace(".wac", ".wav")
        self.log("Converting {0} in {1}".format(filename, new))
        wac2wav(filename, new)
        if self.archive:
            print("adding file to archive")
            self.archive.write(filename, filename.replace(self.root_dir, ""))

    def log(self, text):
        print(text)


if __name__ == '__main__':
    wc = WacConverter(
        "/home/vin/Doctorat/data/acoustic/field/wac",
        "", [
            "/home/vin/Doctorat/data/acoustic/field/wac/2015/Igloolik24/IGLOOLIK24_20150615_170000.wac"
        ])
    wc.files_to_wav()
