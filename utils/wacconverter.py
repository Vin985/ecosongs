import os
import re
import time

from wac2wav import wac2wav


class WacConverter:
    def __init__(self, root="", dest="", files=[]):
        self.rootDir = root
        self.destDir = dest
        self.files = files

    def files_to_wav(self):
        for fn in self.files:
            self.file_to_wac(fn)

    def file_to_wav(self, filename):
        new = self.regex.sub(self.destDir + "\\1.wav", filename)
        dirname = os.path.dirname(new)
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        self.log("Converting {0} in {1}".format(filename, new))
        time.sleep(1)
        #wac2wav(filename, new)

    def log(self, text):
        print(text)

    def setRootDir(self, rootDir):
        self.rootDir = rootDir
        self.regex = re.compile(r"^" + self.rootDir + "(.*)\.wac$")


# if __name__ == '__main__':
#     wc = WacConverter(
#         "/home/vin/Doctorat/data/acoustic/field/wac",
#         "/home/vin/Doctorat/data/acoustic/field/wav", [
#             "/home/vin/Doctorat/data/acoustic/field/wac/2015/Igloolik24/IGLOOLIK24_20150615_170000.wac"
#         ])
#     wc.files_to_wav()
