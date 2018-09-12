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

    def set_args(self, root="", dest="", compress_old=True):
        self.root_dir = root
        self.dest_dir = dest
        self.compress_old = compress_old
        # Only compile regex if we need to move
        if dest:
            self.regex = re.compile(r"^" + self.root_dir + "(.*)\.wac$")

    def open_archive(self, filename="backup_wac.zip"):
        if self.compress_old and self.root_dir:
            self.archive = zipfile.ZipFile(self.root_dir + "/" + filename, 'w')

    def close_archive(self):
        if self.archive:
            self.archive.close()

    # def backup_wac(self, files):
    #     if self.compress_old and self.root_dir:
    #         with zipfile.ZipFile(self.root_dir + "/backup_wac.zip", 'w') as archive:
    #             for filename in files:
    #                 print("compressing")
    #                 archive.write(filename)

    def files_to_wav(self, files):
        for filename in files:
            self.file_to_wav(filename)

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

    def remove_file(self):
        self.log("removing files")
        for fn in self.files:
            os.remove(fn)

    def log(self, text):
        print(text)


if __name__ == '__main__':
    wc = WacConverter(
        "/home/vin/Doctorat/data/acoustic/field/wac",
        "", [
            "/home/vin/Doctorat/data/acoustic/field/wac/2015/Igloolik24/IGLOOLIK24_20150615_170000.wac"
        ])
    wc.files_to_wav()
